from ports.calendar_port import CalendarPort, CalendarUnavailableError

class FakeCalendarAdapter(CalendarPort):
    def __init__(self, should_fail=False):
        self.should_fail = should_fail

    def get_availability(self):
        print("FakeCalendarAdapter: get_availability() called")
        if self.should_fail:
            raise CalendarUnavailableError("Calendar service unavailable")
        return ["Monday 14:00-16:00", "Tuesday 10:00-12:00"]