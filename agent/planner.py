from agent.planning_policy import PlanningPolicy # Import the independently tested business rule.
from domain.models import PlanItem, StudyPlan # Reuse the existing Week 3 domain entities.

class Planner: # Convert assignments and calendar slots into a study plan.
    def __init__(self, policy=None): # Allow injection of a different policy for testing.
        self.policy = policy if policy is not None else PlanningPolicy() # Use the default policy.

    def create_plan(self, student, assignments, availability): # Build a deterministic plan.
        ordered = sorted(assignments, key=lambda item: (item.priority, item.deadline)) # Set priority order.
        plan = StudyPlan(student=student) # Start with an empty plan for the supplied student.
        for index, assignment in enumerate(ordered): # Schedule each input assignment.
            slot = availability[index % len(availability)] # Select one returned calendar slot.
            hours = self.policy.session_hours(assignment.estimated_hours) # Apply the tested policy.
            plan.items.append(PlanItem( # Add one scheduled item to the plan.
                assignment=assignment, scheduled_slot=slot, planned_hours=hours
            ))
        return plan # Return the generated aggregate to the orchestrator.