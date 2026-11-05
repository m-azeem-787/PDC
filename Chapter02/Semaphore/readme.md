# Ticket Booking System using Python Multithreading

## Overview

This project demonstrates the Producer-Consumer problem using Python multithreading and a thread-safe queue.

A ticket booking system is simulated where a producer generates ticket numbers and adds them to a shared queue. Three consumer threads act as customers who retrieve and process the available tickets.

The program demonstrates how multiple threads communicate and synchronize using Python's `Queue` module.

## Features

- Multithreading using Python's `threading` module.
- Producer-Consumer synchronization using `Queue`.
- Generates 10 random ticket numbers.
- Three consumer threads process tickets concurrently.
- Thread-safe communication between the producer and consumers.
- Logging with timestamps, thread names, and log levels.
- Graceful termination using sentinel values (`None`).

## Technologies Used

- Python 3
- `threading`
- `queue`
- `logging`
- `time`
- `random`

## How It Works

The program consists of one producer and three consumers.

### Producer (Booking System)

- Generates 10 random ticket numbers between 1000 and 9999.
- Adds each ticket to the shared queue using `queue.put()`.
- Waits one second between generating tickets.
- Sends a stop signal (`None`) to each consumer after all tickets are produced.

### Consumers (Customers)

- Three consumer threads run concurrently.
- Each consumer waits for an available ticket using `queue.get()`.
- Retrieves and processes one ticket at a time.
- Simulates the booking process using a random delay between 0.5 and 2 seconds.
- Uses `queue.task_done()` to mark each ticket as processed.
- Terminates when it receives the stop signal (`None`).

### Main Function

- Creates the producer and consumer threads.
- Starts all threads.
- Uses `join()` to wait for the producer to finish.
- Uses `queue.join()` to wait until all queued tasks are completed.
- Waits for all consumer threads to terminate.

## Example Output
<img width="521" height="82" alt="image" src="https://github.com/user-attachments/assets/0891d89c-6f7b-4b0d-9bb0-383cbc9b1225" />


*Note: The actual output may vary because ticket numbers, thread scheduling, and processing times are random.*

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your system.

Check your Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
```

Navigate to the project directory:

```bash
cd your-repository
```

### 3. Run the Program

Save the Python code in a file named `ticket_booking.py`.

Run the program:

```bash
python Semaphore.py
```

No external libraries are required. All modules used in this project are included in Python's standard library.

## Concepts Demonstrated

Multithreading: Executes multiple threads concurrently.

Producer-Consumer Problem: Demonstrates communication between a producer and consumers.

Queue: Stores and transfers ticket numbers using FIFO ordering.

`queue.put()`: Adds a ticket to the queue.

`queue.get()`: Retrieves a ticket from the queue.

`queue.task_done()`: Marks a retrieved task as completed.

`queue.join()`: Waits until all queued tasks are completed.

`thread.join()`: Waits for a thread to terminate.

Logging: Displays thread activity with timestamps and log levels.

## Learning Objective

The main objective of this project is to understand how multiple threads can communicate and synchronize using a shared queue.

It demonstrates how a producer generates tasks, how multiple consumers process them concurrently, and how thread synchronization helps coordinate their execution.

