# Engineering Team Crew

A four-agent software team that takes high-level requirements and delivers a working backend module, Gradio UI, and unit tests.

Part of the [CrewAI projects collection](../README.md), based on Ed Donner's [Agentic AI Engineering course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/).

## What it does

Given a requirements brief, the crew runs a sequential pipeline:

1. **Engineering lead** — writes a detailed design (classes, methods, signatures)
2. **Backend engineer** — implements the Python module from the design
3. **Frontend engineer** — builds a simple Gradio demo UI (`app.py`)
4. **Test engineer** — writes unit tests for the backend

Default project in `main.py`: a **trading simulation account management system** (`accounts.py` / `Account` class) with deposits, withdrawals, share trades, portfolio valuation, and balance guards.

## Agents

| Agent | Responsibility | Default LLM |
|-------|----------------|-------------|
| `engineering_lead` | System design document | `gpt-4o-mini` |
| `backend_engineer` | Python backend module | `gpt-4o-mini` |
| `frontend_engineer` | Gradio UI prototype | `gpt-4o` |
| `test_engineer` | Unit tests | `gpt-4o-mini` |

Configuration: `src/engineering_team/config/agents.yaml`, `src/engineering_team/config/tasks.yaml`

## Requirements

- Python **3.10–3.13**
- [uv](https://docs.astral.sh/uv/)
- [CrewAI CLI](https://docs.crewai.com)
- API key: `OPENAI_API_KEY`
- **Gradio** — included in project dependencies for the generated UI

## Setup

```bash
cd engineering_team
uv sync
```

Add `OPENAI_API_KEY` to your `.env` file.

## Run

```bash
crewai run
```

Or:

```bash
uv run engineering_team
```

## Outputs

| File | Description |
|------|-------------|
| `output/accounts.py_design.md` | Architecture and API design |
| `output/accounts.py` | Backend implementation |
| `output/app.py` | Gradio demo UI |
| `output/test_accounts.py` | Unit tests |

After the crew finishes, you can run the demo:

```bash
cd output
uv run python app.py
```

## Customize

Edit `requirements`, `module_name`, and `class_name` in `src/engineering_team/main.py` to have the team build a different application.

## Credits

Project structure and learning goals from **Ed Donner's** [Complete Agentic AI Engineering Course](https://edwarddonner.com/2025/04/21/the-complete-agentic-ai-engineering-course/) and [ed-donner/agents](https://github.com/ed-donner/agents) repository.
