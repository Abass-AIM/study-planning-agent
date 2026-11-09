# Week 9 SOLID Review
## Refactoring context
Before Week 9, `run.py` directly created `FakeCalendarAdapter`. This was acceptable in a small composition root, but provider selection and call logging would become repetitive as integrations grew. The Week 9 refactoring adds `CalendarAdapterFactory` and `LoggingCalendarDecorator`. `StudyPlanningOrchestrator` remains unaware of concrete calendar classes[cite: 75].

## S - Single Responsibility Principle (SRP)
- **Meaning:** each component should have one focused reason to change[cite: 75].
- `agent/planner.py`: changes when scheduling rules change, not when providers are selected[cite: 75].
- `agent/orchestrator.py`: changes when the application workflow changes, not for provider-specific construction or logging[cite: 75].
- `factories/calendar_factory.py`: changes when provider-construction options change[cite: 75].
- `adapters/logging_calendar.py`: changes when calendar-call diagnostic logging changes[cite: 75].

## O - Open/Closed Principle (OCP)
- **Meaning:** add a new behavior without unnecessarily editing existing working implementations[cite: 75].
- `LoggingCalendarDecorator` wraps any `CalendarPort` instance and adds logging[cite: 75].
- `FakeCalendarAdapter` remains responsible only for returning availability or raising an error[cite: 75].

## L - Liskov Substitution Principle (LSP)
- **Meaning:** callers relying on a contract must continue to work with any valid implementation of that contract[cite: 76].
- `FakeCalendarAdapter` and `LoggingCalendarDecorator` both implement `CalendarPort.get_availability()` and preserve exception behavior[cite: 76].

## I - Interface Segregation Principle (ISP)
- **Meaning:** a client should not depend on operations it does not use[cite: 76].
- `ports/calendar_port.py` exposes only the narrow `get_availability()` operation needed by planning[cite: 76].

## D - Dependency Inversion Principle (DIP)
- **Meaning:** high-level policy should depend on abstractions, not provider details[cite: 76].
- `StudyPlanningOrchestrator` receives its calendar dependency through its constructor via the `CalendarPort` abstraction[cite: 76].