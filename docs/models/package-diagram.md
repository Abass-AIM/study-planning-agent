# Package Diagram

The following package-level diagram shows the logical organization of the Study Planning Agent and the dependencies between its main parts.

```mermaid
flowchart TB
 subgraph UI["Presentation / UI"]
 CLI["Command-line / future UI"]
 end

 subgraph Domain["Domain"]
 Student["Student"]
 Assignment["Assignment"]
 StudyPlan["StudyPlan"]
 PlanItem["PlanItem"]
 end

 subgraph Agent["Agent Logic"]
 Planner["Future Planner / Agent"]
 end

 subgraph Persistence["Persistence"]
 Store["Future repository / database"]
 end

 subgraph Integration["Integrations"]
 Calendar["Future Calendar Adapter"]
 end

 CLI --> Planner
 Planner --> Domain
 Planner --> Store
 Planner --> Calendar
```