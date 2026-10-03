# Structured assessment records

Use schema version 2 for a full résumé or LinkedIn assessment. Broad explanatory questions and focused follow-ups can remain conversational. Historical version-1 records check findings only and do not establish full coverage.

## Select the criteria

Run `criteria --asset resume|linkedin|both --mode general|target-role|consistency --json` through the packaged program. General mode examines the supplied professional evidence without a private employer rubric. Target-role mode needs an actual vacancy or a sufficiently defined target. Consistency mode examines at least two supplied assets, which may include a portfolio.

The response supplies `catalogueSha256`, the required `checkId` values, input requirements and eight report sections. Do not choose a smaller set of checks to obtain a favorable result. Read the relevant [criteria explanations](criteria.md) and owning passages through search and exact read before applying thresholds. A quoted rule does not itself justify the conclusion.

## Start the record

Run `scaffold --asset resume|linkedin|both --mode general|target-role|consistency --inputs <inputs.json> --output <new-record.json> --json`. The inputs file is a JSON list of inspected inputs with `id`, `asset`, `kind`, `file`, `label` and, where required, `context` or `derivedFrom`. Paths resolve against the inputs file. The command fingerprints each input, lists every required check with its criterion explanation and prefills a check whose required input is unavailable as a limited result. It never overwrites an existing file. Complete each remaining check, the findings and the summary. Keep the prefilled criterion reference, because every check must cite its explanation or owning chapter. Add the owning passages the result rests on beside it.

Run `locate --file <input> --quote "exact text" --json` to obtain the line range and fingerprint for a subject quotation.

## Record inspected inputs

Keep inputs, extracted text and records in a private working location outside the skill and public repository. Do not copy real personal documents into tests. Use a temporary private working location if the user has not requested durable saving.

Each input has `id`, `asset`, `kind`, `file`, `sha256` and a readable `label`. Relative paths resolve against the assessment JSON's directory. The fingerprint describes the actual bytes. Text evidence is UTF-8, with an optional BOM. Preserve exact quotations, including line endings when quoting multiple lines.

Supported input kinds are `resume-text`, `profile-text`, `live-profile-capture`, `original-file`, `extraction-observation`, `target-requirements`, `portfolio-text` and `user-fact`. Assets are `resume`, `linkedin`, `portfolio`, `target` or `context` as appropriate.

An original file can be binary. Its text is represented by a separate inspected text input. An `extraction-observation` needs a `derivedFrom` input ID pointing to the inspected original and a `context` describing the actual method and observation. A live capture needs context identifying capture scope/date. A `user-fact` needs context identifying it as user-supplied. It does not become independently verified employer history.

Input requirement categories mean:

| Category | Necessary input |
| --- | --- |
| content | Inspected résumé/profile text for the selected asset |
| original | The inspected original file for that asset |
| extraction | An observation tied to that original |
| target | Supplied target requirements |
| comparison | Inspected content from at least two different assets |

Only claim an inspection that occurred. Text extraction does not establish visual appearance or a proprietary ATS import. A dated profile capture does not establish today's account settings.

## Record coverage

Each coverage entry contains `checkId`, `result`, `explanation`, `knowledge` and `subject`. Results are `meets-criterion`, `needs-attention`, `insufficient-evidence` or `not-applicable`.

Knowledge evidence uses the existing `unitId`, `fileSha256` and exact `quote` fields. At least one reference must retrieve the criterion's explanation or owning chapter. Other supporting passages can be added. Subject evidence adds `inputId` to the existing `file`, `sha256`, `startLine`, `endLine` and `quote` fields. It must match a registered inspected text input. Line numbers count newline characters only, as grep and editors do. A page break from PDF extraction stays inside its line, so keep the extracted text unchanged.

A positive result needs both relevant knowledge and subject evidence. A target comparison also quotes target requirements. A consistency check quotes at least two different assets. An extraction check quotes its observation.

`not-applicable` requires `reason`, inspected evidence and a criterion that permits context-based non-applicability. It cannot hide a missing required input. Optional Featured material can be unnecessary for a purpose where another appropriate evidence route already exists. An omitted capture section is instead unavailable inspection material.

`insufficient-evidence` requires `reason` and `missingEvidenceType`. Use `missing-input` plus a nonempty `missingInputs` list for an unavailable original, target, capture section or other necessary input. Subject evidence may be absent for that unavailable input. This produces a limited assessment. Use `unestablished-claim` when actual inspected material does not establish the claim. Subject evidence is then required, and the inspection can still be complete.

## Job-description requirements

In target-role mode with supplied target requirements, add a `requirements` list with one row per requirement in the posting. Each row has a stable `id`, the requirement `text` quoted exactly from the target, `type`, `status`, `explanation` and `subject` evidence. Type is `required` or `preferred` as the posting states it. Treat an unmarked requirement as required and state that assumption in the explanation. When one posting line names two capabilities and the evidence differs between them, give each capability its own row and quote the part of the line it covers. Status is `demonstrated`, `transferable`, `not-shown` or `contradicted`, the screening categories in recruiter operations R4.

One subject reference must quote the requirement text exactly from the target input. Every status except `not-shown` also needs evidence from the assessed material. Not shown means the supplied material does not establish the requirement, not that the person lacks it. The report lists required rows before preferred rows. Other modes, and a target-role assessment without a target, carry no requirement rows.

## Findings and supported summaries

`findings` is a list and can be empty. Each finding has a stable `id`, nonempty `checkIds`, `kind`, `priority`, `certainty`, `finding`, `consequence`, `nextStep`, `knowledge` and `subject`. When no subject evidence can be inspected, only an evidence clarification is valid and `missingSubjectEvidence` names the exact missing input.

Kinds remain `material-correction`, `evidence-clarification`, `presentation-improvement` and `optional-preference`. Priorities are `address-first`, `improve-next` and `optional`. Certainty is `demonstrated` or `conditional`. A material correction must be demonstrated. Optional preferences must remain optional. Only a material correction or an evidence clarification can be ranked address-first. A presentation improvement is ranked improve-next or optional. An insufficient-evidence check supports clarification, not an established defect.

Every needs-attention check links to a finding. A finding cannot contradict a passed check. Keep its evidence tied to the actual issue, not merely another passage in the same document.

`summary` contains `purpose`, `conclusions` and `strengths`. Conclusions and strengths are lists of objects containing `text` and `checkIds`. Strengths reference passed checks. Conclusions reference assessed checks or explicit evidence gaps. Read their evidence before making an overall judgment. Do not infer universal safety, selection probability or recruiter interest from a clean local assessment.

## Reassessment

When a user corrects a fact, preserve the correction as user-supplied evidence and update affected checks. Do not defend the earlier assumption. If a document changes, fingerprint and inspect the new material rather than reusing stale references.

An optional `reassessment` list contains `previousFindingId`, `state`, `explanation` and current `checkIds`. States are `resolved`, `remaining` or `new`. Findings may also include a `supersedes` list of previous finding IDs. The explanation must establish why the assessment changed. Links alone do not establish that an issue was resolved.

Preserve settled stylistic choices. Reopen them only when requested or when new evidence establishes a consequential problem. Resolving one finding does not require inventing a replacement. Historical records remain outside the package.

## Validate and present

Run `verify --assessment <record> --json`, then `report --assessment <record>`. Report also validates independently before emitting Markdown. Errors return JSON with `ok: false` and exit code 2. Do not present an invalid record as a completed audit.

The default renderer includes all eight sections, concise successful checks, detailed recommendations and supported strengths. It states unavailable inspection inputs next to the assessment. It does not add judgments beyond the checked record. Use `report --assessment <record> --detail evidence` when deeper attribution is requested.

Keep machine paths, fingerprints and production receipts out of report prose. Exact evidence-detail output uses package-relative knowledge unit IDs. The code checks structure, coverage, freshness and exact attribution. The reasoning pass must separately establish that each quotation supports the conclusion, that a recommendation applies to the stated purpose, and that a stylistic preference has not become a defect.
