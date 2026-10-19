# Useful SQL Inspection Queries 

 

Run these queries with any SQLite browser, or compare them with `inspect_database.py`. 

 

```sql 

SELECT * FROM students; 

SELECT * FROM assignments; 

SELECT * FROM planning_requests; 

SELECT * FROM memory_events; 

SELECT * FROM tool_calls; 

``` 

 

Reconstruct a stored plan with a relational join: 

 

```sql 

SELECT a.title, pi.scheduled_slot, pi.planned_hours 

FROM plan_items AS pi 

JOIN assignments AS a ON a.assignment_id = pi.assignment_id 

WHERE pi.plan_id = 1; 

``` 