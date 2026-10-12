import json
from pathlib import Path
from ports.memory_store import MemoryStore

class JsonMemoryStore(MemoryStore):
    def __init__(self, filename="week5_memory.json"):
        self.path = Path(filename)

    def load(self):
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def append(self, event):
        events = self.load()
        events.append(event)
        self.path.write_text(json.dumps(events, indent=2), encoding="utf-8")