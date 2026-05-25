# Coder Crew

A single-agent crew that writes Python code to solve a given problem and executes it safely inside Docker.

Part of the [CrewAI projects collection](../README.md), based on Ed Donner's [Agentic AI Engineering course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/).

## What it does

The **coder** agent receives a programming problem, writes Python to solve it, runs the code in a sandboxed Docker container, and returns both the source and program output.

Default problem in `main.py` — estimate π using the Leibniz series:

> Write Python code to calculate the first 10,000 terms of the series, multiplying the total by 4:  
> `1/1 − 1/3 + 1/5 − 1/7 + 1/9 − 1/11 + ...`

## Key features

- **Safe code execution** — `code_execution_mode="safe"` runs agent-generated code in Docker
- **Retry logic** — up to 3 retries with a 30-second execution timeout
- **Sequential process** — single agent, single task

Configuration: `src/coder/config/agents.yaml`, `src/coder/config/tasks.yaml`, `src/coder/crew.py`

## Requirements

- Python **3.10–3.13**
- [uv](https://docs.astral.sh/uv/)
- [CrewAI CLI](https://docs.crewai.com)
- **[Docker Desktop](https://docs.docker.com/desktop/)** — must be running for code execution
- API key: `OPENAI_API_KEY`

## Setup

```bash
cd coder
uv sync
```

Ensure Docker Desktop is installed and running, then add `OPENAI_API_KEY` to your `.env` file.

## Run

```bash
crewai run
```

Or:

```bash
uv run coder
```

## Output

| File | Description |
|------|-------------|
| `output/code_output.txt` | Generated Python code and execution result |

## Customize

Change the `problem` string in `src/coder/main.py` to ask the agent to solve a different challenge.

## Credits

Project structure and learning goals from **Ed Donner's** [Complete Agentic AI Engineering Course](https://edwarddonner.com/2025/04/21/the-complete-agentic-ai-engineering-course/) and [ed-donner/agents](https://github.com/ed-donner/agents) repository.
