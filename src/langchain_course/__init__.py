from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient()


class Source(BaseModel):
    """Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for a agent response containing an answer and sources"""

    answer: str = Field(description="The agent response")

    sources: list[Source] = Field(
        description="The source relating to the answer", default_factory=list
    )


@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query)


llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main() -> None:
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages": HumanMessage("What's the weather like in Wolverhampton?")}
    )
    response = result["structured_response"]
    print(f"Answer:\n{response.answer}")
    print("Sources:")
    for source in response.sources:
        print(f"  - {source.url}")
