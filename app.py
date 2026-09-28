from dataclasses import dataclass, field  # Import helpers that automatically create constructors and readable object representations.
from datetime import date  # Import date so assignment deadlines and planned study dates use a real date type.


@dataclass  # Tell Python to generate standard data-class behavior for Student.
class Student:  # Define the Student domain class that appears in the Week 3 class diagram.
    student_id: int  # Store the unique numeric identifier of the student.
    name: str  # Store the student's display name.
    email: str  # Store the student's email address.


@dataclass  # Tell Python to generate standard data-class behavior for Assignment.
class Assignment:  # Define a task that the student must complete.
    assignment_id: int  # Store the unique numeric identifier of the assignment.
    title: str  # Store the human-readable assignment title.
    deadline: date  # Store the assignment deadline.
    estimated_hours: float  # Store the estimated effort required to finish the assignment.
    priority: int  # Store a simple priority value where a lower number means higher priority in this demo.


@dataclass  # Tell Python to generate standard data-class behavior for PlanItem.
class PlanItem:  # Define one scheduled study item that belongs to a StudyPlan.
    plan_item_id: int  # Store the unique numeric identifier of this scheduled item.
    assignment: Assignment  # Reference the Assignment that this plan item schedules.
    scheduled_date: date  # Store the calendar date on which the work should be performed.
    planned_hours: float  # Store the number of study hours allocated to the assignment.
    reason: str  # Store a short explanation for why the item was scheduled at this point.


@dataclass  # Tell Python to generate standard data-class behavior for StudyPlan.
class StudyPlan:  # Define the aggregate object that groups planned study items for one student.
    plan_id: int  # Store the unique numeric identifier of the study plan.
    student: Student  # Reference the Student who owns this plan.
    start_date: date  # Store the first day covered by the study plan.
    end_date: date  # Store the final day covered by the study plan.
    items: list[PlanItem] = field(default_factory=list)  # Create a fresh PlanItem list for every StudyPlan object.

    def add_item(self, item: PlanItem):  # Define an operation that adds one scheduled item to the plan.
        self.items.append(item)  # Append the supplied PlanItem object to the plan's list.

    def total_hours(self):  # Define an operation that calculates the total planned study time.
        return sum(item.planned_hours for item in self.items)  # Add every PlanItem's planned_hours value and return the sum.


def build_demo_plan():  # Create a concrete object graph that corresponds to the Week 3 object diagram.
    student = Student(student_id=1, name="Alex Student", email="alex@example.com")  # Create the concrete student1 object.

    uml_assignment = Assignment(
        assignment_id=101,
        title="UML Structural Models",
        deadline=date(2026, 9, 20),
        estimated_hours=3.0,
        priority=1,
    )  # Create assignment101 from the object diagram.

    python_assignment = Assignment(
        assignment_id=102,
        title="Python Domain Model",
        deadline=date(2026, 9, 23),
        estimated_hours=4.0,
        priority=2,
    )  # Create assignment102 from the object diagram.

    plan = StudyPlan(
        plan_id=201,
        student=student,
        start_date=date(2026, 9, 14),
        end_date=date(2026, 9, 20),
    )  # Create plan201 for the same student and week shown in the object snapshot.

    first_item = PlanItem(
        plan_item_id=301,
        assignment=uml_assignment,
        scheduled_date=date(2026, 9, 15),
        planned_hours=2.0,
        reason="Earlier deadline and higher priority",
    )  # Create item301 linked to assignment101.

    second_item = PlanItem(
        plan_item_id=302,
        assignment=python_assignment,
        scheduled_date=date(2026, 9, 18),
        planned_hours=2.5,
        reason="Later deadline and lower priority",
    )  # Create item302 linked to assignment102.

    plan.add_item(first_item)  # Add the first concrete PlanItem to plan201.
    plan.add_item(second_item)  # Add the second concrete PlanItem to plan201.

    return plan  # Return the completed object graph to the caller.


def print_plan(plan: StudyPlan):  # Display the concrete object state so students can compare code with the diagrams.
    print(f"Study plan {plan.plan_id} for {plan.student.name}")  # Print the plan identifier and owning student's name.
    print(f"Period: {plan.start_date} to {plan.end_date}")  # Print the date range represented by the StudyPlan object.

    for item in plan.items:  # Iterate through every PlanItem contained by the plan.
        print(f"- {item.scheduled_date}: {item.assignment.title} -> {item.planned_hours} h")  # Print the scheduled date, assignment title, and allocated study time.
        print(f"  Reason: {item.reason}")  # Print the explanatory reason stored in the PlanItem.

    print(f"Total planned time: {plan.total_hours()} h")  # Print the total hours calculated by the StudyPlan operation.


if __name__ == "__main__":  # Run the following statements only when this file is executed directly.
    demo_plan = build_demo_plan()  # Build the exact concrete object graph described by the Week 3 object diagram.
    print_plan(demo_plan)  # Print the object graph so its structure and values can be inspected in the terminal.