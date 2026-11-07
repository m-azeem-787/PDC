
import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared order queue
items = []

MAX_CAPACITY = 10
TOTAL_ORDERS = 20

# Condition variable
condition = threading.Condition()

# Indicates whether the waiter has finished
production_done = False


class Consumer(threading.Thread):

    # Consumer represents the kitchen
    def consume(self):
        with condition:
            # Wait if there are no orders
            while len(items) == 0 and not production_done:
                logging.info('No orders available. Kitchen waiting...')
                condition.wait()

            # Stop when all orders have been received and processed
            if len(items) == 0 and production_done:
                return False

            # Take an order from the queue
            order = items.pop(0)

            logging.info(
                'Kitchen received: {} | Pending orders: {}'.format(
                    order, len(items)
                )
            )

            # Notify waiter that space is available
            condition.notify_all()

        # Prepare food outside the lock
        time.sleep(random.randint(1, 3))
        logging.info('Order completed: {}'.format(order))
        return True

    def run(self):
        while self.consume():
            pass


class Producer(threading.Thread):
    # Producer represents the waiter
    def produce(self):
        with condition:
            # Wait if the order queue is full
            while len(items) >= MAX_CAPACITY:
                logging.info('Order queue full. Waiter waiting...')
                condition.wait()

            # Receive a customer order
            order = random.choice([
                'Burger',
                'Pizza',
                'Pasta',
                'Sandwich',
                'Fried Rice'
            ])

            items.append(order)
            logging.info(
                'New order received: {} | Total pending orders: {}'.format(
                    order, len(items)
                )
            )

            # Notify kitchen that a new order is available
            condition.notify_all()

    def run(self):
        global production_done
        for i in range(TOTAL_ORDERS):
            time.sleep(0.5)
            self.produce()

        # Waiter has finished receiving orders
        with condition:
            production_done = True
            condition.notify_all()

        logging.info('Waiter has finished receiving orders.')


def main():

    waiter = Producer(name='Waiter')
    kitchen = Consumer(name='Kitchen')

    # Start both threads
    waiter.start()
    kitchen.start()

    # Wait for both threads to finish
    waiter.join()
    kitchen.join()

    logging.info('All restaurant orders completed.')


if __name__ == "__main__":
    main()
