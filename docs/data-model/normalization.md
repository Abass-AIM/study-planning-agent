# Normalization Notes 

 

## A deliberately bad design 

 

Imagine one table like this: 

 

```text 

STUDY_PLAN_RAW( 

  student_id, 

  student_name, 

  assignment1_title, 

  assignment1_deadline, 

  assignment2_title, 

  assignment2_deadline, 

  plan_date, 

  calendar_tool_status 

) 

``` 

 

Problems: 

- repeating assignment groups violate the idea of First Normal Form; 

- student name would be duplicated across many rows; 

- tool-call data is mixed with business data; 

- adding a third assignment changes the table structure; 

- updates can create inconsistent copies of the same fact. 

 

## 1NF 

 

Store one value per field and one row per repeating item. Assignments become separate rows. 

 

## 2NF 

 

Keep facts dependent on the whole key. In this teaching schema most tables use a single-column surrogate primary key, while relationship facts such as `scheduled_slot` belong in `PLAN_ITEMS`. 

 

## 3NF 

 

Remove transitive/redundant facts. `ASSIGNMENTS` stores `student_id`, not a repeated copy of `student_name`. The name is obtained by joining with `STUDENTS`. 

 

## Result 

 

The Week 6 schema separates students, assignments, plans, plan items, planning requests, memory events, and tool-call logs. Each relation has a focused purpose and foreign keys connect related facts. 