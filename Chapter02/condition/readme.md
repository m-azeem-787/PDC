# Producer-Consumer Using Condition

## Overview

This project demonstrates the Producer-Consumer problem in Python using the `threading.Condition()` synchronization mechanism.

The practical example simulates a Restaurant Order Management System, where a waiter receives customer orders and the kitchen prepares them.

The Producer (Waiter) adds orders to a shared queue, while the Consumer (Kitchen) removes and processes those orders. Condition variables ensure that both threads coordinate their activities safely.

## Practical Example: Restaurant Order Management System

The program simulates a restaurant with the following components:

- **Producer (Waiter):** Receives customer orders and adds them to the shared order queue.
- **Consumer (Kitchen):** Takes orders from the queue and prepares them.
- **Shared Queue:** Stores pending customer orders.
- **Maximum Capacity:** The queue can hold a maximum of 10 pending orders.
- **Condition Variable:** Synchronizes the waiter and kitchen.

The program generates 20 random food orders, including:
- Burger
- Pizza
- Pasta
- Sandwich
- Fried Rice

Each order is processed individually, with a simulated preparation time.

## How It Works

1. The waiter receives a customer order and adds it to the queue.
2. The kitchen checks whether any orders are available.
3. If the queue is empty, the kitchen waits using `condition.wait()`.
4. When a new order arrives, the waiter notifies the kitchen using `condition.notify_all()`.
5. If the queue reaches its maximum capacity of 10 orders, the waiter waits until the kitchen removes an order.
6. The kitchen processes orders in FIFO (First In, First Out) order.
7. Once all 20 orders have been received and processed, both threads terminate.

## Concepts Covered

- **Producer-Consumer Problem:** Understanding communication between producer and consumer threads.
- **threading.Thread:** Creating custom thread classes.
- **threading.Condition():** Synchronizing multiple threads.
- **wait():** Making a thread wait until a condition is satisfied.
- **notify():** Waking up one waiting thread.
- **notify_all():** Waking up all waiting threads.
- **Locking:** Protecting shared data using `with condition`.
- **FIFO:** Processing orders in the order they were received.
- **Thread Coordination:** Managing communication between multiple threads.

## Technologies Used

- Python 3
- `threading`
- `logging`
- `time`
- `random`

## How to Run

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python condition.py
```

## Expected Output

<img width="638" height="371" alt="image" src="https://github.com/user-attachments/assets/cc8d8384-00f9-44fb-8df5-a8604d07b68e" />

