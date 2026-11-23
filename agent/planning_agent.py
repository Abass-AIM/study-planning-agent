class PlanningAgent:  # Represent the specialist that starts a study-planning goal.
    def __init__(self, orchestrator):  # Accept the existing, tested workflow as a dependency.
        self.orchestrator = orchestrator  # Keep workflow logic in the orchestrator, not this wrapper.

    def execute(self, student, assignments):  # Delegate one goal and return the original StudyPlan.
        print(f"PLANNING AGENT -> goal received for {student.name}")  # Mark entry to this role.
        plan = self.orchestrator.generate_plan(student, assignments)  # Reuse Week 10 behavior.
        print(f"PLANNING AGENT -> returned {len(plan.items)} plan items")  # Report the result size.
        return plan  # Let the coordinator decide whether reflection may run.