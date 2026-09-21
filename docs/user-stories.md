# User Stories

## US-01 Generate a weekly study plan

As a student, I want a 7-day plan from my assignments, so that I can prioritise my work.

### Acceptance criteria

- **AC-01:** Given the student has entered three assignments with valid deadlines, when the student generates a weekly plan, then all three assignments appear in the 7-day plan.
- **AC-02:** Given two assignments have different deadlines, when the plan is generated, then the system shows a visible reason for the suggested ordering.
- **AC-03:** Given one assignment has no deadline, when the student requests a plan, then the agent asks for the missing deadline instead of inventing one.

**Related requirements:** FR-02, FR-04, NFR-03, AG-01

---

## US-02 Explain task prioritisation

As a student, I want to see why a task was scheduled early, so that I can judge whether the suggestion makes sense.

**Related requirements:** FR-04, AG-04

---

## US-03 Regenerate the study plan

As a student, I want to regenerate the plan after changing a deadline, so that the plan reflects current information.

**Related requirements:** FR-03

---

## US-04 Protect external integrations

As an IT administrator, I want external integrations to use minimum permissions, so that unnecessary account access is avoided.

**Related requirements:** NFR-02, AG-03