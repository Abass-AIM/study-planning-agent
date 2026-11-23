import io  # Capture ordinary application messages during testing.
import tempfile  # Create disposable filesystem locations for test databases.
import unittest  # Use the built-in testing framework.
from contextlib import redirect_stdout  # Keep trace output out of the test report.
from datetime import date  # Build deterministic assignment input.
from pathlib import Path  # Construct a portable temporary database path.
from adapters.fake_calendar import FakeCalendarAdapter  # Use the fake external service.
from adapters.logging_calendar import LoggingCalendarDecorator  # Preserve production logging.
from adapters.sqlite_database import connect, initialize_database  # Create and inspect SQLite.
from adapters.sqlite_memory import SQLiteMemoryStore  # Preserve real memory behavior.
from adapters.sqlite_repository import SQLiteStudyRepository  # Preserve real repository behavior.
from agent.coordinator import AgentCoordinator  # Test the new multi-agent coordinator.
from agent.orchestrator import StudyPlanningOrchestrator  # Reuse the production workflow.
from agent.planner import Planner  # Reuse the Week 10 planner.
from agent.planning_agent import PlanningAgent  # Reuse the new planning role.
from agent.planning_policy import PlanningPolicy  # Share the production session rule.
from agent.reflection_agent import ReflectionAgent  # Reuse the new review role.
from domain.models import Assignment, Student  # Build domain input.


class AgentCoordinationIntegrationTests(unittest.TestCase):  # Exercise the real integrated stack.
    def test_completed_plan_is_reflected_and_memory_records_acceptance(self):  # Verify persistence.
        with tempfile.TemporaryDirectory() as temp_directory:  # Isolate database side effects.
            database_path = Path(temp_directory) / "coordination.db"  # Choose disposable SQLite.
            initialize_database(database_path)  # Create the schema inside that database.
            policy = PlanningPolicy()  # Build one shared session-length policy.
            planner = Planner(policy=policy)  # Build the production planner.
            calendar = LoggingCalendarDecorator(FakeCalendarAdapter())  # Wrap a fake provider.
            memory = SQLiteMemoryStore(database_path)  # Use real persistent agent memory.
            repository = SQLiteStudyRepository(database_path)  # Use the real data repository.
            orchestrator = StudyPlanningOrchestrator(  # Compose the existing application workflow.
                planner=planner, calendar=calendar, memory=memory, repository=repository
            )  # Complete production-like orchestration.
            planning_agent = PlanningAgent(orchestrator)  # Add the planning specialist.
            reflection_agent = ReflectionAgent(policy)  # Add the reviewing specialist.
            coordinator = AgentCoordinator(planning_agent, reflection_agent, memory)  # Link roles.
            student = Student(1, "Coordination Student")  # Define the request owner.
            assignments = [  # Define a valid planning goal with one assignment.
                Assignment(801, "Agent Integration", date(2026, 11, 20), 1.5, 1)
            ]  # Complete the scenario input.
            capture = io.StringIO()  # Buffer the terminal trace.
            with redirect_stdout(capture):  # Capture without changing application behavior.
                plan = coordinator.run(student, assignments)  # Execute the real coordination path.
            connection = connect(database_path)  # Open the temporary database for assertions.
            try:
                reflection_events = connection.execute(  # Count persisted acceptance events.
                    "SELECT COUNT(*) FROM memory_events "
                    "WHERE message = 'Reflection accepted the generated study plan'"
                ).fetchone()[0]  # Extract the aggregate count.
            finally:
                connection.close()  # Release the database after inspection.
            self.assertEqual(1, len(plan.items))  # Require the planning goal to produce work.
            self.assertEqual(1, reflection_events)  # Require exactly one durable review verdict.
            self.assertIn("REFLECTION -> ACCEPTED", capture.getvalue())  # Require trace evidence.


if __name__ == "__main__":  # Allow focused debugging.
    unittest.main()  # Execute the integration test.