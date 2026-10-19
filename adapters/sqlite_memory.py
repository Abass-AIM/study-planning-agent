from ports.memory_store import MemoryStore  # Import the memory contract that this SQLite adapter implements. 

from adapters.sqlite_database import connect  # Reuse the common database-connection helper. 

class SQLiteMemoryStore(MemoryStore):  # Implement persistent agent memory using the normalized MEMORY_EVENTS table. 

    def __init__(self, database_path):  # Receive the database file path from the composition root. 

        self.database_path = database_path  # Store the selected database path for later memory operations. 

    def load(self):  # Implement the read operation required by MemoryStore. 

        connection = connect(self.database_path)  # Open a configured SQLite connection. 

        rows = connection.execute("SELECT message FROM memory_events ORDER BY memory_event_id").fetchall()  # Retrieve memory messages in stable insertion order. 

        connection.close()  # Release the database resource after reading is complete. 

        return [row[0] for row in rows]  # Convert one-column database rows into a beginner-friendly list of strings. 

    def append(self, event, request_id=None):  # Implement the write operation required by MemoryStore. 

        connection = connect(self.database_path)  # Open a configured SQLite connection. 

        connection.execute("INSERT INTO memory_events (request_id, event_type, message) VALUES (?, ?, ?)", (request_id, "agent_event", event))  # Insert one memory event using parameterized SQL. 

        connection.commit()  # Persist the inserted event before closing the connection. 

        connection.close()  # Release the database resource after writing is complete. 