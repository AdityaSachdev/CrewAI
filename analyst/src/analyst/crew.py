from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pathlib import Path
from pydantic import BaseModel, Field
from crewai_tools import SerperDevTool
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage

class TrendingCompany(BaseModel):
    name: str = Field(description="Company name")
    ticker: str = Field(description="Stock ticker symbol")
    reason: str = Field(description="Reason this company is trending in the news")

class TrendingCompanyList(BaseModel):
    companies: List[TrendingCompany] = Field(description="List of companies trending in the news")

class TrendingCompanyResearch(BaseModel):
    name: str = Field(description="Company name")
    market_position: str = Field(description="Current market position and competitive analysis")
    future_outlook: str = Field(description="Future outlook and growth prospects")
    investment_potential: str = Field(description="Investment potential and suitability for investment")

class TrendingCompanyResearchList(BaseModel):
    research_list: List[TrendingCompanyResearch] = Field(description="Comprehensive research on all trending companies")

@CrewBase
class Analyst(): # pylint: disable=too-few-public-methods
    """Analyst crew to pick stock"""  

    agents_config = str(Path(__file__).parent / "config" / "agents.yaml")
    tasks_config = str(Path(__file__).parent / "config" / "tasks.yaml")

    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['trending_company_finder'],
            verbose=True,
            tools=[SerperDevTool()],
            memory=True
        )   
    
    @agent
    def financial_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_researcher'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def stock_picker(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_picker'],
            verbose=True,
            memory=True
        )

    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['find_trending_companies'],
            verbose=True,
            output_pydantic=TrendingCompanyList
        )

    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config=self.tasks_config['research_trending_companies'],
            verbose=True,
            output_pydantic=TrendingCompanyResearchList
        )

    @task
    def pick_best_company(self) -> Task:
        return Task(
            config=self.tasks_config['pick_best_company'],
        )

    @crew
    def crew(self) -> Crew:
        manager = Agent(
            config=self.agents_config['manager'],
            verbose=True,
            allow_delegation=True
        )
        short_term_memory = ShortTermMemory(storage=RAGStorage( 
            embedder_config= {
                "provider": "openai",
                "config": {
                    "model": "text-embedding-3-small",
                }
            },
            type="short_term",
            path="data/short_term_memory.db"
        ))
        long_term_memory = LongTermMemory(storage=LTMSQLiteStorage(
            db_path="data/long_term_memory.db"
        ))
        entity_memory = EntityMemory(storage=RAGStorage(
            embedder_config= {
                "provider": "openai",
                "config": {
                    "model": "text-embedding-3-small",
                }
            },
            type="entity",
            path="data/entity_memory.db"
        ))
        return Crew(
            manager_agent=manager,
            agents=self.agents,
            tasks=self.tasks, 
            verbose=True,
            process=Process.hierarchical,
            memory=True,
            long_term_memory=long_term_memory,
            short_term_memory=short_term_memory,
            entity_memory=entity_memory
        )