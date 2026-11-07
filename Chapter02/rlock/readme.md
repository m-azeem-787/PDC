# Bank Account Management System using Python RLock

## Overview
This project demonstrates Python thread synchronization using `threading.RLock()` through a practical Bank Account Management System.

Two threads access the same bank account simultaneously:
- **Depositor:** Deposits Rs. 500 into the account.
- **Withdrawer:** Withdraws Rs. 200 from the account.

The RLock protects the shared account balance and allows the same thread to acquire the same lock multiple times.

## Features
- Uses Python's `threading` module.
- Implements a shared bank account.
- Runs deposit and withdrawal operations concurrently.
- Uses `threading.RLock()` to prevent simultaneous unsafe balance modifications.
- Demonstrates nested lock acquisition.
- Uses `start()` and `join()` for thread management.

## How RLock Works

The most important part of this program is the nested method calls:

```python
def update_balance(self, amount):
    with self.lock:
        self.balance += amount

def deposit(self):
    with self.lock:
        self.update_balance(500)

def withdraw(self):
    with self.lock:
        self.update_balance(-200)
```

When `deposit()` or `withdraw()` calls `update_balance()`, the same thread acquires the same lock again.

A normal `Lock` would cause a deadlock in this situation, whereas an `RLock` allows the same thread to acquire it multiple times.

Each acquisition must be released before another thread can acquire the lock.

## Initial Account Details

- Initial Balance: Rs. 1,000
- Deposit Amount: Rs. 500 per transaction
- Withdrawal Amount: Rs. 200 per transaction
- Number of Deposits: Randomly generated between 1 and 5
- Number of Withdrawals: Randomly generated between 1 and 5

## Sample Output
<img width="212" height="121" alt="image" src="https://github.com/user-attachments/assets/b634993d-b1fb-472a-8ebd-2eada55d4355" />

*Note: The number and order of transactions may vary because of random values and concurrent thread execution.*

## Concepts Demonstrated

| Concept | Description |
|---|---|
| `threading.RLock()` | Creates a reentrant lock. |
| `with self.lock` | Acquires and automatically releases the lock. |
| Nested lock acquisition | Allows the same thread to acquire the RLock again. |
| `threading.Thread()` | Creates a new thread. |
| `start()` | Starts thread execution. |
| `join()` | Waits for a thread to finish. |
| `time.sleep(1)` | Simulates a delay between transactions. |
| `random.randint()` | Generates random transaction counts. |

## How to Run

**1. Clone the repository**

```bash
git clone <repository-url>
```

**2. Navigate to the project directory**

```bash
cd Python-Multithreading-RLock
```

**3. Run the program**

```bash
python rlock.py
```

## Key Takeaway

A normal `Lock` cannot be acquired again by the same thread while it is already held. An `RLock` allows the same thread to acquire the same lock multiple times.

This makes RLock useful when a method holding a lock calls another method that also requires the same lock.

