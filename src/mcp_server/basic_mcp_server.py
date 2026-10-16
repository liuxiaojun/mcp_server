from mcp.server.mcpserver import MCPServer
from mcp.server.models import InitializationOptions

# 基础MCP服务器初始化
mcp = MCPServer("demo-server")

@mcp.tool()
def get_server_info() -> dict:
    return {
        "name":"Demo MCP Server",
        "version":"0.0.1",
        "protocol":"MCP",
        "description":"Demo MCP Server",
    }

if __name__ == '__main__':
    mcp.run()