from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRSUCTIONS
from schemas import AgentResponse
from langchain_tavily import TavilySearch

# Khởi tạo tools
tools = [TavilySearch()]

# Khởi tạo model


# Khởi tạo agent mới sử dụng create_agent
agent = create_agent(
    model="gpt-4",
    tools=tools,
    system_prompt=REACT_PROMPT_WITH_FORMAT_INSTRSUCTIONS,
    response_format=AgentResponse,  
)

# Sử dụng invoke trực tiếp
def main():
    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"}
            ]
        }
    )
    print(result)

if __name__ == "__main__":
    main()
