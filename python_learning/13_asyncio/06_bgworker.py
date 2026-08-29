import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f'Loggine the system health')


async def fetct_order():
    await asyncio.sleep(3)
    print(f"Order fetched")


threading.Thread(target=background_worker, daemon=True)

asyncio.run(fetct_order())