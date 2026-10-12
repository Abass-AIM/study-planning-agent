from enum import Enum

class AgentState(Enum):
    IDLE = "Idle"
    OBSERVING = "Observing"
    WAITING_FOR_INPUT = "WaitingForInput"
    CALLING_TOOL = "CallingCalendarTool"
    PLANNING = "Planning"
    COMPLETED = "Completed"
    FAILED = "Failed"