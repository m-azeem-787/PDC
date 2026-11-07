# Thread Synchronization Using Locks

## Overview

This practical demonstrates thread synchronization in Python using the `threading.Lock()` class.

It includes two programs that show how the placement of `acquire()` and `release()` affects thread execution and concurrency.

Both programs simulate a Computer Lab, where nine students share access to a computer lab resource.

## Practical Example: Computer Lab

The programs consist of nine student threads:
- Each thread represents a student.
- Each student requires a different amount of time to complete a task.
- A shared Lock controls access to a protected section of code.
- The programs demonstrate the difference between sequential and concurrent execution.

## Program 1: MyThreadClass_lock.py

### Lock Held During the Entire Task

In the first program, the lock is acquired before the task starts and released only after the task finishes.

**Execution sequence:**

1. A student acquires the lock.
2. The student starts using the computer.
3. `time.sleep()` simulates the time spent using the computer.
4. The student finishes the task.
5. The lock is released.
6. The next student can acquire the lock.

### Code Concept

```python
threadLock.acquire()

print("Student started using the computer")

time.sleep(self.duration)

print("Student finished using the computer")

threadLock.release()
```

**Result:** Only one thread can execute the protected section at a time. Other threads must wait until the lock is released.

This results in sequential execution of the tasks inside the locked section.

## Program 2: MyThreadClass_lock_2.py

### Lock Released Before the Task Finishes

In the second program, the lock is released immediately after the initial protected operation.

**Execution sequence:**

1. A student acquires the lock.
2. The student completes the initial registration.
3. The lock is released.
4. The student starts working on the assignment.
5. Other students can acquire the lock and continue their work.
6. Multiple students can work concurrently.

### Code Concept

```python
threadLock.acquire()

print("Student registered at the computer lab")

threadLock.release()

time.sleep(self.duration)

print("Student finished the assignment")
```

**Result:** The lock protects only the initial operation. The remaining task can execute concurrently with other threads.



## Python Concepts Used

| Concept | Description |
|---|---|
| `threading.Lock()` | Creates a lock object for thread synchronization. |
| `acquire()` | Acquires the lock. Other threads must wait if it is already held. |
| `release()` | Releases the lock so another thread can acquire it. |
| `Thread` | Creates custom threads using a class. |
| `run()` | Defines the task performed by each thread. |
| `start()` | Starts thread execution. |
| `join()` | Waits for a thread to finish. |
| `time.sleep()` | Simulates the time taken to complete a task. |
| `randint()` | Generates random task durations. |
| `os.getpid()` | Returns the process ID of the current process. |

## Requirements

- Python 3.x
- No external libraries required.

The programs use Python's built-in modules:

- `threading`
- `time`
- `os`
- `random`

## How to Run

Run each program separately from the terminal.

**Program 1:**

```bash
python MyThreadClass_lock.py
```

**Program 2:**

```bash
python MyThreadClass_lock_2.py
```

## Expected Output

Both programs display the starting and finishing messages for nine student threads.

Example:

<img width="359" height="295" alt="image" src="https://github.com/user-attachments/assets/5571c183-2158-4a85-98e0-20c10d800e61" />


<img width="355" height="338" alt="image" src="https://github.com/user-attachments/assets/3e84a8ff-f0a2-4478-afd4-f81c268c51de" />



*Note: The output order and execution time may vary.*

## Key Takeaway

A Lock ensures that only one thread at a time can execute a protected section of code.

The placement of `acquire()` and `release()` determines how much of the program is protected.

- **Program 1:** Holds the lock throughout the task, resulting in sequential execution of the protected work.
- **Program 2:** Releases the lock before the task, allowing multiple threads to perform their work concurrently.
