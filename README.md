# Healthcare Operations Habit Audit™

I built the Healthcare Operations Habit Audit as a student-developed healthcare operations project to study a broader question than any single eligibility, authorization, or denial case: **what recurring day-to-day habits can make a workflow more reliable—or make the same problems keep coming back?**

As I work toward my Bachelor's of Science degree in Healthcare Administration at the University of Phoenix, I am learning that workflow problems are not always caused by one dramatic failure. Sometimes the risk builds through smaller patterns: information that is not verified consistently, documentation that is not ready for the next step, unclear handoffs, patients who are not sure what they need to do next, or recurring problems that are corrected case by case without being studied as a pattern.

From the patient side, those internal habits can become very visible. They can mean another call, another request for information, a delayed authorization, a confusing bill, a rescheduled visit, or uncertainty about what happens next.

This project gives me a way to practice looking at those patterns across the workflow instead of treating every problem as an isolated event.

## Live Streamlit App

[Open the Healthcare Operations Habit Audit](https://healthcare-operations-habit-audit-emd56fbkjuufecaftwypwg.streamlit.app/)

## Why I Built This Project

I do not have formal healthcare operations employment experience yet, so I use simulated projects to turn coursework and independent study into visible practice.

The other projects in my portfolio follow specific workflow problems:

- **EVIS** looks at eligibility and intake risk.
- **PARCS** looks at prior authorization workflow risk, ownership, and escalation.
- **DPIS** looks at upstream denial-prevention and claim-readiness risk.
- **SBI** asks where the first cross-workflow control loss occurred.

The Habit Audit sits across all of them. It asks a different question:

> **What repeated operational habits may be making workflow risk more likely?**

I built it to practice turning that question into a simple review structure that can be discussed, scored, compared, and connected to improvement ideas.

## What the Audit Reviews

The project uses six simulated review categories:

| Category | What I am reviewing |
|---|---|
| Documentation Accuracy | Whether the information needed for the next step is clear and complete |
| Data Integrity | Whether demographic, insurance, and workflow information is current and internally consistent |
| Patient-Centered Workflow | Whether the patient has clear information about what is needed and what happens next |
| Compliance Readiness | Whether authorization, referral, documentation, and payer requirements appear to have been reviewed before service |
| Cross-Functional Communication | Whether status, ownership, next steps, and unresolved issues are carried across handoffs |
| Continuous Improvement | Whether repeated workflow problems are being tracked and reviewed instead of corrected one case at a time |

**Important boundary:** “Compliance Readiness” is an educational workflow-review label in this project. It is not a legal, regulatory, accreditation, or formal compliance determination.

## How the Scoring Works

Each category is scored from **1 to 5**:

| Score | Educational interpretation |
|---:|---|
| 1 | Critical modeled weakness |
| 2 | High modeled workflow risk |
| 3 | Inconsistent / moderate modeled risk |
| 4 | Mostly reliable modeled practice |
| 5 | Strong modeled practice |

The Streamlit app then calculates several **student-designed indicators** from those inputs.

For example, the default demo scores are:

| Category | Default Demo Score |
|---|---:|
| Documentation Accuracy | 3 |
| Data Integrity | 2 |
| Patient-Centered Workflow | 3 |
| Compliance Readiness | 2 |
| Cross-Functional Communication | 2 |
| Continuous Improvement | 3 |

With those defaults:

- Average habit score = **2.5 / 5**
- Modeled workflow practice score = **50 / 100**
- Denial-prevention practice indicator = **2.25 / 5**
- Patient-centered workflow indicator = **2.5 / 5**

These are **not validated healthcare measures or benchmarks**. They are simple educational calculations I created so I could practice turning qualitative workflow observations into a consistent review structure.

## What I Am Practicing

This project helps me practice:

- looking for repeated workflow patterns rather than only one-time errors,
- connecting documentation and data quality to downstream work,
- thinking about patient communication as part of operational reliability,
- reviewing handoffs for ownership and next-step clarity,
- identifying areas that may deserve closer human review,
- creating a simple scoring model,
- translating findings into an improvement plan,
- presenting simulated workflow information in a dashboard,
- and separating educational modeling from real-world performance claims.

## The Patient-to-Professional Connection

One reason this project matters to me is that patients usually experience the **result** of an operational habit, not the internal process name.

A patient may never know that the underlying issue involved data integrity, handoff ownership, documentation readiness, or an unresolved authorization requirement. They may only know that they have to call again, send information again, wait longer, or figure out why the next step did not happen when they expected it to.

That is why I include **Patient-Centered Workflow** as one of the six categories. I want my operational thinking to stay connected to what the workflow feels like from the other side.

## 30-Day Improvement Exercise

The app includes a simulated 30-day improvement plan:

| Timeline | Practice Action | Why I included it |
|---|---|---|
| Week 1 | Review the highest-risk categories | Focus attention before trying to change everything at once |
| Week 1 | Build a front-end checklist | Practice standardizing documentation and verification |
| Week 2 | Map handoffs | Look for unclear status, ownership, and next steps |
| Week 2 | Draft a patient instruction script | Practice clearer patient-facing communication |
| Week 3 | Track repeated errors | Look for patterns instead of isolated corrections |
| Week 4 | Review the findings again | Practice continuous-improvement thinking |

This is a learning exercise, not an implementation plan for a real healthcare organization.

## How It Fits in My Portfolio

The Habit Audit is the final cross-cutting project in the workflow path I use across my portfolio:

**EVIS → PARCS → DPIS → SBI → Habit Audit**

The first projects follow particular workflow problems. The Habit Audit steps back and asks whether repeated behaviors in documentation, data integrity, communication, patient preparation, requirement review, and follow-through could be creating the conditions for those problems to recur.

## What This Project Is — and Is Not

This is a **student-developed educational portfolio project**.

- All scenarios, scores, findings, and recommendations are simulated.
- No protected health information (PHI) is used.
- No real patient, payer, employer, claim, EHR, or healthcare organization data is used.
- The scoring model has not been clinically, operationally, legally, or statistically validated.
- The project does not represent a formal compliance assessment, audit, accreditation review, or quality certification.
- It does not represent formal healthcare employment experience.
- It has not been implemented in a healthcare organization.
- I do not claim that it has reduced denials, improved reimbursement, reduced staff workload, improved compliance, or changed patient outcomes.

I want the project to show how I am learning to organize a workflow problem, ask better questions, create a simple review method, and communicate improvement opportunities without overstating what a student project can prove.

## Career Direction

I am building toward entry-level remote work in patient access and healthcare operations, including eligibility verification, prior authorization support, revenue cycle support, denial prevention, documentation workflow support, and related operational roles.

Longer term, I am interested in healthcare operations analysis, workflow improvement, health information systems, analytics, and responsible AI governance in healthcare.

## Connect

- [Healthcare Operations Portfolio Hub](https://healthcare-operations-portfolio-hub.vercel.app/)
- [LinkedIn](https://www.linkedin.com/in/kori-pickle)
- [GitHub profile](https://github.com/koripickle1101-TN)

Created by Kori Pickle. Student-developed portfolio project. Simulated data only. No PHI.