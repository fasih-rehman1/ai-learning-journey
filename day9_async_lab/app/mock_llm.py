import asyncio

async def mock_llm(prompt: str):
    print("Sending Request to Ai . Mock LLM is thinking...")
    await asyncio.sleep(6)
    return f"Answer to the prompt: {prompt} - Mock LLM response"
