from abc import ABC, abstractmethod

class CalendarUnavailableError(Exception):
    pass

class CalendarPort(ABC):
    @abstractmethod
    def get_availability(self):
        raise NotImplementedError