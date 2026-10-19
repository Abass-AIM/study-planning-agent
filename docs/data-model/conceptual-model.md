# Conceptual Data Model 

 

The conceptual model names the important information concepts and relationships before SQL types or implementation details are added. 

 

```mermaid 

erDiagram 

    STUDENT ||--o{ ASSIGNMENT : owns 

    STUDENT ||--o{ STUDY_PLAN : receives 

    STUDY_PLAN ||--o{ PLAN_ITEM : contains 

    ASSIGNMENT ||--o{ PLAN_ITEM : scheduled_as 

    STUDENT ||--o{ PLANNING_REQUEST : submits 

    PLANNING_REQUEST ||--o{ MEMORY_EVENT : records 

    PLANNING_REQUEST ||--o{ TOOL_CALL : logs 

``` 

 

Teaching interpretation: 

- `PLAN_ITEM` is an association concept between a plan and an assignment. 

- `PLANNING_REQUEST` stores task state for one agent workflow. 

- `MEMORY_EVENT` stores persistent memory/history. 

- `TOOL_CALL` stores trace information about external actions. 