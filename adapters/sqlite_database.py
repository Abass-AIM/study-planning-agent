import sqlite3  # Import Python's built-in SQLite driver so no third-party package is required. 

from pathlib import Path  # Import Path so database and schema file locations are handled safely. 

SCHEMA_FILE = Path(__file__).resolve().parents[1] / "db" / "schema.sql"  # Locate the SQL schema from the installed project structure. 

def connect(database_path):  # Define one helper that creates consistently configured database connections. 

    connection = sqlite3.connect(database_path)  # Open or create the SQLite database file selected by the caller. 

    connection.execute("PRAGMA foreign_keys = ON")  # Enforce declared foreign-key relationships for every connection. 

    return connection  # Return the configured connection to the repository or memory adapter. 

def initialize_database(database_path):  # Define the operation that creates all Week 6 tables from schema.sql. 

    schema_sql = SCHEMA_FILE.read_text(encoding="utf-8")  # Load the version-controlled relational schema as text. 

    connection = connect(database_path)  # Open a configured SQLite connection. 

    connection.executescript(schema_sql)  # Execute all CREATE TABLE statements contained in the schema file. 

    connection.commit()  # Persist any schema changes before closing the connection. 

    connection.close()  # Release the database resource after initialization is complete. 