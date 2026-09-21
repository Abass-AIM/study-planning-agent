# Requirements

## Functional Requirements

- **FR-01:** The system shall allow a student to enter an assignment title, deadline, estimated effort and priority.
- **FR-02:** The system shall generate a 7-day study plan from the entered assignments.
- **FR-03:** The system shall allow the student to regenerate the plan after changing an assignment.
- **FR-04:** The system shall show the reason for the suggested order of tasks.

## Non-functional Requirements

- **NFR-01:** The generated plan shall be displayed within 10 seconds for up to 30 active assignments.
- **NFR-02:** The system shall not modify an external calendar without explicit user confirmation.
- **NFR-03:** The interface shall clearly distinguish user-provided facts from agent-generated suggestions.
- **NFR-04:** Failed external-service calls shall be reported without silently deleting task data.

## AI Agent Boundaries

- **AG-01:** The agent shall ask for clarification when an assignment deadline is missing.
- **AG-02:** The agent shall not invent a deadline or claim that an instructor approved a plan.
- **AG-03:** The agent may read permitted calendar availability but shall require confirmation before any calendar write.
- **AG-04:** The agent shall expose which input data influenced the generated plan.

## Traceability

| Need | Requirement | User story |
|---|---|---|
| Prioritise urgent work | FR-02 | US-01 |
| Understand agent reasoning | FR-04 / AG-04 | US-02 |
| Keep plan current | FR-03 | US-03 |
| Limit external permissions | NFR-02 / AG-03 | US-04 |