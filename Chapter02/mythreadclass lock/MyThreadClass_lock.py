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
        # Acquire lock before using the computer
        threadLock.acquire()

        print("---> " + self.name +
              " started using the computer. Process ID: "
              + str(os.getpid()) + "\n")

        # Simulate working on the computer
        time.sleep(self.duration)

        print("---> " + self.name + " finished using the computer\n")

        # Release lock after finishing
        threadLock.release()


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
