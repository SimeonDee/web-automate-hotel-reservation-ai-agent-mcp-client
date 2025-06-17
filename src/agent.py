import os
from mcp_use import MCPClient, MCPAgent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
MCP_SERVER_CONFIG_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "mcp_server_config.json")

client = MCPClient.from_config_file(MCP_SERVER_CONFIG_FILE_PATH)
openai_llm = ChatOpenAI(model="gpt-4o")

agent = MCPAgent(
    llm=openai_llm,
    client=client,
    max_steps=30,
)
