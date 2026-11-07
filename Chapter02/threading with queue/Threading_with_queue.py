
"""Thread synchronization using Queue"""

from threading import Thread
from queue import Queue
import time
import random


class OrderSystem(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(5):

            # Generate a random food order
            item = random.choice([
                'Burger',
                'Pizza',
                'Pasta',
                'Sandwich',
                'Fried Rice'
            ])

            # Add the order to the queue
            self.queue.put(item)
            print('Order System: New order %s added to queue by %s\n'
                  % (item, self.name))

            time.sleep(1)


class KitchenWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get an order from the queue
            item = self.queue.get()
            print('Kitchen Worker: Preparing %s by %s'
                  % (item, self.name))

            # Simulate food preparation
            time.sleep(random.randint(1, 3))
            print('Kitchen Worker: %s order completed by %s\n'
                  % (item, self.name))

            # Inform the queue that the task is completed
            self.queue.task_done()


if __name__ == '__main__':
    # Create a shared queue
    queue = Queue()

    # Create one order system
    t1 = OrderSystem(queue)

    # Create three kitchen workers
    t2 = KitchenWorker(queue)
    t3 = KitchenWorker(queue)
    t4 = KitchenWorker(queue)

    # Start all threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # Wait for the order system to finish
    t1.join()

    # Wait until all orders are processed
    queue.join()

    # Stop all kitchen workers
    for worker in (t2, t3, t4):
        queue.put(None)

    # Wait for kitchen workers to exit
    t2.join()
    t3.join()
    t4.join()

    print('All food orders have been completed!')