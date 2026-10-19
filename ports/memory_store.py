from abc import ABC, abstractmethod  # Import abstract-base-class helpers so Python can express a memory-storage contract. 

class MemoryStore(ABC):  # Define the contract used to persist and retrieve agent memory events. 

    @abstractmethod  # Require every concrete memory adapter to implement load. 

    def load(self):  # Declare the operation that returns previously persisted memory messages. 

        raise NotImplementedError  # Keep storage technology out of the abstract interface. 

    @abstractmethod  # Require every concrete memory adapter to implement append. 

    def append(self, event, request_id=None):  # Declare the operation that stores one memory event and optionally links it to a request. 

        raise NotImplementedError  # Keep database-specific behavior out of the abstract interface. 