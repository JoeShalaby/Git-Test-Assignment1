import threading
import time

def print_1():
    print("Starting of a thread:", threading.current_thread().name)
    time.sleep(0.02)
    print("Finishing of a thread:", threading.current_thread().name)

def print_2():
    print("Starting of a thread:", threading.current_thread().name)
    print("Finishing of a thread:", threading.current_thread().name)

def print_3():
    print("Starting of a thread:", threading.current_thread().name)
    time.sleep(0.01)
    print("Finishing of a thread:", threading.current_thread().name)

a = threading.Thread(target=print_1, name="Thread-1")
b = threading.Thread(target=print_2, name="Thread-2")
c = threading.Thread(target=print_3, name="Thread-3")

a.start()
b.start()
c.start()

a.join()
b.join()
c.join()
