# Multithreading Using a Custom Thread Class in Python

## Overview
This project demonstrates multithreading in Python using a custom thread class that inherits from Python's built-in `Thread` class.

The practical example simulates downloading multiple files concurrently. Each file download is handled by a separate thread, allowing multiple downloads to execute at the same time instead of sequentially.

## Practical Example: Multiple File Downloads

The program simulates an application downloading nine different files simultaneously.

Each thread:
- Represents a separate file download.
- Receives a file name and a random download duration.
- Executes its task using the `run()` method.
- Displays a message when the download starts and finishes.

**Note:** Downloads are simulated using `time.sleep()`. No actual files are downloaded.

## Concepts Covered

- **Thread Class:** Creating a custom class by inheriting from `threading.Thread`.
- **run():** Defining the task that a thread executes.
- **start():** Starting thread execution.
- **join():** Waiting for all threads to complete before proceeding.
- **Concurrent Execution:** Running multiple tasks at the same time.
- **Execution Time:** Measuring the total time taken using the `time` module.

## Technologies Used

- Python 3
- `threading`
- `time`
- `os`
- `random`

All modules used are included in Python's standard library.

## How to Run

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python mythreadclass.py
```

## Expected Output

The program displays messages showing when each file download starts and finishes.

<img width="319" height="282" alt="image" src="https://github.com/user-attachments/assets/3522b1bb-86a9-40ba-bea3-3b8678e42fbb" />

*The output order and execution time will vary because each thread receives a random duration.*
