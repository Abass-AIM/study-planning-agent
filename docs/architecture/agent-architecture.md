# Agent Architecture 

 

```mermaid 

flowchart TD 

    GOAL["Goal: generate a weekly study plan"] --> ORCH["Orchestrator"] 

    ORCH --> OBSERVE["Observe assignments"] 

    OBSERVE --> INPUT{"Assignments available?"} 

    INPUT -- No --> WAIT["Wait for input"] 

    INPUT -- Yes --> TOOL["Call CalendarPort"] 

    TOOL --> TOOLRESULT{"Tool succeeded?"} 

    TOOLRESULT -- No --> FAIL["Return controlled failure"] 

    TOOLRESULT -- Yes --> MEMORY1["Store tool event via MemoryStore"] 

    MEMORY1 --> PLAN["Delegate to Planner"] 

    PLAN --> MEMORY2["Store plan event via MemoryStore"] 

    MEMORY2 --> DONE["Return StudyPlan"] 

``` 

 

## Agent responsibilities 

 

- **Orchestrator:** controls the workflow and decides what component is called next. 

- **Planner:** contains deterministic planning logic. 

- **Tool port:** defines what calendar capability the workflow needs. 

- **Memory port:** defines how events are stored and retrieved. 

- **Adapters:** implement external details without becoming the application's core logic. 