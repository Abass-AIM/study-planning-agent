import unittest # Use the standard-library testing framework.
from agent.planning_policy import PlanningPolicy # Test the new policy without SQLite or tool calls.

class PlanningPolicyUnitTests(unittest.TestCase): # Isolate the session-duration rule.
    def setUp(self): # Start each test with a fresh policy instance.
        self.policy = PlanningPolicy()

    def test_caps_long_assignment_at_two_hours(self): # A 3.5-hour task gets one 2-hour session.
        self.assertEqual(2.0, self.policy.session_hours(3.5))

    def test_preserves_short_assignment_estimate(self): # A shorter estimate is unchanged.
        self.assertEqual(1.5, self.policy.session_hours(1.5))

    def test_rejects_negative_estimated_hours(self): # Invalid negative input must be rejected.
        with self.assertRaisesRegex(ValueError, "Estimated hours must not be negative"):
            self.policy.session_hours(-1.0)

if __name__ == "__main__": # Support direct test execution.
    unittest.main()