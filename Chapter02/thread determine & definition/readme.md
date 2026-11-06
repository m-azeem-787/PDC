# Thread Definition & Thread Determination

## Overview

This project demonstrates multithreading in Python by creating multiple threads to perform different tasks concurrently.

It combines two threading concepts:
- **Thread Definition:** Creating threads using `threading.Thread()` and assigning functions through the `target` parameter.
- **Thread Determination:** Assigning custom names to threads and identifying the currently executing thread using `threading.current_thread().name`.

## Practical Example: University Examination Result Processing System

The program simulates a university processing examination results for three departments:

1. Computer Science
2. Software Engineering
3. Artificial Intelligence

Each department has its own function and runs in a separate thread.

### How It Works

- Three threads are created, one for each department.
- Each thread receives student marks as arguments.
- Custom names are assigned to identify each thread.
- Each thread calculates the total marks after simulating processing time using `time.sleep()`.
- The `join()` method ensures the main program waits for all threads to complete.
- Finally, the total execution time is displayed.

## Concepts Covered

- **threading.Thread():** Creating threads in Python.
- **target:** Specifying the function a thread will execute.
- **args:** Passing arguments to a thread's target function.
- **name:** Assigning custom names to threads.
- **threading.current_thread().name:** Identifying the currently executing thread.
- **start():** Starting thread execution.
- **join():** Waiting for threads to finish.
- **Concurrent Execution:** Running multiple tasks simultaneously.
- **Execution Time:** Measuring program execution time using the `time` module.

## Technologies Used

- Python 3
- `threading`
- `time`

All modules used are included in Python's standard library.

## How to Run

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Execute:

```bash
python file.py
```

## Expected Output

<img width="284" height="158" alt="image" src="https://github.com/user-attachments/assets/5237dbd1-cb1e-4c73-9307-580bbf2eafab" />


*Note: The output order and execution time may vary depending on thread scheduling and system performance.*
