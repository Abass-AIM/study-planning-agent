from datetime import date  # Give the sample assignments real dates.
from agent.planning_policy import PlanningPolicy  # Reuse the tested session-length rule.
from agent.reflection_agent import ReflectionAgent  # Use the real Week 11 review component.
from domain.models import Assignment, PlanItem, Student, StudyPlan  # Reuse domain objects.


def main():  # Demonstrate a rejection without modifying the normal database.
    student = Student(student_id=1, name="Alex Student")  # Create the familiar student.
    assignments = [  # Define two items that a valid plan must cover.
        Assignment(201, "Agent Design Patterns", date(2026, 11, 17), 2.0, 1),  # First item.
        Assignment(202, "Multi-Agent Coordination", date(2026, 11, 19), 2.0, 2),  # Second item.
    ]  # Complete the goal input.
    flawed_plan = StudyPlan(student=student)  # Start an intentionally invalid proposal.
    flawed_plan.items.append(  # Add only one item with an excessive session duration.
        PlanItem(assignments[0], "Monday 14:00-16:00", 3.0)  # Break coverage and policy.
    )  # Complete the invalid plan item.
    reviewer = ReflectionAgent(PlanningPolicy())  # Construct the real reviewer.
    result = reviewer.review(assignments, flawed_plan)  # Inspect the invalid proposal.
    for check in result.checks:  # Show checks that still passed.
        print(f"REFLECTION CHECK -> {check}")  # Print one successful check.
    for issue in result.issues:  # Show each problem that was found.
        print(f"REFLECTION ISSUE -> {issue}")  # Print one rejection reason.
    print("REFLECTION -> ACCEPTED" if result.accepted else "REFLECTION -> REJECTED")  # Verdict.


if __name__ == "__main__":  # Only run the demo when invoked as a module or script.
    main()  # Execute the deterministic faulty-plan demonstration.