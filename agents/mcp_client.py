import asyncio
from fastmcp import Client


async def main():
    async with Client("http://127.0.0.1:8000/mcp") as mcp_client:
        tools = await mcp_client.list_tools()
        print(f"Available tools: {tools}")


if __name__ == "__main__":
    asyncio.run(main())
