#Youssef Usama Mohamed 23013106 (OS section)
import threading
import time

HR=threading.Semaphore(5)

def interview(n):
    print(f"Interviewee {n} is waiting \n  ")
    HR.acquire()
    print(f"Interviewee {n} is heading inside \n")
    time.sleep(1)
    print(f"Intervieww {n} has left \n")
    HR.release()

Inter=[]
for i in range(10):
    Int=threading.Thread(target=interview , args=(i,))
    Inter.append(Int)
    Int.start()


for Int in Inter:
    Int.join