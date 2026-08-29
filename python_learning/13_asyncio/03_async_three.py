import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetch {url} with status {response.status}")


async def main():
    urls=['https://httpbin.org/delay/2', 'https://httpbin.org/delay/3'] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.time()
    print(f"Start time: {start}")
    asyncio.run(main())
    end = time.time()
    print(f"End time:{end}")
    print(f"Total time take:{end - start:.2f}")