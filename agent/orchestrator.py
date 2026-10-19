from agent.states import AgentState  # Import named workflow states so task-state persistence stays explicit. 

from domain.models import StudyPlan  # Import StudyPlan so controlled early exits can still return a valid domain result. 

from ports.calendar_port import CalendarUnavailableError  # Import the provider-independent calendar failure exposed by the port. 

class StudyPlanningOrchestrator:  # Coordinate observation, tool use, planning, persistence, memory, and result delivery. 

    def __init__(self, planner, calendar, memory, repository):  # Receive all dependencies from run.py instead of constructing adapters inside the application layer. 

        self.planner = planner  # Store the cohesive planning component. 

        self.calendar = calendar  # Store an object that satisfies CalendarPort. 

        self.memory = memory  # Store an object that satisfies MemoryStore. 

        self.repository = repository  # Store an object that satisfies StudyRepository. 

        self.state = AgentState.IDLE  # Begin every newly constructed orchestrator in the Idle state. 

    def move_to(self, new_state, request_id):  # Centralize state transitions so terminal output and database state stay synchronized. 

        self.state = new_state  # Replace the in-memory workflow state with the supplied next state. 

        print(f"STATE -> {self.state.value}")  # Show the transition so students can compare runtime behavior with the Week 4 state diagram. 

        self.repository.update_request_state(request_id, self.state.value)  # Persist the current task state in PLANNING_REQUESTS. 

        self.memory.append(f"State: {self.state.value}", request_id=request_id)  # Persist the same transition as chronological agent memory. 

    def generate_plan(self, student, assignments):  # Define the main application use case coordinated by this orchestrator. 

        self.repository.save_student(student)  # Persist the Student entity before any rows refer to its primary key. 

        self.repository.save_assignments(student.student_id, assignments)  # Persist normalized Assignment rows and their student foreign key. 

        request_id = self.repository.create_request(student.student_id)  # Create a persistent task-state row for this planning request. 

        print(f"REQUEST -> {request_id} created for {student.name}")  # Make the persistent request identifier visible in the terminal. 

        self.move_to(AgentState.OBSERVING, request_id)  # Enter Observing while checking whether required assignment data exists. 

        if not assignments:  # Decide whether the planning workflow has enough domain input to continue. 

            self.move_to(AgentState.WAITING_FOR_INPUT, request_id)  # Persist the waiting state rather than inventing missing assignments. 

            print("RESULT -> Please enter at least one assignment.")  # Explain why no plan was generated. 

            return StudyPlan(student=student)  # Return an empty but valid domain aggregate. 

        self.move_to(AgentState.CALLING_TOOL, request_id)  # Persist the tool-call state before invoking the external calendar capability. 

        try:  # Protect the workflow because external tools can fail. 

            availability = self.calendar.get_availability()  # Request availability through CalendarPort instead of accessing provider details directly. 

            self.repository.log_tool_call(request_id, "CalendarTool", "SUCCESS", f"{len(availability)} slots returned")  # Persist a successful tool trace in TOOL_CALLS. 

            self.memory.append("Calendar availability received", request_id=request_id)  # Store a concise memory event linked to the same planning request. 

        except CalendarUnavailableError as error:  # Handle the controlled provider-independent calendar failure. 

            self.repository.log_tool_call(request_id, "CalendarTool", "FAILED", str(error))  # Persist the failed tool call for later trace inspection. 

            self.move_to(AgentState.FAILED, request_id)  # Persist the terminal Failed task state. 

            print(f"RESULT -> Could not generate plan: {error}")  # Explain the failure to the user without crashing the process. 

            return StudyPlan(student=student)  # Return an empty domain aggregate while keeping the application stable. 

        self.move_to(AgentState.PLANNING, request_id)  # Persist the Planning state after all required inputs are available. 

        plan = self.planner.create_plan(student=student, assignments=assignments, availability=availability)  # Delegate scheduling rules to the cohesive Planner component. 

        plan_id = self.repository.save_plan(plan)  # Map and persist the StudyPlan aggregate into STUDY_PLANS and PLAN_ITEMS. 

        self.memory.append(f"Study plan {plan_id} generated", request_id=request_id)  # Persist an agent memory event that references the stored plan identifier. 

        print(f"DATABASE -> study plan {plan_id} saved")  # Make relational persistence visible in the terminal output. 

        self.move_to(AgentState.COMPLETED, request_id)  # Persist the terminal Completed task state. 

        print("RESULT -> Study plan generated")  # Report successful goal completion to the presentation layer. 

        return plan  # Return the generated domain aggregate to the caller. 