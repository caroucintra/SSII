
# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
import time
 
class MyThread:
    def __init__(self, func):
        self.fun = func
        self.start()

    def start(self):
        self.thread = threading.Thread(target=self.fun, args=())
        self.thread.start()

    def join(self):
        self.thread.join()
        time.sleep(1)
