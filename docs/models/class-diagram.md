# Class Diagram

The following UML class diagram represents the main domain classes of the Study Planning Agent and their relationships.

```mermaid
classDiagram
 direction LR
 class Student {
 +int student_id
 +string name
 +string email
 }
 class Assignment {
 +int assignment_id
 +string title
 +date deadline
 +float estimated_hours
 +int priority
 }
 class StudyPlan {
 +int plan_id
 +date start_date
 +date end_date
 +add_item(item)
 +total_hours()
 }
 class PlanItem {
 +int plan_item_id
 +date scheduled_date
 +float planned_hours
 +string reason
 }
 Student "1" --> "0..*" Assignment : owns
 Student "1" --> "0..*" StudyPlan : receives
 StudyPlan "1" *-- "0..*" PlanItem : contains
 PlanItem "0..*" --> "1" Assignment : schedules
```