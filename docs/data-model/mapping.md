# Model-to-Database Mapping 

 

| Python / agent concept | Relational representation | Mapping note | 

|---|---|---| 

| `Student` | `students` | `student_id` becomes the primary key. | 

| `Assignment` | `assignments` | The owning student is stored as `student_id` foreign key. | 

| `StudyPlan` | `study_plans` | One plan header row identifies the owner and creation time. | 

| `PlanItem` | `plan_items` | Association table links a plan to an assignment and stores scheduling attributes. | 

| Planning request state | `planning_requests` | The latest agent workflow state is persistent task state. | 

| Agent memory | `memory_events` | Chronological events survive process termination. | 

| Calendar tool trace | `tool_calls` | Tool name, status, details, and time are logged separately from business data. | 

 

The domain model does not need to become identical to the database model. Mapping code in the SQLite repository translates between the two representations. 