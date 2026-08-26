import threading 
import time

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk Boiled!")



def toast_bun():
    print("Toasting bun...")
    time.sleep(3)
    print("Done with toasting!")

start = time.time()

thread_1=threading.Thread(target=boil_milk)
thread_2= threading.Thread(target=toast_bun)


thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()

end = time.time()


print(f"Total time take : {end - start:.2f} second")