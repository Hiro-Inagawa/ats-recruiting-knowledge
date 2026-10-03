"""Read-only search and exact passage retrieval for the packaged knowledge.

Python 3.9+, standard library only. No network, model calls or persistent index.
"""
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "references"
COLLECTION = Path(__file__).resolve().parent / "collection.json"
AREAS = ("manuals", "workflows", "examples", "evidence", "assessment")
STOP = set("a an and are as at be by for from how in is it of on or the this to what with your".split())


class RetrievalError(Exception):
    pass


def tokens(text):
    return [x for x in re.findall(r"[^\W_]+", text.casefold()) if x not in STOP]


def load(path):
    resolved = path.resolve()
    if not resolved.is_relative_to(ROOT.resolve()):
        raise RetrievalError("File escapes the knowledge directory")
    try:
        raw = resolved.read_bytes()
        text = raw.decode("utf-8-sig")
    except (OSError, UnicodeError) as exc:
        raise RetrievalError("Cannot read knowledge file: " + path.name) from exc
    return text, hashlib.sha256(raw).hexdigest()


def split_units(path):
    text, digest = load(path)
    lines = text.splitlines(keepends=True)
    starts = []
    stack = []
    fence = None
    for i, line in enumerate(lines):
        fm = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fm:
            marker = fm.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            continue
        if fence:
            continue
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            level, title = len(match.group(1)), match.group(2)
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
            starts.append((i, [x[1] for x in stack]))
    if not starts or starts[0][0] > 0:
        starts.insert(0, (0, [path.stem]))
    relative = path.relative_to(ROOT).as_posix()
    area = relative.split("/")[0] if "/" in relative else "assessment"
    result = []
    for n, (start, headings) in enumerate(starts):
        end = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        body = "".join(lines[start:end])
        if not body.strip():
            continue
        result.append({"unitId": relative + "#L" + str(start + 1),
                       "file": relative, "area": area, "headings": headings,
                       "startLine": start + 1, "endLine": end,
                       "fileSha256": digest, "text": body,
                       "sourceIds": sorted(set(re.findall(r"\b(?:ATS|LI|ROP|DEMO)\d{2}\b", body)))})
    return result


def corpus(area=None):
    if not ROOT.is_dir():
        raise RetrievalError("Knowledge directory is missing")
    try:
        members = json.loads(COLLECTION.read_text("utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        raise RetrievalError("Knowledge membership definition is missing or invalid") from exc
    if not isinstance(members, list) or not members or any(not isinstance(x, str) for x in members):
        raise RetrievalError("Invalid knowledge membership definition")
    actual = {x.relative_to(ROOT).as_posix() for x in ROOT.rglob("*.md")}
    if set(members) != actual or len(members) != len(set(members)):
        raise RetrievalError("Knowledge membership changed. Update collection.json with the owning revision")
    for member in members:
        load(ROOT / member)
    files = [ROOT / member for member in sorted(members)
             if member.split("/")[0] in AREAS[:-1] or member == "assessment-method.md"]
    units = [unit for path in files for unit in split_units(path)]
    return [u for u in units if area is None or u["area"] == area]


def search(query, limit=8, area=None):
    terms = set(tokens(query))
    if not terms:
        raise RetrievalError("Query must contain a searchable term")
    units = corpus(area)
    counts = [Counter(tokens(" ".join(u["headings"]) + " " + u["text"])) for u in units]
    average = sum(sum(c.values()) for c in counts) / max(len(counts), 1)
    frequencies = {t: sum(t in c for c in counts) for t in terms}
    ranked = []
    for unit, count in zip(units, counts):
        length = sum(count.values())
        score = 0.0
        for term in terms:
            tf = count[term]
            if tf:
                idf = math.log(1 + (len(units) - frequencies[term] + 0.5) / (frequencies[term] + 0.5))
                score += idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * length / max(average, 1)))
        if score:
            result = {k: v for k, v in unit.items() if k != "text"}
            result.update(score=round(score, 6), excerpt=unit["text"][:500],
                          matchedTerms=sorted(terms.intersection(count)))
            ranked.append(result)
    ranked.sort(key=lambda u: (-u["score"], u["unitId"]))
    return {"query": query, "unitsSearched": len(units), "results": ranked[:limit],
            "note": "Search excerpts are navigation. Read exact units before using their claims."}


def read(unit_id, expected, offset=0, max_chars=6000):
    match = re.fullmatch(r"(.+\.md)#L([1-9]\d*)", unit_id)
    if not match:
        raise RetrievalError("Invalid unit ID; use a returned search unitId")
    relative, line = match.groups()
    if relative not in {u["file"] for u in corpus()}:
        raise RetrievalError("Unit file is not in the searchable knowledge collection")
    path = ROOT / relative
    _, digest = load(path)
    if digest != expected:
        raise RetrievalError("Source changed since search. Search again before reading")
    units = split_units(path)
    index = next((i for i, u in enumerate(units) if u["startLine"] == int(line)), None)
    unit = units[index] if index is not None else None
    if unit is None:
        raise RetrievalError("Unit no longer exists. Search again")
    if unit["fileSha256"] != expected:
        raise RetrievalError("Source changed during reading. Search again")
    text = unit.pop("text")
    if offset > len(text):
        raise RetrievalError("Offset exceeds passage length")
    stop = min(offset + max_chars, len(text))
    return {**unit, "text": text[offset:stop], "offset": offset,
            "totalChars": len(text), "nextOffset": stop if stop < len(text) else None,
            "previousUnitId": units[index - 1]["unitId"] if index else None,
            "nextUnitId": units[index + 1]["unitId"] if index + 1 < len(units) else None}


KINDS = ("material-correction", "evidence-clarification", "presentation-improvement", "optional-preference")


def require_text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise RetrievalError("Nonempty text required: " + name)


def verify_assessment(record):
    """Validate attribution mechanically, not the semantic truth of a conclusion."""
    if not isinstance(record, dict) or record.get("schemaVersion") != 1:
        raise RetrievalError("Assessment schemaVersion must be 1")
    findings = record.get("findings")
    if not isinstance(findings, list) or not findings:
        raise RetrievalError("Assessment requires at least one evidence-bearing finding")
    knowledge_count, subject_count = 0, 0
    for finding in findings:
        if not isinstance(finding, dict) or finding.get("kind") not in KINDS:
            raise RetrievalError("Invalid finding kind")
        for field in ("finding", "consequence", "nextStep"):
            require_text(finding.get(field), field)
        refs = finding.get("knowledge")
        if not isinstance(refs, list) or not refs:
            raise RetrievalError("Every finding requires knowledge evidence")
        for ref in refs:
            if not isinstance(ref, dict):
                raise RetrievalError("Knowledge evidence must be an object")
            for field in ("unitId", "fileSha256", "quote"):
                require_text(ref.get(field), field)
            passage = read(ref["unitId"], ref["fileSha256"], max_chars=50000)
            if passage["nextOffset"] is not None:
                raise RetrievalError("Evidence unit exceeds verification bound")
            if ref["quote"] not in passage["text"]:
                raise RetrievalError("Knowledge quote does not match the exact passage")
            knowledge_count += 1
        subjects = finding.get("subject", [])
        if not isinstance(subjects, list):
            raise RetrievalError("Subject evidence must be a list")
        for ref in subjects:
            if not isinstance(ref, dict):
                raise RetrievalError("Subject evidence must be an object")
            for field in ("file", "sha256", "quote"):
                require_text(ref.get(field), field)
            start, end = ref.get("startLine"), ref.get("endLine")
            if type(start) is not int or type(end) is not int or start < 1 or end < start:
                raise RetrievalError("Invalid subject line range")
            try:
                raw = Path(ref["file"]).read_bytes()
                lines = raw.decode("utf-8-sig").splitlines(keepends=True)
            except (OSError, UnicodeError) as exc:
                raise RetrievalError("Cannot read the supplied subject text") from exc
            if hashlib.sha256(raw).hexdigest() != ref["sha256"]:
                raise RetrievalError("Subject file changed since inspection")
            if end > len(lines) or ref["quote"] not in "".join(lines[start - 1:end]):
                raise RetrievalError("Subject quote or line range does not match")
            subject_count += 1
        if not subjects:
            require_text(finding.get("missingSubjectEvidence"), "missingSubjectEvidence")
            if finding["kind"] != "evidence-clarification":
                raise RetrievalError("Without subject evidence, only evidence clarification is supported")
    return {"validatedFindings": len(findings), "validatedKnowledgeReferences": knowledge_count,
            "validatedSubjectReferences": subject_count,
            "scope": "Exact attribution, file freshness, finding structure and evidence presence",
            "findings": findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    s = commands.add_parser("search", help="Rank current passages by lexical relevance")
    s.add_argument("--query", required=True)
    s.add_argument("--limit", type=int, default=8)
    s.add_argument("--area", choices=AREAS)
    s.add_argument("--json", action="store_true", help="Output is always JSON")
    r = commands.add_parser("read", help="Read an exact, freshness-checked passage")
    r.add_argument("--unit", required=True)
    r.add_argument("--expected-sha256", required=True)
    r.add_argument("--offset", type=int, default=0)
    r.add_argument("--max-chars", type=int, default=6000)
    r.add_argument("--json", action="store_true", help="Output is always JSON")
    v = commands.add_parser("verify", help="Reject incomplete, stale or fabricated assessment evidence")
    v.add_argument("--assessment", required=True, help="Local JSON record; never uploaded")
    v.add_argument("--json", action="store_true", help="Output is always JSON")
    args = parser.parse_args()
    try:
        if args.command == "search":
            if not 1 <= args.limit <= 100:
                raise RetrievalError("Limit must be between 1 and 100")
            result = search(args.query, args.limit, args.area)
        elif args.command == "read":
            if args.offset < 0 or not 1 <= args.max_chars <= 50000:
                raise RetrievalError("Offset must be nonnegative; max-chars must be 1 to 50000")
            result = read(args.unit, args.expected_sha256, args.offset, args.max_chars)
        else:
            try:
                record = json.loads(Path(args.assessment).read_text("utf-8-sig"))
            except (OSError, UnicodeError, ValueError) as exc:
                raise RetrievalError("Cannot read assessment JSON") from exc
            result = verify_assessment(record)
        print(json.dumps({"ok": True, **result}, ensure_ascii=False))
        return 0
    except RetrievalError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
