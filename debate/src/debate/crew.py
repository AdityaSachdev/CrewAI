from crewai import Agent, Crew, Process, Task
from pathlib import Path
try:
    # `crewai.project` exists in CrewAI 1.x, but some editors/type-checkers
    # may point at a different interpreter where `crewai` isn't installed.
    from crewai.project import CrewBase, agent, crew, task
except ModuleNotFoundError:  # pragma: no cover
    from typing import Any, Callable

    def CrewBase(cls: type) -> type:  # type: ignore[override]
        return cls

    def agent(fn: Callable[..., Any]) -> Callable[..., Any]:
        return fn

    def task(fn: Callable[..., Any]) -> Callable[..., Any]:
        return fn

    def crew(fn: Callable[..., Any]) -> Callable[..., Any]:
        return fn
from crewai_tools import SerperDevTool

@CrewBase
class Debate():
    """Debate crew"""

    # Use paths relative to this module so running from any cwd works.
    agents_config = str(Path(__file__).parent / "config" / "agents.yaml")
    tasks_config = str(Path(__file__).parent / "config" / "tasks.yaml")

    @agent
    def debatorProposing(self) -> Agent:
        return Agent(
            config=self.agents_config['debatorProposing'],
            verbose=True
        )   

    @agent
    def debatorOpposing(self) -> Agent:
        return Agent(
            config=self.agents_config['debatorOpposing'],
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'],
            verbose=True
        )

    @task
    def debate(self) -> Task:
        return Task(
            config=self.tasks_config['debate'],
            verbose=True
        )

    @task
    def debateOpposing(self) -> Task:
        return Task(
            config=self.tasks_config['debateOpposing'],
            verbose=True
        )

    @task
    def debateDecide(self) -> Task:
        return Task(
            config=self.tasks_config['debateDecide'],
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )