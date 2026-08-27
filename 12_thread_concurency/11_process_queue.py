from multiprocessing import Process, Queue

def prepare_chai(queue: Queue):
    queue.put("Masal Chai")

if __name__ == "__main__":
    queue = Queue()
    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get())
