from agent.states import AgentState
from domain.models import StudyPlan
from ports.calendar_port import CalendarUnavailableError

class StudyPlanningOrchestrator:
    def __init__(self, planner, calendar, memory):
        self.planner = planner
        self.calendar = calendar
        self.memory = memory
        self.state = AgentState.IDLE

    def move_to(self, new_state):
        self.state = new_state
        print(f"STATE -> {self.state.value}")
        self.memory.append(f"State: {self.state.value}")

    def generate_plan(self, student, assignments):
        print(f"REQUEST -> Generate weekly plan for {student.name}")
        self.move_to(AgentState.OBSERVING)

        if not assignments:
            self.move_to(AgentState.WAITING_FOR_INPUT)
            print("RESULT -> Please enter at least one assignment.")
            return StudyPlan(student=student)

        self.move_to(AgentState.CALLING_TOOL)
        try:
            availability = self.calendar.get_availability()
            self.memory.append("Tool result: calendar availability received")
        except CalendarUnavailableError as error:
            self.move_to(AgentState.FAILED)
            print(f"RESULT -> Could not generate plan: {error}")
            return StudyPlan(student=student)

        self.move_to(AgentState.PLANNING)
        plan = self.planner.create_plan(student, assignments, availability)
        self.memory.append("Generated study plan")
        self.move_to(AgentState.COMPLETED)
        print("RESULT -> Study plan generated")
        return plan