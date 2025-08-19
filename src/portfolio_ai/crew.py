from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
from dotenv import load_dotenv
load_dotenv()
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class PortfolioAi():
    """PortfolioAi crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def chatbot(self) -> Agent:
        return Agent(
            config=self.agents_config['chatbot'],
            verbose=True,
            knowledge_sources=[TextFileKnowledgeSource(file_paths=["Joel Mbaka CV.txt"])],
            embedder={
                "provider": "google",
                "config": {
                    "model": "models/text-embedding-004",
                    "api_key": os.getenv("GOOGLE_API_KEY")
                }
            }
        )

    @task
    def chatbot_task(self) -> Task:
        return Task(
            config=self.tasks_config['chatbot_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PortfolioAi crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[TextFileKnowledgeSource(file_paths=["Joel Mbaka CV.txt"])],
            embedder={
                "provider": "google",
                "config": {
                    "model": "models/text-embedding-004",
                    "api_key": os.getenv("GOOGLE_API_KEY")
                }
            }
        )
