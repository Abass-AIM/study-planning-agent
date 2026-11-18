import io # Suppress normal application output during automated assertions.
import tempfile # Give each acceptance scenario an independent test database.
import unittest # Use built-in assertions and discovery.
from contextlib import redirect_stdout # Capture the normal application trace.
from datetime import date # Create deterministic assignment deadlines.
from pathlib import Path # Build temporary SQLite paths.
from adapters.fake_calendar import FakeCalendarAdapter # Deterministic tool provider.
from adapters.logging_calendar import LoggingCalendarDecorator # Week 9 Decorator.
from adapters.sqlite_database import connect, initialize_database # Database access.
from adapters.sqlite_memory import SQLiteMemoryStore # Persistent memory component.
from adapters.sqlite_repository import SQLiteStudyRepository # Persistent task and plan state.
from agent.orchestrator import StudyPlanningOrchestrator # The complete agent workflow.
from agent.planner import Planner # Planning logic.
from agent.planning_policy import PlanningPolicy # Two-hour duration policy.
from domain.models import Assignment, Student # Domain input objects.

class AcceptanceWorkflowTests(unittest.TestCase): # Express user-visible Given/When/Then.
    def build_application(self, database, fail=False): # Construct one isolated real application.
        initialize_database(database) # Given an empty initialized database.
        calendar = LoggingCalendarDecorator(FakeCalendarAdapter(should_fail=fail))
        return StudyPlanningOrchestrator( # Connect the real tested components.
            planner=Planner(policy=PlanningPolicy()), calendar=calendar,
            memory=SQLiteMemoryStore(database), repository=SQLiteStudyRepository(database)
        )

    def test_given_valid_assignment_when_plan_requested_then_plan_completes(self):
        with tempfile.TemporaryDirectory() as folder:
            database = Path(folder) / "success.db"
            application = self.build_application(database)
            student = Student(student_id=1, name="Acceptance Student")
            assignments = [Assignment(601, "Acceptance Testing", date(2026, 11, 11), 1.5, 1)]
            with redirect_stdout(io.StringIO()):
                plan = application.generate_plan(student, assignments) # When a plan is requested.
            self.assertEqual(1, len(plan.items)) # Then the plan is not empty.
            self.assertEqual(1.5, plan.items[0].planned_hours) # Short estimates stay unchanged.
            connection = connect(database)
            try:
                state = connection.execute( # Also require a persisted completed state.
                    "SELECT status FROM planning_requests ORDER BY request_id DESC LIMIT 1"
                ).fetchone()[0]
            finally:
                connection.close()
            self.assertEqual("Completed", state)

    def test_given_no_assignments_when_plan_requested_then_agent_waits_for_input(self):
        with tempfile.TemporaryDirectory() as folder:
            database = Path(folder) / "missing.db"
            application = self.build_application(database)
            student = Student(student_id=1, name="Acceptance Student")
            with redirect_stdout(io.StringIO()):
                plan = application.generate_plan(student, []) # Given no assignments.
            connection = connect(database)
            try:
                state = connection.execute( # Then the request waits for input.
                    "SELECT status FROM planning_requests ORDER BY request_id DESC LIMIT 1"
                ).fetchone()[0]
                calls = connection.execute("SELECT COUNT(*) FROM tool_calls").fetchone()[0]
            finally:
                connection.close()
            self.assertEqual(0, len(plan.items)) # No fabricated plan.
            self.assertEqual("WaitingForInput", state)
            self.assertEqual(0, calls) # The calendar tool was never called.

    def test_given_calendar_outage_when_plan_requested_then_failure_is_controlled(self):
        with tempfile.TemporaryDirectory() as folder:
            database = Path(folder) / "failure.db"
            application = self.build_application(database, fail=True)
            student = Student(student_id=1, name="Acceptance Student")
            assignments = [Assignment(602, "Failure Handling", date(2026, 11, 12), 2.0, 1)]
            with redirect_stdout(io.StringIO()):
                plan = application.generate_plan(student, assignments) # A tool outage occurs.
            connection = connect(database)
            try:
                state = connection.execute( # The task records Failed.
                    "SELECT status FROM planning_requests ORDER BY request_id DESC LIMIT 1"
                ).fetchone()[0]
                failed = connection.execute( # The failed tool call is traceable.
                    "SELECT COUNT(*) FROM tool_calls WHERE status = 'FAILED'"
                ).fetchone()[0]
            finally:
                connection.close()
            self.assertEqual(0, len(plan.items))
            self.assertEqual("Failed", state)
            self.assertEqual(1, failed)

if __name__ == "__main__":
    unittest.main()