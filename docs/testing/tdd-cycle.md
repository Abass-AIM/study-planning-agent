# Week 10 - Red, Green, Refactor
## Problem
Before Week 10, `agent/planner.py` directly calculated `min(assignment.estimated_hours, 2.0)`. The two-hour rule was hidden inside a larger planning algorithm[cite: 80].

## RED - specify behavior before implementation
1. Create `tests/__init__.py` and `tests/test_planning_policy.py`[cite: 80].
2. Include three test cases: 3.5 -> 2.0; 1.5 -> 1.5; -1.0 -> `ValueError`[cite: 80].

## GREEN - smallest correct implementation
Create `agent/planning_policy.py` with class `PlanningPolicy`, constant `MAX_SESSION_HOURS = 2.0`, a negative-value guard, and a capped result[cite: 80, 81].

## REFACTOR - move responsibility without changing observable results
Update `agent/planner.py` to accept an injected `policy` and call `self.policy.session_hours(...)`. Update `run.py` to create and inject the policy.