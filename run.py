from datetime import date  # Import date so deterministic demonstration assignments contain real deadlines. 

from pathlib import Path  # Import Path so the runtime database file can be created and reset safely. 

import sys  # Import sys so command-line flags can select success, missing-input, and failure scenarios. 

from domain.models import Student, Assignment  # Import stable domain input objects. 

from agent.planner import Planner  # Import the cohesive planning component. 

from agent.orchestrator import StudyPlanningOrchestrator  # Import the application orchestrator that coordinates the use case. 

from adapters.logging_calendar import LoggingCalendarDecorator  # Import the Decorator that adds logging around any CalendarPort implementation.

from factories.calendar_factory import CalendarAdapterFactory  # Import the Factory that hides concrete calendar-adapter construction from the composition root.

from adapters.sqlite_database import initialize_database  # Import the schema-initialization helper for the SQLite database. 

from adapters.sqlite_memory import SQLiteMemoryStore  # Import the SQLite implementation of persistent agent memory. 

from adapters.sqlite_repository import SQLiteStudyRepository  # Import the SQLite repository for students, assignments, requests, tool logs, and plans. 

DATABASE_FILE = Path("study_planning_agent.db")  # Define the runtime SQLite database path used by the Week 6 demonstration. 

def reset_database():  # Define a helper that removes runtime database files for deterministic classroom demonstrations. 

    for suffix in ["", "-shm", "-wal"]:  # Consider the main SQLite file and possible sidecar files created by SQLite journaling modes. 

        candidate = Path(str(DATABASE_FILE) + suffix)  # Build the full path of one possible runtime database file. 

        if candidate.exists():  # Check whether that runtime file currently exists. 

            candidate.unlink()  # Delete the old runtime file so the next demonstration starts with an empty database. 

def read_provider_name(): # Define a small configuration helper so provider selection stays separate from adapter creation.
    prefix = "--calendar-provider=" # Define the command-line prefix used to choose a calendar provider in the Week 9 demonstration.
    for argument in sys.argv[1:]: # Inspect every command-line argument except the Python script name.
        if argument.startswith(prefix): # Check whether this argument contains calendar-provider configuration.
            return argument[len(prefix):] # Return only the provider name after removing the configuration prefix.
    return "fake" # Use the deterministic fake provider when the caller does not select another provider explicitly.

def build_demo_input():  # Define deterministic domain input that can be compared with the Week 6 relational model. 

    student = Student(student_id=1, name="Alex Student")  # Create the same example student used throughout the semester project. 

    assignments = [  # Create the small deterministic assignment collection used by the laboratory.
        Assignment(assignment_id=101, title="SOLID Refactoring", deadline=date(2026, 11, 1), estimated_hours=3.0, priority=1),  # Create the higher-priority Week 9 assignment.
        Assignment(assignment_id=102, title="Design Patterns", deadline=date(2026, 11, 3), estimated_hours=4.0, priority=2)   # Create the second Week 9 assignment.
    ]  # Finish the deterministic assignment list.

    return student, assignments  # Return both deterministic input values to the composition root. 

def print_plan(plan):  # Define a presentation helper that displays generated plan items. 

    for item in plan.items:  # Iterate through every PlanItem returned by the application layer. 

        print(f"PLAN -> {item.scheduled_slot}: {item.assignment.title} ({item.planned_hours} h)")  # Print one readable summary line for each scheduled assignment. 

if __name__ == "__main__":  # Execute the following composition-root code only when run.py is started directly. 

    if "--reset-db" in sys.argv:  # Check whether the user requested a clean database for this run. 

        reset_database()  # Remove any earlier runtime database so generated identifiers start predictably. 

    initialize_database(DATABASE_FILE)  # Create all normalized relational tables if they do not already exist. 

    print(f"DATABASE -> schema ready at {DATABASE_FILE}")  # Confirm that the relational schema is ready before application work begins. 

    student, assignments = build_demo_input()  # Build the deterministic student and assignment objects. 

    no_assignments = "--no-assignments" in sys.argv  # Detect the scenario where the user supplies no assignments. 

    calendar_fails = "--calendar-fail" in sys.argv  # Detect the scenario where the external calendar tool fails. 

    selected_assignments = [] if no_assignments else assignments  # Select the appropriate assignment list for the requested scenario. 

    provider_name = read_provider_name() # Read provider configuration without importing or constructing a concrete adapter here.

    planner = Planner() # Construct the planning component whose single responsibility is scheduling assignments.

    try: # Protect composition because invalid provider configuration should produce a controlled message rather than a traceback.
        base_calendar = CalendarAdapterFactory.create(provider_name=provider_name, should_fail=calendar_fails) # Ask the Factory for a CalendarPort implementation instead of calling a concrete adapter constructor directly.
    except ValueError as error: # Handle unsupported provider configuration at the application boundary.
        print(f"CONFIGURATION -> {error}") # Explain the invalid configuration in one predictable terminal line.
        raise SystemExit(2) # Stop with a non-zero process code so scripts can detect that configuration failed.

    calendar = LoggingCalendarDecorator(base_calendar) # Wrap the selected CalendarPort with a Decorator that adds logging without changing provider code.

    memory = SQLiteMemoryStore(DATABASE_FILE)  # Construct persistent agent memory backed by the same relational database. 

    repository = SQLiteStudyRepository(DATABASE_FILE)  # Construct the relational repository used for business and trace data. 

    application = StudyPlanningOrchestrator(planner=planner, calendar=calendar, memory=memory, repository=repository)  # Inject all dependencies into the orchestrator in one visible composition root. 

    plan = application.generate_plan(student=student, assignments=selected_assignments)  # Execute the same planning goal through persistent Week 6 architecture. 

    print_plan(plan)  # Display any generated StudyPlan items after the use case completes.