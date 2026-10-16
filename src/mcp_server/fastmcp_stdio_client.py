from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport
from openai import OpenAI
import _asyncio
import logging
import json
import os

class LLMClient():
    def __init__(self,model_name:str,url:str,api_key:str) -> None:
        self.model_name = model_name
        self.url = url
        self.client = OpenAI(api_key,base_url=self.url)

    def get_response(self,messages:list[dict[str,str]]) -> str:
        """发消息给LLM并获取响应"""
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            steam=False
        )
        return response.choices[0].message.content
