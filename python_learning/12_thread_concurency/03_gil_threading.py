
import threading 
import time



def brew_chai():
    print(f"{threading.current_thread().name} started brewing....")
    count = 0
    for _ in range(100_000_000):
        count +=1 

    print(f"{threading.current_thread().name} finished brewing....")



thread_1=threading.Thread(target=brew_chai,name="Barista_1")
thread_2= threading.Thread(target=brew_chai,name="Barista_2")

start = time.time()

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

end = time.time()


print(f"Total time take : {end - start:.2f} second")