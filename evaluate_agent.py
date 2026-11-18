import io # Capture agent logs so the evaluation table is easy to read.
import tempfile # Isolate each scenario in its own disposable SQLite database.
from contextlib import redirect_stdout # Hide detailed logs during aggregate reporting.
from dataclasses import dataclass # Store one scenario's results in a structured record.
from datetime import date # Create assignments with deterministic deadlines.
from pathlib import Path # Build portable SQLite paths.
from adapters.fake_calendar import FakeCalendarAdapter # Use the tested deterministic tool.
from adapters.logging_calendar import LoggingCalendarDecorator # Preserve the Week 9 tool boundary.
from adapters.sqlite_database import connect, initialize_database # Initialize and inspect traces.
from adapters.sqlite_memory import SQLiteMemoryStore # Use real persistent agent memory.
from adapters.sqlite_repository import SQLiteStudyRepository # Use the real relational repository.
from agent.orchestrator import StudyPlanningOrchestrator # Evaluate the actual agent workflow.
from agent.planner import Planner # Use the actual planner.
from agent.planning_policy import PlanningPolicy # Use the Week 10-tested policy.
from domain.models import Assignment, Student # Use the existing domain entities.

@dataclass # Collect the report's measurements in one readable object.
class EvaluationResult:
    name: str # Stable scenario identifier.
    task_success: bool # True only for a nonempty plan with Completed request state.
    behavior_correct: bool # True if state and tool trace match expectations.
    final_state: str # Persisted terminal request state.
    tool_status: str # SUCCESS, FAILED, or NOT_CALLED.
    error_category: str # none, missing_input, tool_failure, or unexpected.

def build_application(database, calendar_should_fail=False): # Compose the real system.
    initialize_database(database) # Start every scenario with an empty database.
    calendar = LoggingCalendarDecorator(FakeCalendarAdapter(should_fail=calendar_should_fail))
    return StudyPlanningOrchestrator( # Inject the production components.
        planner=Planner(policy=PlanningPolicy()), calendar=calendar,
        memory=SQLiteMemoryStore(database), repository=SQLiteStudyRepository(database)
    )

def evaluate_scenario(name, assignments, should_fail, expected_state, expected_tool):
    with tempfile.TemporaryDirectory() as folder: # Keep evaluation state isolated.
        database = Path(folder) / "evaluation.db"
        application = build_application(database, calendar_should_fail=should_fail)
        student = Student(student_id=1, name="Evaluation Student")
        with redirect_stdout(io.StringIO()): # Capture routine agent trace messages.
            plan = application.generate_plan(student=student, assignments=assignments)
        connection = connect(database)
        try:
            state = connection.execute( # Read the last persisted state.
                "SELECT status FROM planning_requests ORDER BY request_id DESC LIMIT 1"
            ).fetchone()[0]
            row = connection.execute( # Missing-input scenarios have no tool-call row.
                "SELECT status FROM tool_calls ORDER BY tool_call_id DESC LIMIT 1"
            ).fetchone()
        finally:
            connection.close()
        tool = row[0] if row is not None else "NOT_CALLED"
        success = len(plan.items) > 0 and state == "Completed"
        correct = state == expected_state and tool == expected_tool
        if success:
            error = "none"
        elif state == "WaitingForInput":
            error = "missing_input"
        elif state == "Failed" and tool == "FAILED":
            error = "tool_failure"
        else:
            error = "unexpected"
        return EvaluationResult(name, success, correct, state, tool, error)

def main(): # Run four controlled scenarios and report transparent metrics.
    standard = [Assignment(701, "Standard Planning", date(2026, 11, 15), 3.0, 1)]
    short = [Assignment(702, "Short Planning", date(2026, 11, 16), 1.0, 1)]
    outage = [Assignment(703, "Tool Failure", date(2026, 11, 17), 2.0, 1)]
    results = [
        evaluate_scenario("standard_success", standard, False, "Completed", "SUCCESS"),
        evaluate_scenario("short_success", short, False, "Completed", "SUCCESS"),
        evaluate_scenario("missing_input", [], False, "WaitingForInput", "NOT_CALLED"),
        evaluate_scenario("calendar_failure", outage, True, "Failed", "FAILED"),
    ]
    task_successes = sum(result.task_success for result in results)
    correct_behaviors = sum(result.behavior_correct for result in results)
    feasible_cases = results[:2] # These cases have input and a working calendar.
    reliable_successes = sum(result.task_success for result in feasible_cases)
    error_counts = {key: sum(r.error_category == key for r in results)
                    for key in ("missing_input", "tool_failure", "unexpected")}
    traces_correct = all(result.behavior_correct for result in results)

    print("AGENT EVALUATION REPORT")
    for result in results:
        print(f"SCENARIO -> {result.name}: task_success={result.task_success}, "
              f"behavior_correct={result.behavior_correct}, state={result.final_state}, "
              f"tool={result.tool_status}, error={result.error_category}")
    print(f"TASK SUCCESS RATE -> {task_successes}/{len(results)} = "
          f"{task_successes / len(results) * 100:.1f}%")
    print(f"CONTROLLED BEHAVIOR RATE -> {correct_behaviors}/{len(results)} = "
          f"{correct_behaviors / len(results) * 100:.1f}%")
    print(f"GOAL COMPLETION RELIABILITY -> {reliable_successes}/{len(feasible_cases)} = "
          f"{reliable_successes / len(feasible_cases) * 100:.1f}%")
    print("ERROR ANALYSIS -> "
          f"missing_input={error_counts['missing_input']}, "
          f"tool_failure={error_counts['tool_failure']}, "
          f"unexpected={error_counts['unexpected']}")
    label = "matched" if traces_correct else "DID NOT MATCH"
    print(f"TRACE INSPECTION -> final task states and tool-call outcomes {label} all four expected scenarios")

if __name__ == "__main__": # Do not run the evaluation during module import.
    main()