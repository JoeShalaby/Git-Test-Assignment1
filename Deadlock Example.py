import threading   
import time       

ResAlpha = threading.Lock()
ResBeta = threading.Lock()
#Wtih deadlock
def thread_function_1():
   
    with ResAlpha:
        print("Thread 1 acquired resource Alpha")

       
        time.sleep(1)

        print("Thread 1 waiting for resource Beta")

     
        with ResBeta:
            print("Thread 1 acquired resource Beta")

def thread_function_2():
   
    with ResBeta:
        print("Thread 2 acquired resource Beta")


        time.sleep(1)

        print("Thread 2 waiting for resource Alpha")

      
        with ResBeta:
            print("Thread 2 acquired resource Alpha")
#with deadlock solved
##def thread_function_1():
   
    with ResAlpha:
        print("Thread 1 acquired resource Alpha")

       
        time.sleep(1)

        print("Thread 1 waiting for resource Beta")

     
    with ResBeta:
            print("Thread 1 acquired resource Beta")

##def thread_function_2():
   
    with ResBeta:
        print("Thread 2 acquired resource Beta")


        time.sleep(1)

        print("Thread 2 waiting for resource Alpha")

      
    with ResBeta:
            print("Thread 2 acquired resource Alpha")
thread_a = threading.Thread(target=thread_function_1)
thread_b = threading.Thread(target=thread_function_2)

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()
