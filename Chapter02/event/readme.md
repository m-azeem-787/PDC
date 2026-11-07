# Event Synchronization

## Overview
This practical demonstrates thread synchronization in Python using the `threading.Event()` class.

The example simulates a Print Server, where employees submit documents to a print queue and a printer waits for notifications before processing print jobs.

## Practical Example: Office Print Server

The program consists of two threads:

- **Employee (Producer):** Generates random document names and adds them to the shared print queue.
- **Printer (Consumer):** Waits for a notification and retrieves documents from the queue for printing.
- **Event:** Acts as a notification signal between the Employee and Printer threads.

## How It Works

1. The Employee waits for 2 seconds.
2. A random document name is generated.
3. The document is added to the shared `print_queue`.
4. `event.set()` signals the Printer that a new print job is available.
5. `event.clear()` resets the notification.
6. The Printer uses `event.wait()` to wait for the notification.
7. Once notified, the Printer retrieves a document using `print_queue.pop()`.

The Employee submits five print jobs.

## Python Concepts Used

| Concept | Description |
|---|---|
| `threading.Thread` | Creates custom threads using classes. |
| `threading.Event()` | Creates an Event object for synchronization. |
| `event.set()` | Sets the Event state to True and signals waiting threads. |
| `event.wait()` | Waits until the Event is set. |
| `event.clear()` | Resets the Event state to False. |
| `time.sleep()` | Adds delays to simulate real-world processing. |
| `random.randint()` | Generates random document identifiers. |
| `start()` | Starts a thread. |
| `join()` | Waits for a thread to finish. |

## Requirements

- Python 3.x
- No external libraries required.

The program uses Python's built-in modules:
- `threading`
- `logging`
- `time`
- `random`

## How to Run

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Run the following command:

```bash
python event.py
```

## Expected Output

The output will display employees submitting print jobs and the printer processing documents.

<img width="585" height="68" alt="image" src="https://github.com/user-attachments/assets/55a8239b-9677-49f5-96db-3e5bd1ecf70c" />


- The Employee uses `event.clear()` to reset the notification.

**This demonstrates basic Event-based synchronization using the Producer-Consumer pattern in Python.**

> **Note:** This is an educational demonstration following the original Event example. It does not implement robust queue synchronization or graceful thread shutdown. A `threading.Condition()` or `queue.Queue` would be more suitable for a reliable print-server implementation.
