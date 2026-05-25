# Analyst Crew

A hierarchical stock-analysis crew that discovers trending companies in a sector, researches them, and recommends the best investment candidate.

Part of the [CrewAI projects collection](../README.md), based on Ed Donner's [Agentic AI Engineering course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/).

## What it does

1. **Trending company finder** — searches the web for 2–3 companies trending in `{sector}`
2. **Financial researcher** — produces detailed analysis for each company
3. **Stock picker** — selects the best investment and explains why others were passed over
4. **Manager** — delegates tasks across the crew in a hierarchical workflow

Default sector in `main.py`: **India's Defence Industry**

## Key features

- **Hierarchical process** — manager agent delegates to specialists
- **Memory** — short-term, long-term, and entity memory (stored under `data/`)
- **Web search** — SerperDevTool for live news and research
- **Structured outputs** — Pydantic models for company lists and research reports
- **Multi-LLM routing** — OpenAI, Google Gemini, and Anthropic Claude per agent

Agent definitions: `src/analyst/config/agents.yaml`  
Tasks and output paths: `src/analyst/config/tasks.yaml`  
Crew assembly: `src/analyst/crew.py`

## Requirements

- Python **3.10–3.13**
- [uv](https://docs.astral.sh/uv/)
- [CrewAI CLI](https://docs.crewai.com)
- API keys:
  - `OPENAI_API_KEY`
  - `ANTHROPIC_API_KEY`
  - `GOOGLE_API_KEY`
  - `SERPER_API_KEY`

## Setup

```bash
cd analyst
uv sync
```

Add the required keys to a `.env` file at the repo root or in this directory.

## Run

```bash
crewai run
```

Or:

```bash
uv run analyst
```

## Outputs

| File | Description |
|------|-------------|
| `output/trending_companies.json` | Trending companies with tickers and reasons |
| `output/research_report.json` | Per-company market analysis and investment outlook |
| `output/decision.md` | Final pick, rationale, and rejected alternatives |
| `data/*.db` | Memory stores (short-term, long-term, entity) |

## Customize

Edit the `sector` input in `src/analyst/main.py`, or change agent roles and LLM assignments in the YAML configs.

## Credits

Project structure and learning goals from **Ed Donner's** [Complete Agentic AI Engineering Course](https://edwarddonner.com/2025/04/21/the-complete-agentic-ai-engineering-course/) and [ed-donner/agents](https://github.com/ed-donner/agents) repository.
