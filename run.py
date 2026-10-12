from datetime import date
import sys
from domain.models import Student, Assignment
from agent.planner import Planner
from agent.orchestrator import StudyPlanningOrchestrator
from adapters.fake_calendar import FakeCalendarAdapter
from adapters.json_memory import JsonMemoryStore

def build_demo_input():
    student = Student(student_id=1, name="Alex Student")
    assignments = [
        Assignment(assignment_id=101, title="Architecture Diagram", deadline=date(2026, 10, 4), estimated_hours=3.0, priority=1),
        Assignment(assignment_id=102, title="Python Refactoring", deadline=date(2026, 10, 6), estimated_hours=4.0, priority=2),
    ]
    return student, assignments

def print_plan(plan):
    for item in plan.items:
        print(f"PLAN -> {item.scheduled_slot}: {item.assignment.title} ({item.planned_hours} h)")

if __name__ == "__main__":
    student, assignments = build_demo_input()
    calendar_fails = "--calendar-fail" in sys.argv
    no_assignments = "--no-assignments" in sys.argv
    selected_assignments = [] if no_assignments else assignments

    planner = Planner()
    calendar = FakeCalendarAdapter(should_fail=calendar_fails)
    memory = JsonMemoryStore()
    application = StudyPlanningOrchestrator(planner=planner, calendar=calendar, memory=memory)

    plan = application.generate_plan(student=student, assignments=selected_assignments)
    print_plan(plan)