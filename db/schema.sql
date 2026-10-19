-- Week 6 relational schema for the Study Planning Agent. 

PRAGMA foreign_keys = ON; 

 

-- One row represents one student. 

CREATE TABLE IF NOT EXISTS students ( 

    student_id INTEGER PRIMARY KEY, 

    name TEXT NOT NULL 

); 

 

-- Assignments belong to students through a foreign key instead of repeating student data. 

CREATE TABLE IF NOT EXISTS assignments ( 

    assignment_id INTEGER PRIMARY KEY, 

    student_id INTEGER NOT NULL, 

    title TEXT NOT NULL, 

    deadline TEXT NOT NULL, 

    estimated_hours REAL NOT NULL CHECK (estimated_hours >= 0), 

    priority INTEGER NOT NULL, 

    FOREIGN KEY (student_id) REFERENCES students(student_id) 

); 

 

-- A planning request stores persistent task state for one agent workflow execution. 

CREATE TABLE IF NOT EXISTS planning_requests ( 

    request_id INTEGER PRIMARY KEY AUTOINCREMENT, 

    student_id INTEGER NOT NULL, 

    status TEXT NOT NULL, 

    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, 

    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, 

    FOREIGN KEY (student_id) REFERENCES students(student_id) 

); 

 

-- A study plan belongs to one student; individual assignments are linked through PLAN_ITEMS. 

CREATE TABLE IF NOT EXISTS study_plans ( 

    plan_id INTEGER PRIMARY KEY AUTOINCREMENT, 

    student_id INTEGER NOT NULL, 

    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, 

    FOREIGN KEY (student_id) REFERENCES students(student_id) 

); 

 

-- PLAN_ITEMS resolves the plan-to-assignment relationship and stores attributes of the scheduling relationship. 

CREATE TABLE IF NOT EXISTS plan_items ( 

    plan_item_id INTEGER PRIMARY KEY AUTOINCREMENT, 

    plan_id INTEGER NOT NULL, 

    assignment_id INTEGER NOT NULL, 

    scheduled_slot TEXT NOT NULL, 

    planned_hours REAL NOT NULL CHECK (planned_hours >= 0), 

    FOREIGN KEY (plan_id) REFERENCES study_plans(plan_id), 

    FOREIGN KEY (assignment_id) REFERENCES assignments(assignment_id) 

); 

 

-- Agent memory is stored as chronological events that may be linked to one planning request. 

CREATE TABLE IF NOT EXISTS memory_events ( 

    memory_event_id INTEGER PRIMARY KEY AUTOINCREMENT, 

    request_id INTEGER, 

    event_type TEXT NOT NULL, 

    message TEXT NOT NULL, 

    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, 

    FOREIGN KEY (request_id) REFERENCES planning_requests(request_id) 

); 

 

-- External tool calls are trace/log data and are kept separate from long-term memory. 

CREATE TABLE IF NOT EXISTS tool_calls ( 

    tool_call_id INTEGER PRIMARY KEY AUTOINCREMENT, 

    request_id INTEGER NOT NULL, 

    tool_name TEXT NOT NULL, 

    status TEXT NOT NULL, 

    details TEXT, 

    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, 

    FOREIGN KEY (request_id) REFERENCES planning_requests(request_id) 

); 