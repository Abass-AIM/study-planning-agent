from abc import ABC, abstractmethod

class MemoryStore(ABC):
    @abstractmethod
    def load(self):
        raise NotImplementedError

    @abstractmethod
    def append(self, event):
        raise NotImplementedError