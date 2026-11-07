# Thread Synchronization with Queue

## Overview

This practical demonstrates thread synchronization in Python using the `Queue` class from the `queue` module.

The example simulates an Online Food Order Processing System, where a producer adds food orders to a shared queue and multiple consumers retrieve and process those orders concurrently.

## Practical Example: Food Order Processing System

The program consists of four threads:

- **Producer (Order System):** Generates random food orders and adds them to the queue.
- **Consumer 1 (Kitchen Worker):** Retrieves and prepares food orders.
- **Consumer 2 (Kitchen Worker):** Retrieves and prepares food orders.
- **Consumer 3 (Kitchen Worker):** Retrieves and prepares food orders.

All three kitchen workers share the same queue and process orders concurrently.

The program generates five food orders, such as:
- Burger
- Pizza
- Pasta
- Sandwich
- Fried Rice

## How It Works

1. A shared `Queue()` is created.
2. The Producer generates a random food order.
3. `queue.put(item)` adds the order to the queue.
4. The Consumer threads use `queue.get()` to retrieve available orders.
5. Each worker simulates food preparation using `time.sleep()`.
6. `queue.task_done()` marks an order as completed.
7. `queue.join()` makes the main program wait until all orders are processed.
8. Special `None` values are added to the queue to signal the workers to stop.
9. `thread.join()` waits for all worker threads to terminate.

## Python Concepts Used

| Concept | Description |
|---|---|
| `threading.Thread` | Creates custom threads using classes. |
| `Queue()` | Creates a thread-safe queue for sharing data between threads. |
| `put(item)` | Adds an item to the queue. |
| `get()` | Retrieves and removes an item from the queue. |
| `task_done()` | Marks a retrieved task as completed. |
| `queue.join()` | Waits until all queued tasks are completed. |
| `time.sleep()` | Simulates order processing time. |
| `random.choice()` | Selects a random food order. |
| `thread.join()` | Waits for a thread to finish execution. |

## FIFO (First In, First Out)

The Queue follows the FIFO principle, meaning the first item added is the first item removed.

## Requirements

- Python 3.x
- No external libraries required.

The program uses Python's built-in modules:
- `threading`
- `queue`
- `time`
- `random`

## How to Run

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Run the following command:

```bash
python threading_with_queue.py
```

## Expected Output

The output displays the Producer adding food orders and multiple Kitchen Workers processing them.
<img width="323" height="328" alt="image" src="https://github.com/user-attachments/assets/bc6f9935-ef49-43c4-81f5-ebd787e01221" />
