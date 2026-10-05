from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from pathlib import Path
import json
import sys

MEMORY_FILE = Path("week4_memory.json")

@dataclass
class Student:
    student_id: int
    name: str

@dataclass
class Assignment:
    assignment_id: int
    title: str
    deadline: date
    estimated_hours: float
    priority: int

@dataclass
class PlanItem:
    assignment: Assignment
    scheduled_slot: str
    planned_hours: float

@dataclass
class StudyPlan:
    student: Student
    items: list[PlanItem] = field(default_factory=list)

class AgentState(Enum):
    IDLE = "Idle"
    OBSERVING = "Observing"
    WAITING_FOR_INPUT = "WaitingForInput"
    CALLING_TOOL = "CallingCalendarTool"
    PLANNING = "Planning"
    COMPLETED = "Completed"
    FAILED = "Failed"

class CalendarToolError(Exception):
    pass

class CalendarTool:
    def __init__(self, should_fail=False):
        self.should_fail = should_fail

    def get_availability(self):
        print("CalendarTool: get_availability() called")
        if self.should_fail:
            raise CalendarToolError("Calendar service unavailable")
        return ["Monday 14:00-16:00", "Tuesday 10:00-12:00"]

class JsonMemory:
    def load(self):
        if not MEMORY_FILE.exists():
            return []
        return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))

    def append(self, event):
        events = self.load()
        events.append(event)
        MEMORY_FILE.write_text(json.dumps(events, indent=2), encoding="utf-8")

class StudyPlanningAgent:
    def __init__(self, calendar_tool, memory):
        self.calendar_tool = calendar_tool
        self.memory = memory
        self.state = AgentState.IDLE

    def move_to(self, new_state):
        self.state = new_state
        print(f"STATE -> {self.state.value}")
        self.memory.append(f"State: {self.state.value}")

    def generate_plan(self, student, assignments):
        print(f"REQUEST -> Generate weekly plan for {student.name}")
        self.move_to(AgentState.OBSERVING)

        if not assignments:
            self.move_to(AgentState.WAITING_FOR_INPUT)
            print("RESULT -> Please enter at least one assignment.")
            return StudyPlan(student=student)

        self.move_to(AgentState.CALLING_TOOL)
        try:
            availability = self.calendar_tool.get_availability()
            self.memory.append("Tool result: calendar availability received")
        except CalendarToolError as error:
            self.move_to(AgentState.FAILED)
            print(f"RESULT -> Could not generate plan: {error}")
            return StudyPlan(student=student)

        self.move_to(AgentState.PLANNING)
        ordered = sorted(assignments, key=lambda item: (item.priority, item.deadline))
        plan = StudyPlan(student=student)

        for index, assignment in enumerate(ordered):
            slot = availability[index % len(availability)]
            hours = min(assignment.estimated_hours, 2.0)
            plan.items.append(PlanItem(assignment=assignment, scheduled_slot=slot, planned_hours=hours))

        self.move_to(AgentState.COMPLETED)
        print("RESULT -> Study plan generated")
        return plan

def build_demo_input():
    student = Student(student_id=1, name="Alex Student")
    assignments = [
        Assignment(assignment_id=101, title="UML Behavioral Models", deadline=date(2026, 9, 27), estimated_hours=3.0, priority=1),
        Assignment(assignment_id=102, title="Python Agent Workflow", deadline=date(2026, 9, 29), estimated_hours=4.0, priority=2),
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
    calendar_tool = CalendarTool(should_fail=calendar_fails)
    memory = JsonMemory()
    agent = StudyPlanningAgent(calendar_tool=calendar_tool, memory=memory)

    plan = agent.generate_plan(student=student, assignments=selected_assignments)
    print_plan(plan)