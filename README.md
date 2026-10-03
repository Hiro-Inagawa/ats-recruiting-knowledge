![ATS & Recruiting Knowledge. An industrial obstacle course with ATS lettering leading toward a doorway marked JOB.](docs/ats-recruiting-knowledge.jpg)

# ATS & Recruiting Knowledge

Assess your résumé and LinkedIn profile from a recruiter’s perspective with a skill for Codex and Claude Code.

Built from official ATS documentation, recruiter demonstrations and employer hiring guides, including Greenhouse, Ashby and Workable, the skill explains how applications are processed, searched and evaluated.

The skill connects the assistant to this knowledge to assess your résumé and LinkedIn profile and recommend improvements based on how recruiters and ATS systems review applications.

---

## Example prompts

```text
Use ATS & Recruiting Knowledge to assess my résumé from a recruiter’s perspective and recommend improvements.
```

```text
Use ATS & Recruiting Knowledge to assess my LinkedIn profile and explain what I could improve.
```

---

## What the knowledge covers

### 1. ATS systems and application screening

- How applications become candidate records and structured information.
- Résumé parsing, text extraction and formatting risks.
- Recruiter searches, keywords, filters and candidate rediscovery.
- Application questions, eligibility rules and rejection decisions.
- AI-assisted screening and how candidate evidence is interpreted.

### 2. Résumé, portfolio and candidate evaluation

- Matching experience to job requirements.
- Direct and transferable experience.
- Demonstrating individual contribution, responsibility and seniority.
- Supporting claims with project and portfolio evidence.
- Interview evaluation, scorecards and conflicting feedback.

### 3. LinkedIn profiles and recruiter discovery

- How recruiters find candidates through search and filters.
- Profile sections, terminology and professional evidence.
- How recruiters inspect profiles and assess credibility.
- Search appearances, profile views and what they indicate.
- LinkedIn and ATS integrations.
- Consistency across LinkedIn, résumé and portfolio.

### 4. Recruiter operations

- Defining hiring requirements and approving vacancies.
- Setting up job postings, application questions and evaluation criteria.
- Sourcing through applications, referrals, agencies and previous candidates.
- Screening, shortlisting, interviews and hiring decisions.
- Offers, candidate communication, hiring handoff and vacancy closure.

### 5. Candidate records and process problems

- Duplicate records and multiple applications.
- Missing, incorrect or outdated information.
- Permissions, integrations and synchronization.
- Application statuses, stalled decisions and communication.
- Changed requirements, withdrawals and reopened vacancies.

### 6. Recruiting metrics and AI oversight

- Stage conversion, elapsed time, aging and source attribution.
- How incomplete records and reporting definitions affect results.
- Checking AI assessments against candidate evidence.
- Unsupported inferences, reviewer corrections and automation boundaries.

### 7. Practical guidance and supporting sources

- Workflows for applicant assessments, LinkedIn reviews and recruiter operations.
- Workable and Ashby walkthroughs.
- A worked recruiting case from vacancy approval to closure.
- Local supporting evidence from ATS documentation, employer hiring guides and research.

---

## Installation and use

With Node.js installed, run:

```sh
npx skills add Hiro-Inagawa/ats-recruiting-knowledge --global --agent codex claude-code
```

This installs the skill for Codex and Claude Code across your projects. To install for just one application, use `--agent codex` or `--agent claude-code`.

The repository is private, so installation requires GitHub access through your configured Git credentials, GitHub CLI or SSH.

Start a new chat or session. Invoke `$ats-recruiting-knowledge` in Codex or `/ats-recruiting-knowledge` in Claude Code, then provide your résumé or LinkedIn profile and use an example prompt above.

<details>
<summary>Manual installation with Git</summary>

Run the command for your application in a terminal. These commands work in Windows PowerShell and macOS/Linux shells. Git must be installed. This repository is private, so your GitHub account needs access.

### Codex

```sh
git clone https://github.com/Hiro-Inagawa/ats-recruiting-knowledge.git "$HOME/.agents/skills/ats-recruiting-knowledge"
```

Start a new Codex chat and invoke:

```text
$ats-recruiting-knowledge
```

### Claude Code

```sh
git clone https://github.com/Hiro-Inagawa/ats-recruiting-knowledge.git "$HOME/.claude/skills/ats-recruiting-knowledge"
```

Start a new Claude Code session and invoke:

```text
/ats-recruiting-knowledge
```

Then provide your résumé or LinkedIn profile and use one of the example prompts above. If the destination already contains this skill, update the existing installation instead of cloning over it.

</details>

---

## Maintain the knowledge

Update an owning explanation and its supporting evidence together. Repair affected workflows and navigation. Review changed claims and run relevant checks. Verify application retrieval when behavior changes. Keep revision, acquisition and acceptance records outside the distributed skill. Historical editions are evidence, not competing current sources.

---

## License

Original knowledge, supporting paraphrases and hypothetical examples use CC BY 4.0. Original skill instructions and code use MIT. Third-party sources retain their own rights; complete acquired source documents are not distributed here. [LICENSE](LICENSE) specifies the file mapping and attribution.
