import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition
threadLock = threading.Lock()

class StudentThread(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):

        # Acquire lock for registration only
        threadLock.acquire()
        print("---> " + self.name +
              " registered at the computer lab. Process ID: "
              + str(os.getpid()) + "\n")

        # Release lock after registration
        threadLock.release()

        # Students can now work independently
        time.sleep(self.duration)
        print("---> " + self.name + " finished the assignment\n")


def main():
    start_time = time.time()

    # Create 9 student threads
    threads = []

    for i in range(1, 10):
        t = StudentThread("Student#" + str(i), randint(1, 5))
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    print("All students have finished.")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
