__author__ = "ayengec"
__email__ =  "alicaneem@gmail.com"
""" 
This example shows the importance of interprocess communication and usage of threads
We need sometimes communicate many functions or processes input/outputs each other.
To control which sequence it must be, we need to use threads.

"""

import threading
from queue import Queue

# function1 puts each receiving value to queue
def function1(out_q, a): 
    out_q.put(a)          # queue.put() function appends 'a' value to our queue
    print("Here is Function1 and pushed data="+str(a))
    a=a+1

# function1 pulls each data from the queue filled by function1
def function2(in_q):
    data=in_q.get()       # queue.pull() function receives data from the queue
    in_q.task_done()      # our adventure had started when q.join() was called in main. 
                          # Now, we have completed this task after called task_done() method.
    print("Here is Function2 and pulled data="+str(data))

if __name__ == "__main__":  # main process of our code. it's important for big projects
    i=0
    while i<10:
        q=Queue() # q object is instantiated from Queue class
        th1=threading.Thread(target=function1, args=(q, i**2))
        print("Thread1 is created")
        th2=threading.Thread(target=function2, args=(q, ))
        print("Thread2 is created")
        th1.start() # Start the th1's activity
        th2.start() # Start the th2's activity

        q.join()
        i+=1