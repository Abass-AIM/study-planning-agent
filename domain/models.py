from dataclasses import dataclass, field
from datetime import date

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