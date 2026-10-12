# Architecture Decisions 

 

## ADR-01 - Use layered architecture with ports/adapters at external boundaries 

 

**Status:** Accepted 

 

**Decision:** Keep domain concepts independent, coordinate the use case in an orchestrator, and access external capabilities through abstract ports. 

 

**Reason:** The design is beginner-friendly while demonstrating lower coupling, higher cohesion, replaceable integrations, and clear dependency direction. 

 

## Coupling and cohesion review 

 

| Component | Cohesion | Coupling observation | 

|---|---|---| 

| `domain/models.py` | High: domain data only | Does not depend on calendar or JSON | 

| `planner.py` | High: planning only | Depends on domain objects and plain input data | 

| `orchestrator.py` | High: workflow coordination | Uses ports instead of concrete adapters | 

| `fake_calendar.py` | High: calendar adapter only | Replaceable without changing planner | 

| `json_memory.py` | High: JSON persistence only | Replaceable behind `MemoryStore` | 

 

## Dependency direction 

 

Preferred: 

 

```text 

Presentation -> Orchestrator -> Planner / Ports -> Domain 

                               ^ 

                               | 

                         Adapters implement Ports 

``` 