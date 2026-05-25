# Debate Crew

A three-agent debate crew: one agent argues **for** a motion, another argues **against** it, and a judge decides which side was more convincing.

Part of the [CrewAI projects collection](../README.md), based on Ed Donner's [Agentic AI Engineering course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/).

## What it does

1. **Proposing debator** — builds a persuasive case in favor of the motion
2. **Opposing debator** — presents counterarguments against the motion
3. **Judge** — reviews both sides and declares a winner with reasoning

Default inputs in `main.py`:

- **Topic:** Real estate investing
- **Motion:** *"Buying a real estate property in India is a good investment"*

## Agents & models

| Agent | Role | Default LLM |
|-------|------|-------------|
| `debatorProposing` | Argues for the motion | OpenAI `gpt-4o-mini` |
| `debatorOpposing` | Argues against the motion | Google `gemini-2.5-flash` |
| `judge` | Evaluates and decides | Anthropic Claude 3.7 Sonnet |

Agent definitions: `src/debate/config/agents.yaml`  
Task flow: `src/debate/config/tasks.yaml`

## Requirements

- Python **3.10–3.13**
- [uv](https://docs.astral.sh/uv/)
- [CrewAI CLI](https://docs.crewai.com)
- API keys: `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `ANTHROPIC_API_KEY`

## Setup

```bash
cd debate
uv sync
```

Add your API keys to a `.env` file at the repo root or in this directory.

## Run

```bash
crewai run
```

Or from Python:

```bash
uv run debate
```

## Outputs

| File | Description |
|------|-------------|
| `output/debatorProposing.md` | Argument in favor of the motion |
| `output/debatorOpposing.md` | Argument against the motion |
| `output/decide.md` | Judge's verdict and rationale |

## Customize

Edit `src/debate/main.py` to change `topic` and `motion`, or adjust agent prompts in the YAML config files.

## Credits

Project structure and learning goals from **Ed Donner's** [Complete Agentic AI Engineering Course](https://edwarddonner.com/2025/04/21/the-complete-agentic-ai-engineering-course/) and [ed-donner/agents](https://github.com/ed-donner/agents) repository.
