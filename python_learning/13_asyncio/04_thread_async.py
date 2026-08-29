import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3)
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock,"Masala chai")
        print(result)


if __name__ == "__main__":
    start = time.time()
    print(f"Start time: {start}")
    asyncio.run(main())
    end = time.time()
    print(f"End time:{end}")
    print(f"Total time take:{end - start:.2f}")