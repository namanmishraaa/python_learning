from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Cruching some numbers ...")
    total = 0
    for i in range(10**9):
        total += i
    print("Done")


if __name__ == "__main__":
    start = time.time()

    procesess = [Process(target=cpu_heavy) for _ in range(2)]

    [t.start() for t in procesess]
    [t.join() for t in procesess]

    end = time.time()

    print(f"Total time take : {end - start:.2f} second")