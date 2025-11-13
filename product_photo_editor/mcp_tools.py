from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters


mcp_toolset = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="uv",
            args=[
                "run",
                "veo_mcp/main.py",
            ],
        ),
        timeout=120, # seconds
    ),
)

# Option to connect to remote MCP server

# from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

# mcp_toolset = MCPToolset(
#     connection_params=StreamableHTTPConnectionParams(
#         url="http://localhost:8000/mcp",
#         timeout=120,
#     ),
# )