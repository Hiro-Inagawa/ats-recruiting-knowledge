# Connected recruiter case and reporting calculations

This is a hypothetical instructional case. Names, identifiers, records and dates are invented. The percentages describe this case only. They are not hiring benchmarks, predictions or evidence that a workflow improves outcomes. [Recruiter operations](../manuals/recruiter-operations.md) owns the operating guidance and [its evidence guide](../evidence/source-guide.md) owns attribution.

## The vacancy and consistent identities

PD-AI-01 is a product-design vacancy for an AI-assisted support experience. It has one headcount. Maya is the hiring manager, Robin the recruiter, Jules the design interviewer and Sam the engineering partner. Noor approves headcount and offer terms. Lee owns HR operations. A smaller company could assign several responsibilities to one person without removing the distinct decisions.

The role needs product-design judgment, uncertainty/fallback design and collaboration with engineering. It does not require the designer to own model infrastructure. Version 1 also lists familiarity with one named AI tool as a preference; version 2 replaces that preference with the evidence criterion described below. Four people enter the process. Person P-01 has application A-01 and a duplicate raw record representing that same application. A separate historical application A-OLD belongs to P-01 but is outside this vacancy's cohort. It is not counted as a new applicant or overwritten.

Opening OP-01 is opened September 2. Recruitment is paused September 7–9. When it resumes, the employer's example record convention creates OP-02 for the same approved headcount, preserving OP-01's history. OP-02 is filled September 19. This is one search with two opening cycles, not two hires. Product-specific reopening behavior requires current verification.

## Event sequence

All events use UTC for the example. Day calculations subtract dates using half-open intervals: the start instant is included and the end instant excluded. We use calendar days, not business days. The final report cutoff is September 22 at 23:59 UTC.

| Date | Event and resulting record |
| --- | --- |
| September 1 | Manager proposes requisition PD-AI-01-v1, separating design responsibility from engineering deployment |
| September 2 | Noor approves one headcount. Robin records OP-01 and setup plan v1 |
| September 3 | A-01 agency introduction/application and A-02 direct application received. A-03 is logged through direct intake but its original application timestamp is missing |
| September 4 | A-04 enters through a referral. Raw record R5 duplicates A-01 without an additional application |
| September 5 | Robin screens A-01, A-02 and A-04 against v1. A-03 requires clarification |
| September 6 | Manager replaces a named-tool preference with a criterion about evaluation and fallback decisions. Version 2 preserves engineering deployment as preferred, not essential. Robin reassesses all four against v2. A-03 is declined after clarification under the documented role decision |
| September 7 | Budget reconfirmation pauses recruitment. OP-01 closes with hold reason. Candidates receive a process update |
| September 9 | Noor reconfirms the same headcount. OP-02 opens. Existing application history is linked to the resumed search |
| September 10 | A-01, A-02 and A-04 complete case discussions. A-01's AI assessment and ownership disagreement are recorded |
| September 11 | A-02 withdraws before debrief. Robin records the withdrawal and tells the relevant interviewers |
| September 12 | A-01 and A-04 reach debrief. Manager recommends A-01 after resolving the ownership distinction. A-04 remains under review |
| September 13 | Offer O-01-v1 is created for A-01 |
| September 14 | Noor approves O-01-v1 |
| September 15 | Approved offer delivered to A-01 |
| September 18 | A-01 accepts through the employer's required process |
| September 19 | Authorized operator records A-01 hired against OP-02. Lee acknowledges HR handoff. Start date remains separately confirmed. A-04 is still active despite closure |
| September 22 | Robin reconciles A-04's terminal role decision and candidate communication, preserving prior evaluations |

## Completed operating records

### J/K: approve the work and prepare its assessment

**J-01 requisition:** outcome is a usable assisted-support experience with understandable uncertainty and fallback. Essential criteria are design judgment, evaluation reasoning and engineering collaboration. Infrastructure operations are preferred. Manager owns capability definition, Noor owns headcount/terms authorization, Robin owns process coordination. Decision: approve v1 and later approve the v2 criterion clarification. Neither version makes production engineering mandatory.

**K-01 setup:** recruiter screen checks context and evidence availability. Design case evaluates individual choices and alternatives. Collaboration discussion tests evaluation/fallback reasoning with engineering. Each assessor records observations and distinguishes unestablished evidence. There is no automated disqualification rule. The application asks for a case description but accepts a redacted alternative. Candidate preparation and adjustment contact are stated. Decision: ready for authorized intake.

### L/P: preserve provenance and investigate a duplicate

**L-01 intake:** A-01 is agency-sourced, with current evidence and completion recorded. Agency representation/terms are handled by the client owner. A-OLD is historical and separate. The source field does not establish qualification or full relationship history.

**P-01 discrepancy:** R5 appears to duplicate A-01. Identity/application context is corroborated for this instructional dataset. It is excluded as a duplicate from the report. That analytical deduplication is not an ATS merge. A real merge would require authorization, surviving-field review and integration consequences. The administrator retains the raw-record correspondence. Decision: one report application A-01, no employer-system mutation.

### J/M: change a criterion and reassess

**J-02 change impact:** criterion v2 evaluates design decisions about uncertainty rather than familiarity with one named tool. Robin records affected job text, interview prompts and scorecards. All four applications are reviewed under v2. Earlier v1 observations remain identifiable. No candidate is assessed against a secret late requirement.

**M-01 screening:** A-01 demonstrates fallback design and collaboration. Deployment responsibility remains unestablished. A-02 and A-04 have evidence warranting case discussion. A-03's clarification does not provide the required product-design case evidence for this role and the manager's authorized decision is decline, without asserting general inability. Decision records identify criteria version, material and next communication owner.

### M/N: check AI inference and conflicting feedback

**AI-01:** a generated rationale infers deployment ownership from A-01's prototype case. The case states that Sam's engineering counterpart deployed it. Supported: candidate's prototype/design work. Unestablished: personal deployment ownership. Decision: correct the interpretation through the permitted review process if available and retain the source evidence. Continue design assessment because deployment is not essential under v2.

**N-01 debrief:** Jules writes that the candidate owned the AI experience. Sam writes that the candidate did not own the model service. They describe different responsibilities rather than a factual contradiction. The candidate identifies personal fallback decisions and evaluation examples, while attributing deployment to engineering. Manager records demonstrated design ownership, production engineering ownership unestablished and no unmet essential criterion on that basis. Decision: recommend A-01 with stated role boundaries. A-04's evidence is recorded separately and not overwritten by the selected candidate's result.

### O: withdrawal, offer, handoff and remaining applications

**O-01 withdrawal:** A-02 withdraws September 11 from this application. Optional reason is not supplied. Record that fact without inventing a motive, deleting every person record or classifying the withdrawal as a recruiter rejection. Its case attendance remains in the event history.

**O-02 offer/handoff:** O-01-v1 has distinct creation, approval, delivery and acceptance dates. September 19's ATS hired record is separate from the eventual employment start. Lee acknowledges the handoff of required terms/start-process information and outstanding conditions. Medical or adjustment detail is not copied into a general debrief. Actual legal acceptance conditions remain the employer's responsibility.

**O-03 closure:** OP-02 closes September 19. A-04 remains active until Robin reconciles its application and communication September 22. Opening closure did not prove notification occurred. Historical stage/evaluation events remain available for the report. Decision: vacancy filled, all four application dispositions reconciled, handoff acknowledged.

## Reporting dataset and unit

The cohort is four distinct applications first recorded for this requisition during September 3–4. Inclusion is based on recorded intake evidence, so A-03 can be counted despite its missing original application timestamp. This is an intake cohort, not an elapsed-time cohort or all people in the ATS. The duplicate R5 and unrelated A-OLD are excluded with reasons.

| Application/person | Recorded source | Original application date | Screen event | Case reached | Debrief reached | Final disposition at cutoff |
| --- | --- | --- | --- | --- | --- | --- |
| A-01 / P-01 | Agency | September 3 | September 5 | September 10 | September 12 | Hired, September 19 |
| A-02 / P-02 | Direct | September 3 | September 5 | September 10 | None | Withdrawn, September 11 |
| A-03 / P-03 | Direct | Unknown | Clarification completed September 6 | None | None | Declined, September 6 |
| A-04 / P-04 | Referral | September 4 | September 5 | September 10 | September 12 | Declined/communicated, September 22 |

## Metric contracts and worked calculations

These are instructional definitions chosen for this dataset. Product reports must be matched to their documented events and filters. A metric requiring complete dates excludes missing observations only from that calculation, with missingness disclosed. An empty denominator produces undefined, not zero.

| Metric and purpose | Definition, boundaries and exclusions | Calculation |
| --- | --- | --- |
| Screen-to-case conversion | Distinct cohort applications reviewed at screen/clarification and reaching case by cutoff, divided by all four reviewed. Withdrawals remain included. Exclude duplicate and unrelated application | 3/4 = 75% |
| Case-to-debrief conversion | Distinct case entrants reaching debrief by cutoff divided by all case entrants, including A-02's later withdrawal | 2/3 = 66.7% |
| Intake-to-hire conversion | Applications recorded hired by cutoff divided by the four intake applications. This is observed cohort progression, not a forecast | 1/4 = 25% |
| Withdrawal share | Cohort applications explicitly withdrawn by cutoff divided by all intake applications. Unknown reasons are not imputed | 1/4 = 25% |
| Offer acceptance | Delivered offers accepted by cutoff divided by delivered offers. One delivered offer, no pending response in this case | 1/1 = 100%, one observation |
| Application-to-offer-created | For hired A-01 only, created offer date minus known application date, calendar days. No claim this measures delivery or acceptance | September 13 minus September 3 = 10 days |
| Application-to-offer-delivered | For A-01, delivered offer date minus application date | September 15 minus September 3 = 12 days |
| Application-to-acceptance | For A-01, actual acceptance event minus application date | September 18 minus September 3 = 15 days |
| Application-to-ATS-hired | For A-01, ATS hired event minus application date. Not actual start | September 19 minus September 3 = 16 days |
| Resumed-opening-to-hire | OP-02 open date to ATS hired date. Excludes OP-01's earlier cycle by definition | September 19 minus September 9 = 10 days |
| Original-search calendar duration | OP-01's original open date to ATS hired date, including hold | September 19 minus September 2 = 17 days |
| Original-search active duration | Original calendar duration minus documented hold [September 7, September 9). This is a separately labeled net clock | 17 minus 2 = 15 days |
| Known application-to-screen delay | Mean date difference for A-01/A-02/A-04 only. A-03 cannot enter without a valid application date. No assertion of candidate waiting experience beyond these events | (2 + 2 + 1)/3 = 1.67 days, 3/4 complete |
| Stage age snapshot | At September 18, A-04 is active in debrief since September 12. Date difference measures elapsed residence, not a diagnosed reason | 6 days at that cutoff |
| Completed debrief residence | For A-04, September 12 to terminal record September 22. This is historical residence after closure reconciliation, not current active age | 10 days |
| Recorded-source composition | Source-labeled intake applications divided by four, with unknown source included as its own category if present | Direct 2/4 = 50%, agency 1/4 = 25%, referral 1/4 = 25% |
| Recorded-source hire yield | Hired cohort applications with a label divided by intake applications with that label, at the same cutoff | Agency 1/1, direct 0/2, referral 0/1. These small counts do not establish channel advantage |

### How changed assumptions change the conclusion

If raw rows are used as the intake denominator while case entries are deduplicated, the calculation becomes 3/5 = 60%. That mixes units. If both sides duplicate A-01, it can become 4/5 = 80%. Neither describes the four distinct applications. Record the identity rule and apply it consistently.

If A-02's withdrawal is removed from case entrants, debrief conversion becomes 2/2 = 100%. That answers an assessed-survivor question, not cohort progression. Report it only with that label and retain the withdrawal count. Do not use the changed denominator to claim the process improved.

If A-03's missing application date is treated as zero delay, average screening delay becomes 5/4 = 1.25 days instead of 5/3 = 1.67 days. The apparent improvement is fabricated by an unsupported value. Keep 3/4 completeness visible and investigate the missing timestamp if it matters.

If only the reopened opening is measured, the opening clock is 10 days. If the original search is measured, it is 17 calendar days or 15 active days under the stated hold convention. All can be correct for different questions. None should silently replace the other or imply two hires.

If the report stops September 18 before the ATS hired event, intake-to-hire is 0/4 even though the candidate has accepted. Acceptance and ATS hired recording are different events. An operations review should investigate the event lag, not conclude that no selection succeeded.

Source labels show agency-associated hiring in this case. They do not establish that the agency caused the result, that direct applications are ineffective or that the pattern will repeat. A merge can alter a surviving source field. Preserve the attribution convention and relationship history when comparing reports.

## Completed Q report and next decision

**Q-01:** four applications, one hire, one withdrawal and two declined applications at the September 22 cutoff. Screen-to-case 75%, case-to-debrief 66.7%, intake-to-hire 25%. Elapsed hired-applicant clocks span 10 days to offer creation and 16 days to ATS hired recording. Opening clocks span 10 resumed-cycle days and 17 original-search calendar days. Application-to-screen completeness is 3/4. A-04's three-day post-opening-closure reconciliation delay is identified from September 19–22.

**Decision:** inspect why remaining-application reconciliation occurred after opening closure, and recover A-03's timestamp if elapsed-time reporting requires it. Preserve all clock definitions. Do not change candidate criteria or select a channel based on these four applications. The record supplies a specific process investigation without an invented causal explanation or outcome guarantee.
