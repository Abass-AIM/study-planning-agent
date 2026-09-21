from pathlib import Path
import json
from datetime import datetime

MEMORY_FILE = Path("agent_memory.json")

TARGETS = {
    Path("notes/week1.md"): "# Week 1 Notes\n\nCreated by the mini agent.\n",
    Path("agent_output.txt"): "The mini agent completed its Week 1 setup task.\n",
}


def load_memory():
    if MEMORY_FILE.exists():
        return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    return []


def save_memory(memory):
    MEMORY_FILE.write_text(
        json.dumps(memory, indent=2),
        encoding="utf-8"
    )


def observe():
    """Return the target files that do not exist yet."""
    return [path for path in TARGETS if not path.exists()]


def decide(missing_files):
    """Choose the next action."""
    if not missing_files:
        return None
    return missing_files[0]


def write_file_tool(path):
    """Tool used by the agent to change the environment."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(TARGETS[path], encoding="utf-8")


def remember(memory, message):
    memory.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "event": message,
    })
    save_memory(memory)


def run_agent():
    memory = load_memory()

    print("Goal: make sure the Week 1 project artefacts exist.")

    while True:
        missing = observe()
        next_file = decide(missing)

        if next_file is None:
            remember(memory, "Goal complete")
            print("Goal complete. No more actions are required.")
            break

        print(f"Observed missing file: {next_file}")
        print(f"Decision: create {next_file}")

        write_file_tool(next_file)

        remember(memory, f"Created {next_file}")
        print(f"Action completed: {next_file}\n")


if __name__ == "__main__":
    run_agent()