import asyncio

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from mcp import StdioServerParameters, stdio_client, ClientSession

load_dotenv()

llm = ChatOpenAI(model="gpt-6-luna")

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:\\Personal Drive\\LangChain Course\\repos\\mcp-crash-course\\servers\\math_server.py"]
)
async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
            print("Session initialized")
            tools = await load_mcp_tools(session)
            print(tools)

            agent = create_agent(llm, tools)
            response = await agent.ainvoke({
                "messages": [HumanMessage(content="What is 2+5*8?. Use the tools, dont calculate yourself")]
            })
            print(response["messages"][-1].content)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
