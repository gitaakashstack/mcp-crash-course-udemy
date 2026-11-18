import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp import StdioServerParameters

load_dotenv()

llm = ChatOpenAI(model="gpt-6-luna")

stdio_server_params = StdioServerParameters(
    command="python",
    args=["C:\\Personal Drive\\LangChain Course\\repos\\mcp-crash-course\\servers\\math_server.py"]
)
async def main():
    print("Hello world")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
