# Study Planning Agent 
 
**Course:** Software Engineering and AI Agent Fundamentals   
**Course code:** GAINBAN-SZOFMEIN-1   
**Project type:** Semester laboratory project 
 
## About This Repository 
 
This repository contains the semester project and laboratory artefacts for the Software Engineering and AI Agent Fundamentals course. 
 
The project is developed incrementally. Each laboratory adds software engineering documentation, models, source code, tests, or AI-agent-related components. 
 
## Current Repository Structure 
 
```text 
study-planning-agent/
|-- README.md
|-- lab_agent.py
|-- agent_memory.json
|-- agent_output.txt
|-- notes/
|   `-- week1.md
`-- docs/
    |-- stakeholders.md
    |-- requirements.md
    |-- user-stories.md
    `-- use-cases.md
``` 
 
## Week 1 - Git Collaboration and AI Agent Fundamentals 
 
Week 1 introduces Git/GitHub collaboration and a deterministic mini-agent simulator. 
 
Topics: 
- repository and commit workflow 
- task branches 
- GitHub Issues 
- Pull Requests 
- autonomy 
- tool use 
- memory 
- action 
 
### Run the Week 1 Demo 
 
```bash 
python lab_agent.py 
``` 
 
If your system uses `python3`: 
 
```bash 
python3 lab_agent.py 
``` 
 
### Week 1 Output Files 
 
- `lab_agent.py` - observe/decide/act logic 
- `agent_memory.json` - persistent memory 
- `agent_output.txt` - file-system action produced by the agent 
- `notes/week1.md` - project artefact created/managed by the agent 
 
## Development Workflow 
 
The project uses `main` as the stable integrated branch. 
 
For each task or laboratory: 
 
```text 
main 
  -> create a task branch 
  -> make and review changes 
  -> git add / git commit 
  -> git push 
  -> Pull Request 
  -> merge into main 
  -> git switch main 
  -> git pull 
``` 
 

## Week 2 - Requirements Engineering

Week 2 adds stakeholder analysis, functional and non-functional requirements, AI-agent boundaries, user stories, acceptance criteria, traceability, and a Mermaid use-case-style model. The artefacts are stored in `docs/`.

## Application Status

The executable `lab_agent.py` application is unchanged from Week 1. Week 2 changes the specification and project documentation, not the implementation.
Do not begin a new laboratory from an old task branch. 
 
## Current Project Status 
 
- Week 1: completed - Git workflow and introductory agent simulator 
- Week 2: next - requirements engineering and use-case modeling 
 
## Course 
 
Software Engineering and AI Agent Fundamentals   
GAINBAN-SZOFMEIN-1
