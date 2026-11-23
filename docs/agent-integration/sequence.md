\# Week 11 Agent Interaction Sequence



The sequence records the successful path and makes the fail-fast boundary visible. Time flows downwards; the Mermaid `alt`/`else` branches are mutually exclusive.



```mermaid

sequenceDiagram

&#x20;   actor Student

&#x20;   participant Coordinator as AgentCoordinator

&#x20;   participant Planning as PlanningAgent

&#x20;   participant Core as StudyPlanningOrchestrator

&#x20;   participant Calendar as CalendarPort

&#x20;   participant Memory as SQLiteMemoryStore

&#x20;   participant Review as ReflectionAgent



&#x20;   Student->>Coordinator: request weekly plan

&#x20;   Coordinator->>Planning: execute(student, assignments)

&#x20;   Planning->>Core: generate\_plan(student, assignments)



&#x20;   alt assignments missing

&#x20;       Core->>Memory: append WaitingForInput

&#x20;       Core-->>Planning: empty StudyPlan

&#x20;       Planning-->>Coordinator: empty StudyPlan

&#x20;       Coordinator->>Memory: append coordination stopped

&#x20;       Coordinator-->>Student: request missing input

&#x20;   else assignments provided

&#x20;       Core->>Calendar: get\_availability()

&#x20;       alt calendar tool fails

&#x20;           Calendar--xCore: CalendarUnavailableError

&#x20;           Core->>Memory: append Failed

&#x20;           Core-->>Planning: empty StudyPlan

&#x20;           Planning-->>Coordinator: empty StudyPlan

&#x20;           Coordinator->>Memory: append coordination stopped

&#x20;           Coordinator-->>Student: controlled failure

&#x20;       else calendar tool succeeds

&#x20;           Calendar-->>Core: available slots

&#x20;           Core->>Memory: append state and tool events

&#x20;           Core-->>Planning: candidate StudyPlan

&#x20;           Planning-->>Coordinator: candidate StudyPlan

&#x20;           Coordinator->>Review: review(assignments, plan)

&#x20;           Review-->>Coordinator: ReflectionResult

&#x20;           Coordinator->>Memory: append reflection decision

&#x20;           Coordinator-->>Student: reviewed StudyPlan

&#x20;       end

&#x20;   end

