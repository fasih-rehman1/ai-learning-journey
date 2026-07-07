import asyncio
from mock_llm import mock_llm

async def call_ai(prompt):
    for attempt in range(2):
        try:
            print(f"Attempt {attempt+1}")
            return await asyncio.wait_for(
                mock_llm(prompt),
                timeout=5
            )


        except asyncio.TimeoutError:
            print("Timeout!")
            if attempt==0:
                print("Retrying...\n")
            else:
                print("Failed After Retry")

    return None


# from _typeshed import NoneType
# import asyncio
# from mock_llm import mock_llm

# async def call_ai(prompt: str):
#     for attempt in range(2):
#         try:
#             print(f"Attempt {attempt + 1} of 2")
#             response = await asyncio.wait_for(
#                 mock_llm(prompt),
#                 timeout=5
#             )
#         return response

#         except asyncio.TimeoutError:
#             print(f"Timeout!...... Attempt {attempt + 1} timed out. Retrying...")
#             if attempt == 0:
#                 print("Retrying!.."/n)
#             else:
#                 print("Failed After Retry......")

#     return None    


        

