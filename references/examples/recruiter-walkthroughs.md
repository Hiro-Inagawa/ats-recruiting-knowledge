# Recruiter walkthroughs: conventional ATS and AI-assisted review

Observed 2026-10-02. This companion explains what a recruiter can inspect, how records differ from decisions, and where AI evaluation adds another judgment to review. It complements Chapters 2, 5, 6, 7, 8 and 10 of [the current manual](../manuals/ats-and-recruiting.md).

Two public vendor demonstrations were inspected. Workable's guided tour was advanced to its closing screen. Ashby's 6:37 release video was inspected at seven selected paused frames; it was not continuously watched. We did not operate a live employer ATS, hear and assess the complete video narration, validate a complete transcript, or observe hiring outcomes. These are product examples, not evidence of a particular employer's configuration or a candidate's rejection cause.

## Conventional example: Workable candidate profile

The starting point is a job and one of its pipeline stages. Selecting a person in that list opens a candidate record. This matters because the list defines which applications the recruiter is looking at; a profile contains information, while a stage expresses a position in a process. Neither by itself establishes suitability.

Combined observation covers 37 unique instruction dialogs in the advertised 37-step tour, including the Profile introduction explaining information supplied during application. This is dialog coverage, not complete pixel transcription, narration assessment or every possible branch.  

| Part of the tour | What was visible or explained | What the recruiter needs to distinguish |
| --- | --- | --- |
| Job and stage | Job selection, stage lists, All, qualified/disqualified lists | Which job application and which subset is being reviewed; an empty subset is not the whole database |
| Candidate browser | Candidate list, sorting controls, selected profile and collapsible browser | List order versus an evaluation; the meaning of a sort depends on its inputs |
| Header and record | Information, tags, source/headline editing controls and Profile tab | Entered information and labels versus verified professional evidence |
| Application material | Résumé/custom-field guidance and Answers tab | File contents, structured fields and application answers may provide different evidence |
| Activity history | Timeline and activity icons | A recorded event versus the reason for a decision; history must be read in context |
| Communication | Messages, Events, reply control and visibility choices | Candidate-facing correspondence versus internal discussion, and which colleagues can see each item |
| Review | Evaluation/scorecard guidance and conditional assessment tabs | A review record versus a selection decision; absent tabs may simply mean no relevant record |
| Internal comments | Comment controls, visibility and team mentions | Collaboration and access settings; an internal UI label is not a guarantee against lawful disclosure |
| Offer and files | Conditional Offer tab, sample approval state, Files tab and overview | Preparing an offer, obtaining approval and hiring are separate events |

These distinctions are useful before discussing automation. A recruiter can encounter structured fields, human evaluations, communication and process states within the same record. A badge or stage cannot explain which person read a résumé, whether a criterion was met, or why the employer stopped considering the application.

The tour's guidance says event evaluations can be hidden until a reviewer submits their own, with administrator exceptions. It also describes integration-dependent external-message import and conditionally displayed tabs. Those statements were read in the guided dialogs. We did not test backend permissions, imports or whether hidden evaluations reduce bias. Treat them as documented demo guidance requiring tenant-specific verification before operational use.

The observer used guided navigation only. No real information was edited, message sent, evaluation submitted, offer approved or candidate deleted. Menu and button presence establishes that a control appears in the demo, not that the observer exercised it successfully.

## AI example: Ashby application review

This is a separate 2024 release demonstration, not the later keynote transcript already used in the manual. The player identifies Chapman Swaine as presenter. The official page captured on October 2, 2026 displays September 9, 2024. ATS04 metadata records September 10. The publication-day discrepancy remains unresolved; [DEMO02](../evidence/assessed-passages/DEMO02.md) explains the observation scope.

The sampled sequence connects configured criteria, an application queue, generated explanations, reviewer correction and candidate actions. It does not establish the current release, subscription entitlement, accuracy or fairness of the system.

| Observed player time | Visible material | Decision lesson and limit |
| --- | --- | --- |
| 2:23 | Job settings and Edit Job Criteria; short titles and prompts; add-criterion control | The assessment depends on what the employer asks it to evaluate. Sample sales requirements are not general hiring standards |
| 2:57 | A university-list criterion and EEO Warning | A warning can prompt scrutiny; its presence does not demonstrate a lawful or fair criterion |
| 3:29 | Application queue, per-criterion badges, AI quick filter marked Beta | A filtering mechanism appears in this historical demo. The sample count of 63 applications is not a benchmark |
| 4:02 | AI-generated evaluation says Meets 3 of 4, alongside application answers and résumé; separate advance/reject controls | A criterion count is not a universal ATS score. Suggested assessment and candidate action are separate controls |
| 4:16 | Expanded rationales quote résumé material; one positive revenue rationale says likely exceeding when relating a multi-year result to a criterion | Inspect time basis, attribution and inference before accepting the conclusion. This sample was not independently checked against the complete résumé |
| 4:39 | Flag Evaluations dialog with Meets, Does not meet, Undecided and optional feedback | A reviewer correction route is visible. We did not submit it or test its downstream effects |
| 5:19 | Privacy, transparency and accountability slide | Redaction, training restrictions, disclosure, audits and other assurances are vendor claims on a slide, not independently established outcomes |


At 4:16 the rationale's wording makes inference visible. It would be premature to call the evaluation wrong: a multi-year result might support a particular annual conclusion, depending on the figures and what the criterion means. It would also be premature to certify it as correct without checking the complete evidence. The useful review asks whether the time period, individual responsibility, revenue type and required threshold actually align.


The visible override options include Undecided. Ashby's assessed written release also documents unknown/skipped states, but those states were not observed in these seven frames. Keep the article's claims separate from the screen observations. A blank or uncertain result should not silently become evidence that an applicant lacks the capability.

## Practice record 1: inspect a conventional application

This exercise is hypothetical. A recruiter is reviewing a product designer in an interview stage. The résumé describes a redesign, an application answer describes research responsibilities, and the offer area has no record.

Record the job and application identity first, then the material inspected and its version. Map one requirement to the relevant answer or portfolio evidence. Check the evaluation record for an actual review rather than treating the stage label as a recommendation. Read permitted communication to establish what the candidate has been told. If a required approval is not visible, record it as unknown and ask the responsible colleague.

Resulting record: **Application:** designer role, interview stage. **Evidence read:** submitted résumé and research answer. **Supported:** participation in redesign research. **Missing:** who owned the decisions and what changed after release. **Decision:** obtain a focused example in the interview before assessing ownership. **Process limit:** no offer record inspected; no conclusion about offer approval or candidate notification. This produces a next question, not an invented pass/fail score.

## Practice record 2: challenge an AI rationale

This exercise is hypothetical. A requirement asks for independent production deployment experience. A rationale cites a prototype and says the applicant probably has deployment skills. Available evidence does not state that they deployed it.

Resulting record: **Criterion:** independent production deployment. **Cited evidence:** prototype construction. **Supported:** prototyping experience. **Inference:** production deployment. **Missing:** release responsibility, reliability work and operating environment. **Decision:** leave deployment unestablished and ask for a concrete release example; correct the assessment through the permitted review route if appropriate. **Limit:** this does not imply the applicant cannot deploy, or that the AI system is always inaccurate.

If the applicant then provides a production case, reassess the criterion against that case. Preserve the distinction between newly supplied evidence and what the original résumé supported. The knowledge should revise its conclusion when the facts change.

## Practice record 3: interpret a missing notification

This exercise is hypothetical. A record is marked rejected, but the applicant reports no email. A demo shows a separate rejection/email control with a configurable delay.

Resulting record: **Known:** process status and applicant report. **Plausible:** email not selected, pending scheduled send, delivery problem, or an incomplete record. **Needed:** authorized communication history and actual send configuration. **Decision:** verify those records before explaining the cause. **Limit:** the demo's sample three-day delay is not a recommended follow-up interval or evidence of this employer's setting.

## How to apply this companion

Use it when a screen label is being mistaken for a hiring decision, when comparing conventional review with AI-assisted review, or when learning what a recruiter inspects. Necessary inputs are the question, the actual evidence available and whether you are examining a vendor sample or an employer record. The resulting record should identify observed facts, assessed source claims, missing facts and the next permitted decision.

For a real employer system, verify current documentation, account permissions and configuration before following exact UI instructions. Do not use these demonstrations to infer private rules, bypass access, manufacture qualifications or promise better application outcomes. Wider employer rubrics, independent AI evaluations and real authorized case observations remain useful additions; these two vendor examples do not supply them.

## Supporting observations

[DEMO01](../evidence/assessed-passages/DEMO01.md) explains the Workable observation scope. [DEMO02](../evidence/assessed-passages/DEMO02.md) explains Ashby's sampled frames and the unresolved page-date discrepancy. Ashby's full narration remains unassessed: no verified complete transcript or caption track was available in the inspected player. Generated highlights are not a transcript. For decisions beyond the observation, use [Recruiter operations](../manuals/recruiter-operations.md) and its written evidence.
