
import threading
import time
import random

# Function for CS
def process_cs(marks):
    print(threading.current_thread().name + " --> Starting result processing")
    time.sleep(2)

    total = sum(marks)
    print("Computer Science Total Marks:", total)
    print(threading.current_thread().name + " --> Processing completed\n")


# Function for SE
def process_se(marks):
    print(threading.current_thread().name + " --> Starting result processing")

    time.sleep(4)

    total = sum(marks)
    print("Software Engineering Total Marks:", total)

    print(threading.current_thread().name + " --> Processing completed\n")


# Function for AI
def process_ai(marks):
    print(threading.current_thread().name + " --> Starting result processing")

    time.sleep(1)

    total = sum(marks)
    print("Artificial Intelligence Total Marks:", total)

    print(threading.current_thread().name + " --> Processing completed\n")


def main():
    start_time = time.time()

    # Create threads with names and functions
    t1 = threading.Thread(
        name="CS_Thread",
        target=process_cs,
        args=([80, 75, 90],)
    )

    t2 = threading.Thread(
        name="SE_Thread",
        target=process_se,
        args=([85, 70, 95],)
    )

    t3 = threading.Thread(
        name="AI_Thread",
        target=process_ai,
        args=([90, 88, 92],)
    )

    # Start all threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()

    print("All department results processed successfully!")

    print("Total Execution Time:", round(time.time() - start_time, 2), "seconds")


if __name__ == "__main__":
    main()
