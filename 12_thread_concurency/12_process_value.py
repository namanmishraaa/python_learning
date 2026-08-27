from multiprocessing import Process, Queue, Value

def increment(counter):
    for _ in range(10000):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    queue = Queue()
    counter = Value('i', 1)
    process = [Process(target=increment, args=(counter,)) for _ in range(4)]
    [p.start() for p in process]
    [p.join() for p in process]
    print(f"Final counter values : {counter.value}")
