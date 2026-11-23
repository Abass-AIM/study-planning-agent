import unittest  # Use Python's standard unit-testing library.
from datetime import date  # Make domain assignment deadlines deterministic.
from agent.planning_policy import PlanningPolicy  # Reuse the Week 10 session rule.
from agent.reflection_agent import ReflectionAgent  # Test the Week 11 review component.
from domain.models import Assignment, PlanItem, Student, StudyPlan  # Build test input objects.


class ReflectionAgentUnitTests(unittest.TestCase):  # Test reflection without SQLite or a calendar.
    def setUp(self):  # Prepare fresh domain objects for each independent test.
        self.student = Student(1, "Reflection Student")  # Define the owner of each plan.
        self.first = Assignment(701, "Reflection", date(2026, 11, 17), 2.0, 1)  # First goal.
        self.second = Assignment(702, "Coordination", date(2026, 11, 19), 1.5, 2)  # Second goal.
        self.assignments = [self.first, self.second]  # Collect the expected work items.
        self.reviewer = ReflectionAgent(PlanningPolicy())  # Build the policy-aware reviewer.

    def test_accepts_complete_policy_compliant_plan(self):  # Check the successful review path.
        plan = StudyPlan(self.student)  # Create a candidate plan for this student.
        plan.items.append(PlanItem(self.first, "Monday 14:00-16:00", 2.0))  # Valid first item.
        plan.items.append(PlanItem(self.second, "Tuesday 10:00-12:00", 1.5))  # Valid second item.
        result = self.reviewer.review(self.assignments, plan)  # Review the completed plan.
        self.assertTrue(result.accepted)  # Require acceptance of valid input.
        self.assertEqual([], result.issues)  # Require no hidden validation errors.

    def test_rejects_missing_assignment(self):  # Check that plan coverage must be complete.
        plan = StudyPlan(self.student)  # Create an incomplete candidate plan.
        plan.items.append(PlanItem(self.first, "Monday 14:00-16:00", 2.0))  # Omit ID 702.
        result = self.reviewer.review(self.assignments, plan)  # Inspect incomplete coverage.
        self.assertFalse(result.accepted)  # Do not accept missing work.
        self.assertIn("missing assignments [702]", result.issues)  # Identify the missing ID.

    def test_rejects_session_over_two_hours(self):  # Check the independent duration rule.
        plan = StudyPlan(self.student)  # Create a candidate that covers both assignments.
        plan.items.append(PlanItem(self.first, "Monday 14:00-16:00", 3.0))  # Violate policy.
        plan.items.append(PlanItem(self.second, "Tuesday 10:00-12:00", 1.5))  # Valid item.
        result = self.reviewer.review(self.assignments, plan)  # Inspect policy compliance.
        self.assertFalse(result.accepted)  # Reject the violation.
        self.assertIn("one or more sessions violate the planning policy", result.issues)  # Explain.


if __name__ == "__main__":  # Allow focused manual execution.
    unittest.main()  # Execute the reflection unit tests.