from fastmcp import FastMCP
# 创建一个MCP服务器
mcp = FastMCP("fastmcp-server")

# 添加一个加法工具
@mcp.tool()
def say_hello(name:str) -> str:
    return 'hello,' + name

@mcp.tool()
def add(a:int, b:int) -> int:
    return a+b

# 添加一个动态问候资源
@mcp.resource("greeting://{name}")
def get_greeting(name:str) -> str:
    return f"Hello {name}!"

if __name__ == '__main__':
    mcp.run(transport="stdio")