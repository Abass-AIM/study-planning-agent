from ports.study_repository import StudyRepository  # Import the persistence contract implemented by this SQLite repository. 

from adapters.sqlite_database import connect  # Reuse the common configured SQLite connection helper. 

class SQLiteStudyRepository(StudyRepository):  # Implement project persistence using normalized relational tables. 

    def __init__(self, database_path):  # Receive the database file location from the composition root. 

        self.database_path = database_path  # Store the selected database path for all repository operations. 

    def save_student(self, student):  # Persist one Student domain object into the STUDENTS relation. 

        connection = connect(self.database_path)  # Open a configured SQLite connection. 

        connection.execute("INSERT INTO students (student_id, name) VALUES (?, ?) ON CONFLICT(student_id) DO UPDATE SET name = excluded.name", (student.student_id, student.name))  # Insert or update the student without duplicating its primary key. 

        connection.commit()  # Persist the student change before closing the connection. 

        connection.close()  # Release the database resource after writing is complete. 

    def save_assignments(self, student_id, assignments):  # Persist Assignment objects while storing only the student's foreign-key identifier. 

        connection = connect(self.database_path)  # Open a configured SQLite connection. 

        for assignment in assignments:  # Process each domain Assignment supplied by the application. 

            connection.execute("INSERT INTO assignments (assignment_id, student_id, title, deadline, estimated_hours, priority) VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT(assignment_id) DO UPDATE SET student_id = excluded.student_id, title = excluded.title, deadline = excluded.deadline, estimated_hours = excluded.estimated_hours, priority = excluded.priority", (assignment.assignment_id, student_id, assignment.title, assignment.deadline.isoformat(), assignment.estimated_hours, assignment.priority))  # Insert or update one normalized assignment row. 

        connection.commit()  # Persist all assignment changes as one small transaction. 

        connection.close()  # Release the database resource after writing is complete. 

    def create_request(self, student_id):  # Create one persistent task-state record for a new planning request. 

        connection = connect(self.database_path)  # Open a configured SQLite connection. 

        cursor = connection.execute("INSERT INTO planning_requests (student_id, status) VALUES (?, ?)", (student_id, "Idle"))  # Insert the initial request state and keep the generated identifier. 

        request_id = cursor.lastrowid  # Read the automatically generated primary key of the new request. 

        connection.commit()  # Persist the new planning request before returning its identifier. 

        connection.close()  # Release the database resource after writing is complete. 

        return request_id  # Return the persistent request identifier to the orchestrator. 

    def update_request_state(self, request_id, state):  # Persist the latest state of an existing planning request. 

        connection = connect(self.database_path)  # Open a configured SQLite connection. 

        connection.execute("UPDATE planning_requests SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE request_id = ?", (state, request_id))  # Update only the mutable task-state fields of the selected request. 

        connection.commit()  # Persist the state transition before closing the connection. 

        connection.close()  # Release the database resource after writing is complete. 

    def log_tool_call(self, request_id, tool_name, status, details):  # Persist one external-tool trace for review and debugging. 

        connection = connect(self.database_path)  # Open a configured SQLite connection. 

        connection.execute("INSERT INTO tool_calls (request_id, tool_name, status, details) VALUES (?, ?, ?, ?)", (request_id, tool_name, status, details))  # Insert the tool name, outcome, and readable details using parameterized SQL. 

        connection.commit()  # Persist the tool log before closing the connection. 

        connection.close()  # Release the database resource after writing is complete. 

    def save_plan(self, plan):  # Persist one StudyPlan aggregate across STUDY_PLANS and PLAN_ITEMS. 

        connection = connect(self.database_path)  # Open a configured SQLite connection. 

        cursor = connection.execute("INSERT INTO study_plans (student_id) VALUES (?)", (plan.student.student_id,))  # Insert the plan header and keep the generated plan identifier. 

        plan_id = cursor.lastrowid  # Read the primary key generated for the new study plan. 

        for item in plan.items:  # Process every PlanItem contained by the generated StudyPlan. 

            connection.execute("INSERT INTO plan_items (plan_id, assignment_id, scheduled_slot, planned_hours) VALUES (?, ?, ?, ?)", (plan_id, item.assignment.assignment_id, item.scheduled_slot, item.planned_hours))  # Persist the relationship between plan and assignment plus scheduling attributes. 

        connection.commit()  # Persist the complete plan aggregate as one transaction. 

        connection.close()  # Release the database resource after writing is complete. 

        return plan_id  # Return the generated plan identifier so the application can report what was stored. 