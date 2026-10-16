# -*- coding: utf-8 -*-
"""
安装依赖：pip install fastmcp
天气查询 MCP 服务器
基于 FastMCP的天气查询mcp
启动方式：
    fastmcp run server.py            # stdio 模式
    fastmcp run server.py --transport sse --port 8000  # SSE 模式
提供的工具（Tools）：
    get_weather(city)        查询城市当前天气
"""

import asyncio
from typing import Any
from fastmcp import FastMCP

mcp = FastMCP(
    name="weather",
    instructions="天气查询服务：可查询城市实时天气",
)


@mcp.tool
async def get_weather(city: str) -> dict[str, Any]:
    """查询指定城市的当前实时天气。

    Args:
        city: 中国城市名称，用英文的形式表示（如 "Shanghai"）
    """
    if city == "shanghai":
        return {"result": "上海今天天气晴朗，15摄氏度，微风~"}
    elif city == "beijing":
        return {"result": "北京今天天气寒冷，-3摄氏度，有强冰雹"}
    elif city == "hangzhou":
        return {"result": "杭州今天阴转晴，午后有大风，不适合出行"}
    else:
        return {"result": "我无法获取当前天气"}


if __name__ == "__main__":
    # 本地调试：直接以 stdio 方式运行
    mcp.run()