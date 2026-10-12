# Interfaces 

 

```mermaid 

classDiagram 

    class CalendarPort { 

        <<interface>> 

        +get_availability() 

    } 

 

    class MemoryStore { 

        <<interface>> 

        +load() 

        +append(event) 

    } 

 

    class FakeCalendarAdapter { 

        -bool should_fail 

        +get_availability() 

    } 

 

    class JsonMemoryStore { 

        -Path path 

        +load() 

        +append(event) 

    } 

 

    class StudyPlanningOrchestrator { 

        -Planner planner 

        -CalendarPort calendar 

        -MemoryStore memory 

        +generate_plan(student, assignments) 

    } 

 

    class Planner { 

        +create_plan(student, assignments, availability) 

    } 

 

    FakeCalendarAdapter ..|> CalendarPort : implements 

    JsonMemoryStore ..|> MemoryStore : implements 

    StudyPlanningOrchestrator --> CalendarPort : uses 

    StudyPlanningOrchestrator --> MemoryStore : uses 

    StudyPlanningOrchestrator --> Planner : delegates planning 

``` 

 

## Why these interfaces matter 

 

`CalendarPort` and `MemoryStore` protect the core workflow from provider-specific details. A later real calendar or SQLite memory adapter can replace the teaching adapters without rewriting the orchestrator. 