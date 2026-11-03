import logging
import threading
import time
import random
from queue import Queue

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

ticket_queue = Queue()

# Number of customers
NUM_CUSTOMERS = 10

def producer():
    # Generate tickets and add them to the queue.
    for i in range(NUM_CUSTOMERS):
        time.sleep(1)
        # Generate a ticket number
        ticket = random.randint(1000, 9999)

        # Add ticket to queue
        ticket_queue.put(ticket)

        logging.info(
            'Booking System: Ticket %d is available',
            ticket
        )

    # Notify consumers that no more tickets will be produced
    for i in range(3):
        ticket_queue.put(None)

def consumer():
    # Customers wait for tickets and book available tickets.
    while True:
        logging.info('Customer is waiting for a ticket')
        # Wait until a ticket becomes available
        ticket = ticket_queue.get()

        # Stop signal
        if ticket is None:
            ticket_queue.task_done()
            break

        logging.info(
            'Customer booked ticket number %d',
            ticket
        )

        # Simulate booking process
        time.sleep(random.uniform(0.5, 2))

        logging.info(
            'Ticket %d booking completed',
            ticket
        )

        ticket_queue.task_done()


def main():
    # Create producer thread
    t1 = threading.Thread(
        target=producer,
        name='BookingSystem'
    )

    # Create three customer threads
    t2 = threading.Thread(
        target=consumer,
        name='Customer-1'
    )

    t3 = threading.Thread(
        target=consumer,
        name='Customer-2'
    )

    t4 = threading.Thread(
        target=consumer,
        name='Customer-3'
    )

    # Start customer threads
    t2.start()
    t3.start()
    t4.start()

    # Start booking system
    t1.start()
    # Wait for producer to finish
    t1.join()
    # Wait for all tickets and stop signals to be processed
    ticket_queue.join()

    # Wait for customer threads to finish
    t2.join()
    t3.join()
    t4.join()
    logging.info('All bookings completed')

if __name__ == "__main__":
    main()