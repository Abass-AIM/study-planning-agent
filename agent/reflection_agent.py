from dataclasses import dataclass, field  # Define small, inspectable review results.


@dataclass  # Automatically provide a constructor for the review record.
class ReflectionResult:  # Store the decision and its supporting evidence.
    accepted: bool  # True only when no reflection issues exist.
    checks: list[str] = field(default_factory=list)  # Successful checks for the trace.
    issues: list[str] = field(default_factory=list)  # Reasons for rejection.


class ReflectionAgent:  # Review a plan without generating or editing the plan itself.
    def __init__(self, planning_policy):  # Share the Week 10 business rule with planning.
        self.planning_policy = planning_policy  # Keep a testable policy dependency.

    def review(self, assignments, plan):  # Evaluate goal coverage, hours and slot collisions.
        checks = []  # Collect evidence for every successful validation.
        issues = []  # Collect every problem that should block acceptance.

        expected_ids = {a.assignment_id for a in assignments}  # IDs requested by the user.
        planned_ids = {item.assignment.assignment_id for item in plan.items}  # IDs planned.
        if planned_ids == expected_ids:  # Require exact coverage, not just matching counts.
            checks.append(f"assignment coverage {len(planned_ids)}/{len(expected_ids)}")  # Record coverage.
        else:  # Explain missing or unexpected items rather than returning only False.
            missing_ids = sorted(expected_ids - planned_ids)  # Find requested items omitted from the plan.
            unexpected_ids = sorted(planned_ids - expected_ids)  # Find unrequested items in the plan.
            if missing_ids:  # Only report missing IDs when there are some.
                issues.append(f"missing assignments {missing_ids}")  # Preserve the exact missing IDs.
            if unexpected_ids:  # Only report extra IDs when there are some.
                issues.append(f"unexpected assignments {unexpected_ids}")  # Preserve the exact extra IDs.

        session_limit_ok = all(  # Check every session using the shared Week 10 limit.
            0 <= item.planned_hours <= self.planning_policy.MAX_SESSION_HOURS  # Enforce range.
            for item in plan.items  # Apply the rule to all generated items.
        )  # Finish the aggregate hours validation.
        if session_limit_ok:  # Record success if no session violates the rule.
            checks.append(f"session limit <= {self.planning_policy.MAX_SESSION_HOURS} h")  # Add evidence.
        else:  # Explain why the proposed plan cannot be approved.
            issues.append("one or more sessions violate the planning policy")  # Keep rejection clear.

        slot_values = [item.scheduled_slot for item in plan.items]  # Collect selected slots.
        if len(slot_values) == len(set(slot_values)):  # Require unique slots in this demo.
            checks.append("calendar slots are unique")  # Record that collisions were absent.
        else:  # A repeated slot would create a scheduling conflict in this simple example.
            issues.append("duplicate calendar slot detected")  # Report the collision.

        accepted = len(issues) == 0  # Accept only when every enforced condition holds.
        return ReflectionResult(accepted=accepted, checks=checks, issues=issues)  # Return evidence.