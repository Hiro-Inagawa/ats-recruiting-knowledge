# Recruiter operations

This manual explains how a recruiter moves from an approved hiring need to a documented selection, offer and handoff. It also explains how to investigate records and reports when the process does not behave as expected. The context is professional hiring, particularly product design and work involving AI.

The operating recommendations are synthesis from assessed documentation and employer practices. Examples and records are hypothetical. Explicit product statements identify their evidence IDs. No workflow claims to reproduce every employer's policy or every ATS configuration. The [operations evidence guide](../evidence/source-guide.md) provides exact local passages. The [ATS manual](ats-and-recruiting.md) owns parsing, search and applicant interpretation; the [LinkedIn manual](linkedin.md) owns discovery and profile evidence. The [connected vacancy case](../examples/recruiting-case-and-metrics.md) carries the records through one complete process.

## Responsibilities and operating records

The hiring manager owns the work requirement and recommendation about capability. The recruiter coordinates intake, evidence collection, progression and communication. Interviewers assess assigned criteria and preserve their observations. The approver authorizes the opening or terms according to the organization's policy. HR operations receives the accepted hire, records the handoff and manages the next employment-process steps. System administrators own access and configuration. Privacy, legal and accessibility specialists resolve questions outside a recruiter's authority.

One person can perform several roles in a small organization. Keep the responsibilities distinguishable even when names repeat. A founder's decision to hire does not remove the need to document the requirement, permitted budget, candidate evidence and next action. In a larger organization, identify which decision needs which approver rather than sending every action to everyone.

An agency can introduce and coordinate a candidate without owning the client's requisition, final selection or offer authorization. Record the client owner, permitted submission route, representation basis and communication responsibilities. Flowserve's historical agency guide illustrates candidate-completion steps after introduction, not a universal rule that an agency submission completes an application. [ATS24.] Engagement terms belong to the relevant contract owner, not to an inferred ATS source label.

Use distinct identities for person, application, requisition/opening, evaluation and offer. A person can have several applications. An application can have several evaluations and offer versions. An opening can be paused or replaced while its job title remains unchanged. These distinctions prevent one record from silently overwriting another decision. They are the organizing model used by the examples, not a required database schema.

## R1. Requirements and requisitions

A requisition turns a business need into a hiring decision with an owner and limits. Begin with the work that must happen, why it cannot reasonably be covered by the existing arrangement, and what success would look like. A title alone cannot establish required seniority, budget or evidence. A team asking for a senior designer may actually need delivery capacity, research leadership or technical product judgment. Those needs imply different criteria and interview coverage.

Separate capabilities needed on entry from capabilities that can be learned with available support. Define must-have conditions narrowly enough that the manager can explain their job relevance. Define preferences separately so that a familiar tool or employer name does not become an accidental veto. The decision is whether the organization can support someone who meets the essential work requirement, not whether every candidate resembles the previous employee. OPM describes job-related interview competencies and evaluation structure. GitLab's published design family distinguishes responsibilities across levels. [ROP10; ATS14.] The particular criterion design below is synthesis.

### Application and decision guidance

The manager supplies outcomes, essential functions, expected independence and support. The recruiter tests whether each criterion can be assessed with available evidence. The approver confirms the headcount and financial boundary. Record employment type, location constraints, reporting relationship and the responsible policy owner where these matter. Do not turn unverified eligibility assumptions into disqualification rules.

For a design role involving AI, distinguish designing an AI experience, evaluating model behavior, implementing a prototype and operating production infrastructure. A designer may need to reason about uncertainty and failure without being the engineer responsible for deployment. Ask what the person must own. Where engineering ownership is required, collect engineering evidence. GitLab's ML family explicitly discusses security, performance, collaboration and concept-to-production ownership for engineering roles. It does not make those requirements mandatory for designers. [ROP13.] Existing Chapter 7 explains the evidence distinctions.

Choose approve, revise or pause. Approval means the stated need and boundaries are authorized. Revision means a specific criterion, scope or budget remains unresolved. Pause means recruitment should not create expectations the organization cannot currently fulfill. Product approvals differ. Greenhouse documents job and offer approvals, and one-stage versus two-stage job approval behavior. Some one-stage changes do not automatically request reapproval. A governance review after a material change is an operating recommendation, not a claim that software always enforces it. [ROP01/02.]

### Worked example and completed record

The team needs a designer to improve an AI-assisted support interface. It originally asks for five years with a named model framework, but the work is interaction design and evaluation with an engineering partner. The manager replaces the proxy with demonstrated decisions about uncertain output and fallback behavior.

**Record:** requisition PD-AI-01, version 1. Owner: hiring manager. Outcome: usable assisted-support flow with observable fallback behavior. Essential: product-design judgment, evidence-based decisions and engineering collaboration. Preferred: prior AI product work. Production infrastructure ownership: assigned to engineering. Headcount: one approved opening. Decision: approve the design search, with infrastructure experience assessed as a preference. Next step: recruiter prepares versioned criteria and interview coverage. Unresolved: actual compensation/legal constraints require the employer's approved policy.

### Essential, advanced and common mistakes

Essential practice is a clear work requirement and named decision owner. Advanced practice records criterion versions and a change-impact review. If requirements change after intake, identify which candidates need reassessment, what evidence is missing and what must be communicated. Preserve prior decisions and their basis instead of rewriting history to make the revised process look original.

Common mistakes are copying an old role unchanged, confusing prestige with capability, advertising before approval, and adding a late requirement only to justify a favored outcome. Escalate changes to headcount, terms, eligibility or essential responsibilities to the corresponding owner. Unknown facts are the employer's actual authority chain, job needs and permissible constraints. Use workflow J.

## R2. Job and process setup

The job description communicates the work. The interview plan defines how evidence will be collected. The scorecard organizes judgments. Application questions collect information. A screening rule acts on a configured input. These are related artifacts, but none substitutes for the others.

A useful setup maps every important criterion to an evidence opportunity and an assessor. If a criterion has no planned evidence source, the team will either guess or add an unplanned interview later. If several interviews assess the same criterion and none covers another essential capability, the process consumes time without completing the decision. Greenhouse documents stages containing interviews, focus attributes and interview kits. Stage naming also affects reporting. [ROP03/04.] The allocation method below is synthesis, not a product requirement.

### Application and decision guidance

For each stage, state its purpose, entrance conditions, assigned owner, required record and possible exits. Keep stage names stable enough that reports can compare meaningful activities. A recruiter screen and manager review can be separate decisions even if they happen in the same week. Do not create a new stage name for every interviewer or calendar event unless it represents a distinct process state.

Map requirements to questions or work samples. Ask for evidence that the candidate can reasonably share. Offer an alternative when confidentiality prevents showing a client's material. A portfolio presentation can use redacted artifacts or a reconstruction that makes its status clear. Limit take-home work to the assessment purpose, explain expected effort and evaluation criteria, and establish who decides any compensation or policy conditions. These are candidate-treatment recommendations, not an adoption of historical Monzo time expectations. [ATS16 supplies a historical contrasting format.]

Review automatic rules separately. Greenhouse's documented application rules require configured questions and support different actions under stated product conditions. An answer appearing in the application does not prove any action was configured. [ATS02.] Before an authorized operator enables a rule, document its criterion, input, action, exception handling and test cases. An unknown answer is not automatically an ineligible answer. Do not use indirect proxies for essential requirements without a justified, reviewed basis.

Provide candidates with the next stage, preparation requirements, accessibility contact and how updates will be communicated. Keep adjustment arrangements separate from general assessment notes. In covered US circumstances, EEOC guidance distinguishes job-function questions from medical inquiries and explains accommodation and confidentiality conditions. [ROP11.] Verify jurisdiction and policy before making legal assertions. The practical aim is a process that evaluates the intended capability rather than an avoidable access barrier.

### Worked example and completed record

The design team has three interviews but no one is assigned to evaluate failure-state decisions in the AI flow. The recruiter replaces a duplicate general conversation with a focused case discussion. A portfolio alternative is available for candidates unable to share confidential work.

**Record:** plan PD-AI-01-v1. Screen owner: recruiter, confirming work context and evidence availability. Case owner: design interviewer, assessing problem framing, interaction quality and individual decisions. Collaboration owner: manager/engineering partner, assessing uncertainty and delivery boundaries. Scorecard: evidence plus judgment for each assigned criterion, with unassessed fields left unestablished. Automated disqualification: none enabled. Candidate preparation: one case, redacted alternative accepted. Decision: ready for intake after approval/access review. Next step: publish through the authorized operator, not through knowledge use alone.

### Essential, advanced and common mistakes

Essential practice is matching criteria to assessment and telling candidates what to expect. Advanced practice calibrates interviewers using a hypothetical response and records why questions were changed. Pilot the process before using it at scale, but do not infer effectiveness from a tiny sample. Common mistakes include copying irrelevant scorecards, enabling a rule without exception handling, leaving assessment ownership implicit and letting stage names drift across jobs. Unknowns are actual enabled configuration, accessibility needs and organizational policy. Use workflow K.

## R3. Sourcing and intake

Sourcing identifies potentially relevant people. Intake establishes what record, permission and application belong to the hiring process. A discovered profile, an agency introduction and a submitted application are different events. Treating them as one event creates both attribution errors and communication failures.

Choose the route according to the work requirement and the available evidence. For a role requiring a case discussion, an initial search can identify relevant experience, but it cannot establish private contribution or willingness to apply. LinkedIn's member, Recruiter and integration features are explained in existing Chapters 11–15. A product's search or saved-profile feature does not establish buying or hiring intent. [LI03/04/08/09/12.] This chapter owns the transition into the recruiter's process.

### Application and decision guidance

Record what was found, where it came from, the date, who introduced it and the next permitted action. Use the organization's approved communication and data-handling process. Do not import unnecessary personal information merely because it is public. A source label records a convention; it may omit later relationships or earlier visits. Workable's source documentation demonstrates why attribution and relationship history can differ. [ATS23.]

For a direct applicant, establish the job, application identifier, submitted evidence and receipt. For a referral, record the referrer separately from the candidate's qualifications and application completion. For an agency introduction, verify client ownership, permitted representation and whether the candidate must finish additional steps. A prior applicant requires the appropriate current record/access and evidence of relevance to the new opening. Prior rejection does not prove current unsuitability, and old consent or retention cannot be assumed sufficient for every future use.

When a candidate appears twice, investigate identity before treating the records as duplicates. A person may legitimately apply to several jobs. Conversely, two similar names may belong to different people. Identity review and merge consequences belong to R7. Intake should preserve the application context while that review happens rather than inventing a new global status.

Separate intake completeness from qualification. If a requested document is absent, ask whether it was required, whether the route supports attachments and whether an alternative evidence source exists. An agency completion step or a delayed form is a process problem until the actual capability has been assessed. Do not reject someone for an apparently absent field without knowing the relevant requirement and permitted remedy.

### Worked example and completed record

An agency introduces a designer using a profile that already exists from an earlier application. The current opening needs different evidence. The recruiter records the introduction without replacing the earlier job history or claiming a second person exists.

**Record:** person P-01, prior application A-OLD, new application A-01 for PD-AI-01. Route: agency introduction, received September 3. Agency relationship: recorded separately, contractual ownership unresolved with client owner. Current evidence: résumé received, case not yet supplied. Decision: request the approved application-completion step and a permitted case example. Next step: client recruiter checks the candidate's completion and permissions. Limit: introduction is not qualification or final authorization to contact through an arbitrary channel.

### Essential, advanced and common mistakes

Essential practice records provenance and distinguishes person from application. Advanced practice preserves both system attribution and human relationship history with their different meanings. Common mistakes are awarding qualification from a referral, replacing current evidence with an old résumé, treating profile access as consent for any reuse, and counting duplicate introductions as additional applicants. Unknowns include representation terms, current availability and lawful reuse conditions. Use workflow L.

## R4. Screening and shortlisting

Screening answers whether the available evidence justifies the next assessment step. It is not a certification that every requirement has been met. Eligibility conditions, work capability, evidence completeness and competition for a limited opening can lead to different decisions. Recording only a thumbs-up or thumbs-down loses those distinctions.

Use the approved criterion version. For each important requirement, distinguish demonstrated, transferable, unestablished and contradicted evidence. These are explanatory categories in this manual, not a universal ATS rating scale. Direct evidence shows the relevant responsibility in context. Transferable evidence supports a reason to investigate an adjacent capability. Missing evidence means the record does not yet establish the claim. Contradictory evidence requires review of what is actually incompatible.

### Application and decision guidance

First identify the application and material assessed. Then connect an observation to a criterion. A title, tool name or prestigious employer can guide a question, but it is not proof of the person's contribution. A portfolio result produced by a team should lead to questions about the candidate's decisions and scope. A prototype can establish exploration skill without establishing deployment responsibility. Existing Chapter 7 owns those evidence distinctions.

Choose advance, clarify, hold or decline using a stated reason. Advance when the available evidence warrants the planned next stage. Clarify when a decisive missing fact can reasonably be obtained. Hold only with an owner and a reason, not as a substitute for making a decision. Decline when a relevant requirement is demonstrably unmet or the authorized comparative decision has been made. Preserve whether the reason concerns eligibility, evidence, role fit or the opening's circumstances.

Apply equivalent criteria across candidates while allowing equivalent evidence formats and necessary adjustments. Consistency is about the capability assessed, not forcing every person into an identical barrier. If the process changes materially, review previously assessed candidates affected by the change. Do not apply a late requirement only to remaining applicants without considering earlier decisions.

If AI assists review, read the actual criterion and rationale, then check the underlying evidence. A criterion badge can represent a generated judgment, not a verified fact. Ashby's written release and selected frames show explanations and reviewer controls. The demos do not establish accuracy or employer use. [ATS04; DEMO02.] R9 owns AI scrutiny. Screening rules and notification must also be distinguished: a rejection record and a message can be separate actions. [ATS02/19.]

### Worked example and completed record

A designer's case shows evaluation of uncertain output and collaboration with engineers. It does not state who deployed the model. The role requires design judgment, while deployment ownership is a preference. The recruiter advances the candidate for an evidence discussion without crediting the missing responsibility.

**Record:** application A-01, criteria v1, material case C-01 and résumé R-01. Demonstrated: design decisions about fallback behavior. Transferable: delivery collaboration. Unestablished: production infrastructure ownership. Contradiction: none. Decision: advance to case discussion. Question for interviewer: which decisions did the candidate personally own, and how was behavior evaluated? Communication owner: recruiter. Limit: advancement is permission for further assessment, not an offer recommendation.

### Essential, advanced and common mistakes

Essential practice is a criterion-linked reason and an explicit next step. Advanced practice reviews inconsistent screening decisions and separates rule behavior from reviewer judgment. Common mistakes are treating omissions as inability, penalizing an adjustment, using keyword matches as capability, and allowing an AI rationale to supply evidence that is not present. Escalate unresolved eligibility, sensitive information or an unapproved criterion to the responsible owner. Use workflow M.

## R5. Interviews and evaluation

An interview collects evidence the earlier record could not establish. Its purpose is narrower than deciding whether the interviewer likes the candidate. Assign criteria before the conversation, use questions suited to them, and preserve the answer separately from the judgment. OPM describes job-related questions and individual ratings before discussion. [ROP10.] Greenhouse documents scorecard attributes, assignment and configurable visibility. [ROP04.]

For a design case, examine the problem, constraints, alternatives, decisions and contribution. A polished artifact may establish craft but not research ownership or influence on delivery. Ask what changed because of the candidate's decisions, what they could verify and what remained uncertain. Distinguish a measured result from a plausible interpretation or a team-wide outcome. For seniority, examine the expected scope and independence rather than substituting years for responsibility.

### Application and decision guidance

Use comparable lead questions and evidence standards for the same requirement. Follow-up can clarify a person's answer without changing the competency being assessed. Record the material and version inspected, relevant observations, interpretation and confidence. If a criterion was not assessed, leave it unestablished. A blank field is not a negative finding. GitLab's published design interview guidance specifically connects assessments to covered evidence and explains justification records. [ATS15.]

Employer examples differ. GitLab's published process uses rubric-linked scorecards and a manager justification. The historical Monzo account emphasizes application answers, a design challenge, feedback and a cross-functional workshop. [ATS15/16.] Neither establishes a universal interview sequence. The contrast supports choosing an assessment that answers the role's question and making its burden explicit. Do not copy historical durations, vote thresholds or culture criteria as general recommendations.

For AI work, ask which part the person owned: interaction and uncertainty design, evaluation, model implementation, deployment, monitoring or support. A GitLab engineering job family supplies a production-ownership example for engineers, while its design family discusses design judgment about AI. [ROP13; ATS14.] The recruiter's task is to assess the actual role, not to demand every technical specialty from anyone who mentions AI.

Collect individual notes before a group debrief where feasible. Resolve disagreement by identifying whether the interviewers saw different evidence, used different criteria or interpreted the same observation differently. Do not mechanically average incompatible ratings. The hiring manager records the remaining gap, its effect on the recommendation and available support. If a decisive criterion was never assessed, arrange a focused clarification or retain the uncertainty rather than laundering it into consensus.

### Worked example and completed record

One interviewer writes that a designer owned the AI system. Another writes that the designer only made the interface. The case shows the candidate designed fallback interactions and co-defined evaluation examples, while engineering owned deployment. The disagreement partly concerns the meaning of ownership.

**Record:** evaluation E-01, application A-01. Observation: candidate explained fallback trade-offs and personally created evaluation scenarios. Engineering deployment: explicitly attributed to another team member. Interpretation: demonstrated design ownership, engineering ownership unestablished. Debrief decision: assess against design responsibility, not an invented full-stack requirement. Follow-up: ask how their scenarios affected release decisions. Manager recommendation: pending that evidence. Limit: team success does not establish each contributor's responsibility.

### Essential, advanced and common mistakes

Essential practice is evidence-linked feedback and assessed-versus-unassessed distinction. Advanced practice calibrates criteria, documents disagreement and reviews unnecessary assessment stages. Common mistakes are vague culture-fit labels, allowing confident interviewers to overwrite earlier evidence, treating fluency as proof, and interpreting every missing score as failure. Unknowns include confidential evidence that cannot be inspected and the employer's actual level expectations. Use workflow N.

## R6. Offers, handoff and closure

A positive selection recommendation is not an approved offer. Offer preparation, authorization, delivery, acceptance, ATS hired recording and employment commencement are separate events. Keeping them separate prevents premature promises and misleading reporting.

Greenhouse documents different offer flows depending on whether approvals are configured. Multiple approvers can be sequential or non-sequential. Its approved-offer hiring flow closes an opening when an authorized user marks the candidate hired. [ROP05/06.] These product actions do not establish legal acceptance, fulfillment of conditions or a person's actual start date. The operating sequence below requires the employer's authorized records.

### Application and decision guidance

Prepare terms from the approved role, compensation boundaries and appropriate employment/engagement process. Identify the approver and the exact offer version. If terms change, determine whether the revision needs approval under policy and current configuration. Do not infer that a previous approval covers a materially different offer. A pending offer should have a named owner, missing authorization and next follow-up, not merely an aging status.

Record when the approved offer was delivered, what version the candidate received, the response and any conditions requiring resolution. An informal expression of interest is not a substitute for the relevant acceptance record. Contract interpretation belongs to qualified employment/engagement owners. The knowledge can explain the process distinction without drafting or signing terms.

For a withdrawal, preserve what the candidate communicated, the relevant application and date. Ask a reason only where appropriate, make optional feedback genuinely optional, and distinguish a stated reason from recruiter speculation. Notify the responsible team through approved channels. A withdrawal from one application does not mean the person withdrew from every application or authorized deletion of all their data.

Handoff should include the selected application, approved/accepted terms, agreed start information, outstanding conditions, responsible next owner and only the information needed for that step. Keep accommodation or medical details restricted to the appropriate process. Closing the opening does not automatically notify other applicants or close every active application. Greenhouse documentation shows that active candidate records may remain after a job closes. [ATS17.] Reconcile each remaining application's next action and communication rather than claiming closure completed everything.

### Worked example and completed record

The selected candidate accepts offer O-01 after approval. Another candidate remains in an interview stage when the opening closes. The recruiter hands off the hire and separately reviews the remaining application's status and notification.

**Record:** opening OP-02, application A-01, offer O-01-v1. Recommendation recorded September 12. Approval September 14. Delivered September 15. Acceptance September 18. Authorized ATS hired record September 19. HR operations handoff September 19, start date confirmed separately. Remaining application A-04: close/communicate through the approved process, no assumption that the job closure sent email. Decision: opening filled, handoff acknowledged, remaining communication reconciled. Limit: the ATS hired event is not proof of employment commencement.

### Essential, advanced and common mistakes

Essential practice is tracking the distinct events and offer version. Advanced practice reconciles pending approvals, failed delivery and unresolved handoffs with named owners. Common mistakes are equating an Offer stage with an approved offer, marking a candidate hired to improve a report, and using silence as acceptance or withdrawal. Unknowns are actual terms, approval configuration and legal conditions. Use workflow O.

## R7. Records, permissions and exceptions

An ATS record is a representation of an event or fact under specific permissions. When records disagree, investigate the event and data ownership before changing the display. A correction can affect an application, a person profile, an integration, a scheduled interview or a report differently.

Start by preserving the relevant identifiers, displayed values, dates and source of each assertion. Do not copy unrelated private information into an investigation record. Distinguish an absent value from one hidden by permissions or an integration that has not synchronized. Existing Chapters 2, 10 and 15 own the underlying record and LinkedIn integration mechanisms.

### Application and decision guidance

For duplicate review, establish identity using appropriate corroborating information. A potential-match flag is an investigation prompt, not proof. Greenhouse documents configured matching, permission requirements, primary-record conflict rules and irreversible merges. It also warns about integration identifier changes and scheduled-interview consequences. [ROP07.] Before any authorized merge, the responsible operator should assess identity, surviving values, separate application history and dependent systems. A merge requires explicit authorization and review by the responsible operator.

When values conflict, choose the authoritative source for the specific fact. A candidate correction may establish a new date, but the historical submitted file should remain identifiable as what was originally received. A profile edit may not update a submitted application or an employer record. A successful connector event may only show that one operation completed, not that every downstream record agrees. Record actual synchronization evidence and escalate unresolved mappings to the integration owner.

For permissions, identify which role needs which information and why. Do not broaden access merely to resolve a convenient comparison. A reviewer can assess capability without seeing medical information or unrelated compensation notes. EEOC's selected US guidance requires confidentiality under its covered circumstances. ICO's UK recruitment guidance landing page identifies sensitive-data scope and is marked under review/draft. [ROP11/12.] Neither supplies a global retention duration. Route legal access, deletion, retention and cross-border questions to current jurisdiction-specific policy and qualified owners.

If a candidate requests an adjustment, record the assessment arrangement and responsible contact, while restricting sensitive supporting detail. Tell evaluators what arrangement they must follow without assuming they need a diagnosis. When a correction could change fairness or eligibility, document the decision and apply the relevant policy consistently rather than quietly rewriting the scorecard.

### Worked example and completed record

A duplicate flag matches an email and LinkedIn URL, but one application contains an accepted offer and another is active for a different role. The integration owner has not confirmed which identifier survives. The recruiter does not merge immediately.

**Record:** persons P-01/P-01-DUP, applications A-01/A-OTHER, discrepancy X-01. Identity: provisionally same person, verified corroboration required. Proposed primary: not yet approved. Known impact: conflicting source/owner fields, possible integration ID change. Decision: hold merge, preserve both applications, request identity and integration review. Next owner: authorized administrator plus integration owner. Limit: the flag establishes potential duplication, not permission or safety of a merge.

### Essential, advanced and common mistakes

Essential practice is identifying the affected record and preserving its context. Advanced practice uses an explicit data-owner map, correction history and dependent-system readback. Common mistakes are merging names alone, treating person-level status as application status, assuming a current profile replaced a historical submission, and confusing internal labels with legal access restrictions. Unknowns are tenant mappings, access configuration and applicable privacy policy. Use workflow P.

## R8. Reporting and process quality

A report answers a defined question using selected records and timestamps. The metric name cannot establish the calculation. Decide whether the question concerns people, applications, openings, events or a cohort. Then identify who is included, what period is measured and what is missing.

Greenhouse's time-to-hire article explicitly distinguishes an essential report using created-offer date from a dashboard using hire date. Its evergreen guidance also discusses opening clocks, pauses and reopening while using overlapping terminology. [ROP08/09.] Preserve these differences. The connected case defines its own application-to-offer, application-to-acceptance and opening-to-hire calculations instead of presenting one as universal.

### Application and decision guidance

Use a metric contract: purpose, unit, cohort, cutoff, start event, end event, numerator/denominator where relevant, exclusions and missingness. A stage conversion count should specify applications that entered the starting stage and later reached the next stage by the cutoff. It is not the ratio of today's two stage populations. A slow conversion may reflect unfinished cases or a changed process rather than poor screening.

Elapsed-time metrics should name their events. Offer created, offer sent, accepted and ATS marked hired can occur on different dates. Report calendar versus business days and the timezone convention. For a reopened opening, show both the current-cycle clock and the original search history where useful. If subtracting a hold, specify the interval convention and do not subtract it twice. Do not silently reset the history to make performance look better.

Withdrawals belong in an intake-cohort conversion denominator if they were part of that cohort, with a separate withdrawal count. An assessed-only denominator can answer a different question, but label it. An application missing a start timestamp cannot support an elapsed-time calculation. Exclude it from that calculation with its missingness count rather than treating it as zero or inventing a date.

Source attribution reports describe recorded sources under a convention. They do not prove which channel caused a hire. A referral may follow an earlier direct visit, and merging records may change a surviving source field. [ATS23; ROP07.] Small source counts can show a difference in this dataset without establishing a stable channel advantage. Keep unknown attribution visible.

Use reports to identify a specific record or process investigation. If one stage is aging, determine whether the delay concerns scheduling, missing evaluations, approval or an unrecorded action. Counts alone do not justify changing criteria or making a causal claim about people. Review data quality and ownership before recommending a process change.

### Worked example and completed record

A report shows one hire from five raw records. Two raw records represent the same application. After documented identity/context review, the cohort has four applications, one of which withdrew. Three reached the case discussion and two reached debrief.

**Record:** report M-01, cutoff September 22, application cohort for requisition PD-AI-01, filled opening OP-02. Unique applications: 4, not 5. Screen-to-case: 3/4 = 75%. Case-to-debrief: 2/3 = 66.7%. Intake-to-hire: 1/4 = 25%. Withdrawal share: 1/4 = 25%. Decision: report these observed counts with pending states and no forecast. Limit: the small case illustrates calculation and cannot establish process effectiveness or future conversion. Exact event data and alternate clocks are in the connected case.

### Essential, advanced and common mistakes

Essential practice is defining the metric and recording missingness. Advanced practice keeps cohorts separate from event-period reports and checks sensitivity to reopened cycles or excluded records. Common mistakes are dividing unrelated snapshots, mixing applications and people, using offer creation as acceptance, excluding withdrawals without disclosure and interpreting a source label causally. Unknowns are the actual report implementation and unrecorded events. Use workflow Q.

## R9. AI-assisted assessment and automation

AI assistance adds an interpretation layer between evidence and a decision. First establish the task: extraction, search, criterion comparison, summarization, ranking or an automated action. These mechanisms have different risks and evidence requirements. A useful generated summary does not demonstrate that an eligibility rule or ranking model is appropriate.

Ashby's written release describes criterion-based assessment, explanations and reviewer control. The observed 2024 frames show editable criteria, per-criterion results and correction/action controls. [ATS04; DEMO02.] These establish documented or displayed features, not current entitlement, assessment accuracy or independent fairness. The recovered Workable tour illustrates conventional human-review records, not universal AI screening.

### Application and decision guidance

Inspect the configured criterion before the result. Ask whether it represents an actual work requirement, whether the supplied evidence can establish it, and whether the wording invites unsupported inference. A university list, famous employer or tool vocabulary may function as a proxy. A warning is a prompt for scrutiny, not certification of the criterion's legality or validity.

Read the cited material and distinguish extraction from interpretation. A generated rationale might correctly quote a multi-year result but infer a one-year threshold or personal ownership that the text does not establish. The sampled Ashby rationale requires such a check, but its correctness was not independently validated. Do not declare it erroneous merely because it uses qualifying language. Record what follows from the evidence, what is inferred and what remains unknown.

Where a reviewer can correct an assessment, distinguish the corrected criterion from advancement, rejection and notification. A human click does not guarantee meaningful oversight if the reviewer has not checked the evidence or lacks authority to change the outcome. The recommended process requires an evidence-linked correction and a separate candidate decision.

Independent research supports scrutiny without supplying a current vendor verdict. Raghavan and colleagues studied public vendor disclosures and expressly limited what they could conclude about model validity. Fabris and colleagues' survey discusses contextual fairness and why changes can invalidate earlier evaluations. [ROP14/15.] Neither evaluates this employer's Ashby deployment. Ask for a task-specific evaluation with relevant data, defined errors, comparison conditions and known limitations before adopting performance claims.

For authorized automation, identify the operator, permitted data, action scope, exception path, monitoring and stop conditions. Begin with reviewable output when consequences and evidence are uncertain. A prototype's apparent success on selected examples does not authorize unattended decisions. Preserve failures and overrides rather than measuring only agreement on easy cases. A small trial can reveal defects, not prove universal accuracy, fairness or compliance.

### Worked example and completed record

An AI assessment says a candidate meets production deployment because the résumé mentions an AI prototype. The actual requirement concerns design evaluation, with engineering deployment preferred. The reviewer checks both the claim and the requirement instead of replacing one unsupported assumption with another.

**Record:** AI review AI-01, application A-01, criterion v1. Input: prototype case. Supported: prototype/design evidence. Inference: production deployment. Missing: release ownership and operational responsibility. Correction recommendation: deployment remains unestablished, design criterion assessed separately. Candidate decision: continue the planned design interview because deployment is not essential under v1. Next step: obtain actual evidence if deployment becomes essential. Limit: no general product-accuracy conclusion and no automated action authorized.

### Essential, advanced and common mistakes

Essential practice checks the criterion, evidence and action separately. Advanced practice evaluates the complete human/system process and records error patterns, overrides and context changes. Common mistakes are calling a count a universal ATS score, treating citations as truth certification, assuming a bias warning proves fairness and counting human approval as meaningful review without examining it. Unknowns include tenant settings, actual model/data performance and legal applicability. Use workflows M/N/P/Q as appropriate.

## Maintenance and escalation

The decision distinctions, record separation and evidence reasoning are stable guidance. Product controls, permissions, tier names, report implementations, integrations, preview availability and legal requirements need current verification before operational reliance.

If a supporting explanation is missing, narrow the answer to available evidence and identify the consequential missing fact. A dated source does not establish the present account configuration. Refresh the relevant official reference before an exact operational step.
