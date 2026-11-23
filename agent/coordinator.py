from agent.states import AgentState  # Reuse the established request-state vocabulary.


class AgentCoordinator:  # Control planning first, followed by conditional reflection.
    def __init__(self, planning_agent, reflection_agent, memory):  # Inject role and memory dependencies.
        self.planning_agent = planning_agent  # Specialist responsible for generating a plan.
        self.reflection_agent = reflection_agent  # Specialist responsible for reviewing that plan.
        self.memory = memory  # Persist coordination outcomes through the existing memory port.

    def run(self, student, assignments):  # Execute one deterministic multi-agent workflow.
        print("COORDINATOR -> planning phase started")  # Mark the planning phase in the trace.
        plan = self.planning_agent.execute(student, assignments)  # Ask for a candidate result.
        state = self.planning_agent.orchestrator.state  # Read the actual terminal workflow state.
        if state != AgentState.COMPLETED:  # Never approve missing-input or failed requests.
            print(f"COORDINATOR -> reflection skipped because planning state is {state.value}")  # Explain.
            self.memory.append(f"Coordination stopped before reflection: {state.value}")  # Save evidence.
            return plan  # Preserve the original controlled result.

        print("COORDINATOR -> reflection phase started")  # Mark the second specialist phase.
        reflection = self.reflection_agent.review(assignments, plan)  # Inspect the candidate plan.
        for check in reflection.checks:  # Surface every successful check.
            print(f"REFLECTION CHECK -> {check}")  # Print check evidence.
        for issue in reflection.issues:  # Surface each discovered issue.
            print(f"REFLECTION ISSUE -> {issue}")  # Print rejection evidence.

        if reflection.accepted:  # Accept a candidate with no issues.
            print("REFLECTION -> ACCEPTED")  # Make the decision visible.
            self.memory.append("Reflection accepted the generated study plan")  # Persist acceptance.
        else:  # Preserve a rejected candidate as a visible, non-approved result.
            print("REFLECTION -> REJECTED")  # Make rejection visible to the caller.
            self.memory.append(  # Save all rejection reasons for later inspection.
                "Reflection rejected the generated study plan: " + "; ".join(reflection.issues)
            )  # Complete the persistent rejection event.

        print("COORDINATOR -> completed")  # Mark the end of coordination.
        return plan  # Keep the existing StudyPlan return contract; inspect the verdict separately.