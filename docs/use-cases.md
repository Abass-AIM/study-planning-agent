# Use Cases

## Actors

- Student - primary human actor
- Calendar Service - external system used when calendar availability is enabled

## Use Cases

- **UC-01:** Enter assignments
- **UC-02:** Generate weekly plan
- **UC-03:** Review plan and explanation
- **UC-04:** Regenerate plan
- **UC-05:** Read calendar availability

## Mermaid Use-Case-Style Diagram

```mermaid
flowchart LR
 Student["Student"]
 Calendar["Calendar Service"]

 subgraph SPA["Study Planning Agent"]
 UC1(["Enter assignments"])
 UC2(["Generate weekly plan"])
 UC3(["Review plan and explanation"])
 UC4(["Regenerate plan"])
 UC5(["Read calendar availability"])
 end

 Student --- UC1
 Student --- UC2
 Student --- UC3
 Student --- UC4
 Calendar --- UC5
 UC2 -. optional data .-> UC5