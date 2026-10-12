from domain.models import PlanItem, StudyPlan

class Planner:
    def create_plan(self, student, assignments, availability):
        ordered = sorted(assignments, key=lambda item: (item.priority, item.deadline))
        plan = StudyPlan(student=student)
        for index, assignment in enumerate(ordered):
            slot = availability[index % len(availability)]
            hours = min(assignment.estimated_hours, 2.0)
            plan.items.append(PlanItem(assignment=assignment, scheduled_slot=slot, planned_hours=hours))
        return plan