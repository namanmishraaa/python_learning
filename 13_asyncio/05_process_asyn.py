import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def ecrypt(data):
    return f" lock {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, ecrypt,"Credit_card_9874")
        print(result)


if __name__ == "__main__":
    start = time.time()
    print(f"Start time: {start}")
    asyncio.run(main())
    end = time.time()
    print(f"End time:{end}")
    print(f"Total time take:{end - start:.2f}")