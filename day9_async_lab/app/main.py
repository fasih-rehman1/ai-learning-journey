import asyncio
from resilient_client import call_ai

async def main():
    result = await call_ai(
        "Explain AI"
    )
    print(result)
asyncio.run(main())