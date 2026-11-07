import threading
import time
import random

class BankAccount:
    def __init__(self):
        self.lock = threading.RLock()
        self.balance = 1000

    def update_balance(self, amount):
        with self.lock:
            self.balance += amount

    def deposit(self):
        with self.lock:
            self.update_balance(500)

    def withdraw(self):
        with self.lock:
            self.update_balance(-200)


def depositor(account, transactions):
    print("Number of deposits:", transactions)
    while transactions:
        account.deposit()

        print("Deposited Rs. 500")

        time.sleep(1)
        transactions -= 1


def withdrawer(account, transactions):
    print("Number of withdrawals:", transactions)
    while transactions:
        account.withdraw()

        print("Withdrawn Rs. 200")

        time.sleep(1)
        transactions -= 1


def main():
    account = BankAccount()
    t1 = threading.Thread(
        target=depositor,
        args=(account, random.randint(1, 5))
    )

    t2 = threading.Thread(
        target=withdrawer,
        args=(account, random.randint(1, 5))
    )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\n========== BANK ACCOUNT ==========")
    print("Final Balance: Rs.", account.balance)

if __name__ == "__main__":
    main()