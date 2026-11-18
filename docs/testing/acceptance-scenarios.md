# Week 10 - Acceptance Scenarios
## AC-01 - Valid assignments
**Given** a student with a valid assignment and a working calendar adapter, **When** the student requests a study plan, **Then** the request reaches `Completed`, a nonempty plan is returned, and the shorter 1.5-hour estimate is preserved[cite: 81].

## AC-02 - Missing assignments
**Given** a student supplies no assignments, **When** the student requests a study plan, **Then** the agent enters `WaitingForInput`, returns no plan items, and does not call the calendar tool[cite: 81].

## AC-03 - Calendar unavailable
**Given** valid input and an unavailable calendar adapter, **When** the student requests a study plan, **Then** the agent enters `Failed`, returns no misleading plan, and persists one failed tool-call trace[cite: 81].