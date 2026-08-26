# This is example of multi-threading



import threading
import time 

def take_order():
    for i in range(1,4):
        print(f"taking order for #{i}")
        time.sleep(2)


def make_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)



order_thread=threading.Thread(target=take_order)
brew_thred=threading.Thread(target=make_chai)


order_thread.start()
brew_thred.start()

# Wait for thread to finish the work

order_thread.join()
brew_thred.join()

print("All order taken and chai brewed!")

