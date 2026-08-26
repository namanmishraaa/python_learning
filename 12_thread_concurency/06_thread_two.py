import threading 
import time

def prepare_chai(type_, wait_time):
    print(f"{type_} chai : Brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: ready...")

start = time.time()

thread_1=threading.Thread(target=prepare_chai, args=("Masala",2))
thread_2= threading.Thread(target=prepare_chai,args=("Ginger",3))


thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

end = time.time()


print(f"Total time take : {end - start:.2f} second")