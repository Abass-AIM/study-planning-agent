# Week 9 Factory, Adapter, and Decorator
## Pattern 1: Factory
- **Intent:** move calendar-provider creation out of workflow logic and centralize selection in one place[cite: 76].
- **Factory class:** `CalendarAdapterFactory` in `factories/calendar_factory.py`[cite: 76].

## Pattern 2: Adapter
- **Intent:** translate the application's narrow calendar contract into the behavior of a particular provider[cite: 76, 77].
- **Adapter:** `FakeCalendarAdapter` in `adapters/fake_calendar.py`[cite: 77].

## Pattern 3: Decorator
- **Intent:** add logging around a calendar operation without changing provider code[cite: 77].
- **Decorator class:** `LoggingCalendarDecorator` in `adapters/logging_calendar.py`[cite: 77].