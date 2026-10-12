 

# System Architecture 

 

## Selected style 

 

The project uses a **layered architecture** for the overall application and **ports/adapters** around external boundaries. 

 

```mermaid 

flowchart LR 

    subgraph PRESENTATION["Presentation"] 

        CLI["run.py / Presentation"] 

    end 

 

    subgraph APPLICATION["Application / Agent"] 

        ORCH["StudyPlanningOrchestrator"] 

        PLANNER["Planner"] 

        STATES["AgentState"] 

    end 

 

    subgraph DOMAIN["Domain"] 

        STUDENT["Student"] 

        ASSIGNMENT["Assignment"] 

        PLANITEM["PlanItem"] 

        STUDYPLAN["StudyPlan"] 

    end 

 

    subgraph PORTS["Ports / Contracts"] 

        CALPORT["CalendarPort"] 

        MEMPORT["MemoryStore"] 

    end 

 

    subgraph ADAPTERS["Adapters / Infrastructure"] 

        CALADAPTER["FakeCalendarAdapter"] 

        MEMADAPTER["JsonMemoryStore"] 

    end 

 

    CLI --> ORCH 

    ORCH --> PLANNER 

    ORCH --> STATES 

    ORCH --> CALPORT 

    ORCH --> MEMPORT 

    PLANNER --> STUDENT 

    PLANNER --> ASSIGNMENT 

    PLANNER --> PLANITEM 

    PLANNER --> STUDYPLAN 

    CALADAPTER -. implements .-> CALPORT 

    MEMADAPTER -. implements .-> MEMPORT 

``` 

 

## Dependency rule 

 

The core application depends on abstractions (`CalendarPort`, `MemoryStore`). Concrete adapters depend on those abstractions. The orchestrator does not construct the concrete adapters. 