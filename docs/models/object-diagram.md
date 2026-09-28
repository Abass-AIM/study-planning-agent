# Object Diagram

The following object diagram shows a concrete snapshot of the Study Planning Agent domain model using example runtime objects and values aligned with `app.py`.

```mermaid
flowchart LR
 student1["student1 : Student<br/>student_id = 1<br/>name = Alex Student"]
 a101["assignment101 : Assignment<br/>title = UML Structural Models<br/>priority = 1"]
 a102["assignment102 : Assignment<br/>title = Python Domain Model<br/>priority = 2"]
 plan201["plan201 : StudyPlan<br/>2026-09-14 .. 2026-09-20"]
 item301["item301 : PlanItem<br/>2026-09-15<br/>2.0 h"]
 item302["item302 : PlanItem<br/>2026-09-18<br/>2.5 h"]

 student1 --> a101
 student1 --> a102
 student1 --> plan201
 plan201 --> item301
 plan201 --> item302
 item301 --> a101
 item302 --> a102
```