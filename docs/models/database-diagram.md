# Database Diagram

The following ER diagram represents the persistent data model of the Study Planning Agent, including entities, primary keys, foreign keys, and relationships.

```mermaid
erDiagram
 STUDENT ||--o{ ASSIGNMENT : owns
 STUDENT ||--o{ STUDY_PLAN : has
 STUDY_PLAN ||--o{ PLAN_ITEM : contains
 ASSIGNMENT ||--o{ PLAN_ITEM : scheduled_as

 STUDENT {
   int student_id PK
   string name
   string email
 }

 ASSIGNMENT {
   int assignment_id PK
   int student_id FK
   string title
   date deadline
   float estimated_hours
   int priority
 }

 STUDY_PLAN {
   int plan_id PK
   int student_id FK
   date start_date
   date end_date
 }

 PLAN_ITEM {
   int plan_item_id PK
   int plan_id FK
   int assignment_id FK
   date scheduled_date
   float planned_hours
   string reason
 }
```