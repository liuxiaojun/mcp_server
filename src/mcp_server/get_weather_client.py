# -*- coding: utf-8 -*-
"""
天气 MCP 的 stdio 客户端
通过 stdio 传输方式拉起 get_weather_server.py 子进程，连接后列出工具并调用 get_weather

运行方式：
    python get_weather_client.py                # 交互式输入城市
    python get_weather_client.py shanghai       # 直接指定城市（可多个）
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Any

# Windows 控制台默认 GBK，强制 UTF-8 输出
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

HERE = Path(__file__).resolve().parent
SERVER_SCRIPT = HERE / "get_weather_server.py"

# 用和客户端相同的 Python 解释器拉起服务器子进程
TRANSPORT = StdioTransport(
    command=sys.executable,
    args=[str(SERVER_SCRIPT)],  # mcp服务器的路径
    env={"PYTHONIOENCODING": "utf-8", "PYTHONUNBUFFERED": "1"},
)


def format_result(city: str, result: Any) -> str:
    """把 call_tool 的返回结果整理成可读文本。"""
    payload = getattr(result, "data", result)
    if isinstance(payload, dict):
        return payload.get("result", json.dumps(payload, ensure_ascii=False))
    return str(payload)


async def main() -> None:
    cities = [a.strip().lower() for a in sys.argv[1:] if a.strip()]
    if not cities:
        raw = input("请输入要查询的城市（英文，多个用空格分隔）：").strip()
        cities = [c.lower() for c in raw.split() if c]

    # 通过 stdio 连接服务器（自动拉起子进程，退出 with 块时自动关闭）
    async with Client(TRANSPORT) as client:
        # 1. 列出服务器提供的工具
        tools = await client.list_tools()
        print("=" * 46)
        print("已连接 weather MCP (stdio)，可用工具:")
        for t in tools:
            description = (t.description or "").strip()
            summary = description.splitlines()[0] if description else "暂无描述"
            print(f"  - {t.name}: {summary}")
        print("=" * 46)

        # 2. 逐个调用 get_weather
        for city in cities:
            try:
                result = await client.call_tool("get_weather", {"city": city})  # 传入一个工具名与工具调用参数
                print(f"[{city}] {format_result(city, result)}")
            except Exception as e:  # noqa: BLE001
                print(f"[{city}] 调用失败: {e}")


if __name__ == "__main__":
    asyncio.run(main())
