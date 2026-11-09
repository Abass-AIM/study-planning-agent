from adapters.fake_calendar import FakeCalendarAdapter  # Import the concrete fake adapter only inside the infrastructure construction layer. 
from ports.calendar_port import CalendarPort  # Import the abstraction returned by the factory so callers can depend on the port rather than a provider class. 
 
class CalendarAdapterFactory:  # Encapsulate calendar-adapter creation so the composition root does not construct concrete providers directly. 
    @staticmethod  # Mark the operation as a factory utility because it does not need object-specific state. 
    def create(provider_name: str, should_fail: bool = False) -> CalendarPort:  # Create one CalendarPort implementation from simple configuration values. 
        normalized_name = provider_name.strip().lower()  # Normalize user configuration so harmless capitalization or spaces do not change provider selection. 
        if normalized_name == "fake":  # Select the deterministic classroom provider used in this semester project. 
            print("FACTORY -> created FakeCalendarAdapter")  # Make the Factory pattern visible in the terminal for the laboratory demonstration. 
            return FakeCalendarAdapter(should_fail=should_fail)  # Return the concrete object through the CalendarPort abstraction. 
        raise ValueError(f"Unsupported calendar provider: {provider_name}")  # Reject unknown providers explicitly instead of silently selecting the wrong integration. 