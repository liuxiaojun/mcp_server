# mcp_server.py

from mcp.server.mcpserver import MCPServer

# 创建一个MCP服务器
mcp = MCPServer("Demo")

# 添加一个加法工具
@mcp.tool()
def add(a:int, b:int) -> int:
    return a+b

# 添加一个动态问候资源
@mcp.resource("greeting://{name}")
def get_greeting(name:str) -> str:
    return f"Hello {name}!"

if __name__ == '__main__':
    mcp.run(transport="stdio")