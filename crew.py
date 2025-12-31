"""
Data Science Multi-Agent Crew
Orchestrates multiple AI agents to perform comprehensive data science analysis
"""

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools.csv_reader import csv_reader_tool
from tools.data_stats import data_stats_tool
import os


@CrewBase
class DataScienceCrew():
    """DataScience crew for multi-agent data analysis"""
    
    agents_config = 'agents.yaml'
    tasks_config = 'tasks.yaml'
    
    def __init__(self):
        """Initialize LLM configuration"""
        # Configure LLM based on environment variables
        llm_provider = os.getenv('LLM_PROVIDER', 'openai')
        
        if llm_provider.lower() == 'ollama':
            base_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
            model_name = os.getenv('OLLAMA_MODEL', 'gemma3:1b')
            # For Ollama with CrewAI, prefix model name with ollama/
            self.llm = LLM(
                model=f"ollama/{model_name}",
                base_url=base_url
            )
        elif llm_provider.lower() == 'groq':
            api_key = os.getenv('GROQ_API_KEY')
            model_name = os.getenv('GROQ_MODEL_NAME', 'llama-3.1-70b-versatile')
            self.llm = LLM(
                model=f"groq/{model_name}",
                api_key=api_key
            )
        else:  # Default to OpenAI
            api_key = os.getenv('OPENAI_API_KEY')
            model_name = os.getenv('OPENAI_MODEL_NAME', 'gpt-4-turbo-preview')
            self.llm = LLM(
                model=model_name,
                api_key=api_key
            )
    
    @agent
    def project_planner(self) -> Agent:
        """Creates the Project Planner agent"""
        return Agent(
            config=self.agents_config['project_planner'],
            llm=self.llm,
            verbose=True
        )
    
    @agent
    def data_analyst(self) -> Agent:
        """Creates the Data Analyst agent with tools"""
        return Agent(
            config=self.agents_config['data_analyst'],
            tools=[csv_reader_tool, data_stats_tool],
            llm=self.llm,
            verbose=True
        )
    
    @agent
    def modelling_agent(self) -> Agent:
        """Creates the Modelling Agent"""
        return Agent(
            config=self.agents_config['modelling_agent'],
            llm=self.llm,
            verbose=True
        )
    
    @agent
    def report_writer(self) -> Agent:
        """Creates the Report Writer agent"""
        return Agent(
            config=self.agents_config['report_writer'],
            llm=self.llm,
            verbose=True
        )
    
    @task
    def planning_task(self) -> Task:
        """Creates the planning task"""
        return Task(
            config=self.tasks_config['planning_task'],
        )
    
    @task
    def exploratory_analysis_task(self) -> Task:
        """Creates the exploratory analysis task"""
        return Task(
            config=self.tasks_config['exploratory_analysis_task'],
        )
    
    @task
    def modeling_proposal_task(self) -> Task:
        """Creates the modeling proposal task"""
        return Task(
            config=self.tasks_config['modeling_proposal_task'],
        )
    
    @task
    def report_generation_task(self) -> Task:
        """Creates the report generation task"""
        return Task(
            config=self.tasks_config['report_generation_task'],
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the DataScience crew"""
        return Crew(
            agents=self.agents,  # Automatically uses @agent decorated methods
            tasks=self.tasks,    # Automatically uses @task decorated methods
            process=Process.sequential,
            verbose=True,
        )
