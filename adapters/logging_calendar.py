from ports.calendar_port import CalendarPort # Import the same port implemented by both the wrapped adapter and this decorator.

class LoggingCalendarDecorator(CalendarPort): # Implement Decorator by preserving CalendarPort while wrapping another CalendarPort object.
    def __init__(self, wrapped_calendar: CalendarPort): # Receive the calendar object whose behavior should be extended without changing its source code.
        self.wrapped_calendar = wrapped_calendar # Store the wrapped CalendarPort so calls can be forwarded after additional behavior runs.

    def get_availability(self): # Keep exactly the same operation required by CalendarPort so the decorator remains substitutable for any calendar adapter.
        print("DECORATOR -> calendar call started") # Add cross-cutting logging before the wrapped tool invocation.
        try: # Protect the after-call log so success and failure can be reported consistently.
            availability = self.wrapped_calendar.get_availability() # Delegate the real availability work to the wrapped adapter instead of reimplementing provider behavior.
        except Exception: # Observe any failure while preserving the original exception type for the orchestrator to handle.
            print("DECORATOR -> calendar call failed") # Add a visible failure log without converting or swallowing the provider-independent exception.
            raise # Re-raise the original exception so existing application error handling continues to work unchanged.
        print(f"DECORATOR -> calendar call finished with {len(availability)} slots") # Add a success log after the wrapped tool returns its result.
        return availability # Return the unchanged availability data so decoration does not alter business semantics.