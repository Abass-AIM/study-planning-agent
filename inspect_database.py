import sqlite3  # Import Python's built-in SQLite driver so the database can be inspected without extra software. 

from pathlib import Path  # Import Path so the script can check whether the runtime database exists. 

DATABASE_FILE = Path("study_planning_agent.db")  # Point the inspection script at the Week 6 runtime database file. 

TABLES = ["students", "assignments", "planning_requests", "study_plans", "plan_items", "memory_events", "tool_calls"]  # List the normalized tables whose row counts will be displayed. 

if __name__ == "__main__":  # Execute the following inspection code only when this file is run directly. 

    if not DATABASE_FILE.exists():  # Check whether the application has created a database yet. 

        raise SystemExit("Database not found. Run: python run.py --reset-db")  # Stop with a clear beginner-friendly instruction instead of a long traceback. 

    connection = sqlite3.connect(DATABASE_FILE)  # Open the existing SQLite database for read-only-style inspection queries. 

    print("DATABASE SUMMARY")  # Print a heading that separates inspection output from normal application output. 

    for table in TABLES:  # Visit each normalized Week 6 relation in a predictable order. 

        count = connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]  # Count rows in the selected teaching table. 

        print(f"{table}: {count}")  # Display the table name and row count. 

    request = connection.execute("SELECT request_id, status FROM planning_requests ORDER BY request_id DESC LIMIT 1").fetchone()  # Read the most recently created persistent planning request. 

    if request:  # Check whether at least one planning request exists. 

        print(f"LATEST REQUEST -> id={request[0]} state={request[1]}")  # Display the request identifier and persisted task state. 

    plan = connection.execute("SELECT study_plans.plan_id, students.name FROM study_plans JOIN students ON students.student_id = study_plans.student_id ORDER BY study_plans.plan_id DESC LIMIT 1").fetchone()  # Join normalized plan and student tables to inspect the latest plan owner. 

    if plan:  # Check whether at least one study plan exists. 

        print(f"LATEST PLAN -> id={plan[0]} student={plan[1]}")  # Display the generated plan identifier and student name from the relational join. 

    rows = connection.execute("SELECT assignments.title, plan_items.scheduled_slot, plan_items.planned_hours FROM plan_items JOIN assignments ON assignments.assignment_id = plan_items.assignment_id WHERE plan_items.plan_id = (SELECT MAX(plan_id) FROM study_plans) ORDER BY plan_items.plan_item_id").fetchall()  # Join PLAN_ITEMS with ASSIGNMENTS to reconstruct the latest plan details. 

    for title, slot, hours in rows:  # Iterate through the reconstructed plan rows returned by the join query. 

        print(f"PLAN ROW -> {slot}: {title} ({hours} h)")  # Display relational data in a form comparable with the domain-object output. 

    connection.close()  # Release the database resource after inspection is complete. 