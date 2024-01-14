import threading
import time


class myThread(threading.Thread):
    def __init__(self, thread_ID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = thread_ID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        self.print_time( self.counter, 3)
        # Free lock to release next thread
        threadLock.release()

    def print_time(self, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (self, time.ctime(time.time())))
            counter -= 1


threadLock = threading.Lock()
threads = []
# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
# Start new Threads
thread1.start()
thread2.start()
# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")
