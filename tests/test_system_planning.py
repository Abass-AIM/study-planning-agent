import io # Capture the application's terminal trace.
import tempfile # Keep test databases out of the student's working files.
import unittest # Use built-in test assertions.
from contextlib import redirect_stdout # Capture the normal workflow logs.
from datetime import date # Supply a realistic assignment deadline.
from pathlib import Path # Identify an isolated SQLite database path.
from adapters.fake_calendar import FakeCalendarAdapter # Use the real deterministic adapter.
from adapters.logging_calendar import LoggingCalendarDecorator # Use the real Decorator.
from adapters.sqlite_database import connect, initialize_database # Create/inspect the schema.
from adapters.sqlite_memory import SQLiteMemoryStore # Use persistent agent memory.
from adapters.sqlite_repository import SQLiteStudyRepository # Persist plans and traces.
from agent.orchestrator import StudyPlanningOrchestrator # Execute the complete use case.
from agent.planner import Planner # Use the actual planner.
from agent.planning_policy import PlanningPolicy # Use the tested duration rule.
from domain.models import Assignment, Student # Construct domain input objects.

class StudyPlanningSystemTests(unittest.TestCase): # Verify the full application with SQLite.
    def test_successful_plan_is_generated_and_persisted(self):
        with tempfile.TemporaryDirectory() as temporary_folder: # Dispose of test state automatically.
            database = Path(temporary_folder) / "system-test.db"
            initialize_database(database) # Create the real schema in the temporary database.
            student = Student(student_id=1, name="System Test Student")
            assignments = [Assignment( # Use a task longer than the maximum study session.
                assignment_id=501, title="Testing", deadline=date(2026, 11, 10),
                estimated_hours=3.0, priority=1
            )]
            calendar = LoggingCalendarDecorator(FakeCalendarAdapter())
            repository = SQLiteStudyRepository(database)
            memory = SQLiteMemoryStore(database)
            planner = Planner(policy=PlanningPolicy())
            application = StudyPlanningOrchestrator(planner, calendar, memory, repository)
            with redirect_stdout(io.StringIO()): # Keep normal messages out of test output.
                plan = application.generate_plan(student=student, assignments=assignments)
            self.assertEqual(1, len(plan.items)) # One assignment creates one item.
            self.assertEqual(2.0, plan.items[0].planned_hours) # The policy is active.
            connection = connect(database)
            try:
                status = connection.execute( # Read persisted request state.
                    "SELECT status FROM planning_requests ORDER BY request_id DESC LIMIT 1"
                ).fetchone()[0]
                plans = connection.execute("SELECT COUNT(*) FROM study_plans").fetchone()[0]
                calls = connection.execute( # Check successful calendar traces.
                    "SELECT COUNT(*) FROM tool_calls WHERE status = 'SUCCESS'"
                ).fetchone()[0]
            finally:
                connection.close()
            self.assertEqual("Completed", status)
            self.assertEqual(1, plans)
            self.assertEqual(1, calls)

if __name__ == "__main__":
    unittest.main()