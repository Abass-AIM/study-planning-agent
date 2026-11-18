import io # Capture printed Factory/Decorator messages in memory.
import unittest # Use built-in test discovery.
from contextlib import redirect_stdout # Redirect prints within a single test.
from adapters.logging_calendar import LoggingCalendarDecorator # Real Decorator from Week 9.
from factories.calendar_factory import CalendarAdapterFactory # Real Factory from Week 9.
from ports.calendar_port import CalendarUnavailableError # Port-level failure contract.

class CalendarIntegrationTests(unittest.TestCase): # Check cooperation across components.
    def test_factory_and_decorator_return_calendar_slots(self): # The wrapped tool still works.
        output = io.StringIO()
        with redirect_stdout(output):
            base = CalendarAdapterFactory.create("fake", should_fail=False)
            calendar = LoggingCalendarDecorator(base)
            availability = calendar.get_availability()
        self.assertEqual(["Monday 14:00-16:00", "Tuesday 10:00-12:00"], availability)
        self.assertIn("FACTORY -> created FakeCalendarAdapter", output.getvalue())
        self.assertIn("DECORATOR -> calendar call finished with 2 slots", output.getvalue())

    def test_decorator_preserves_calendar_failure(self): # Logging must not hide a tool outage.
        output = io.StringIO()
        with redirect_stdout(output):
            base = CalendarAdapterFactory.create("fake", should_fail=True)
            calendar = LoggingCalendarDecorator(base)
            with self.assertRaises(CalendarUnavailableError):
                calendar.get_availability()
        self.assertIn("DECORATOR -> calendar call failed", output.getvalue())

if __name__ == "__main__":
    unittest.main()