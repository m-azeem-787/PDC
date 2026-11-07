import logging
import threading
import time
import random

LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

print_queue = []
event = threading.Event()

class Printer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(2)

            # Wait until an employee submits a document
            event.wait()
            # Get the document from the queue
            document = print_queue.pop()

            logging.info(
                'Printer is printing: {} by {}'
                .format(document, self.name)
            )


class Employee(threading.Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(5):
            time.sleep(2)

            # Generate a document name
            document = 'Document-' + str(random.randint(100, 999)) + '.pdf'

            # Add document to the print queue
            print_queue.append(document)

            logging.info(
                'New print job: {} submitted by {}'
                .format(document, self.name)
            )

            # Notify the printer
            event.set()

            # Reset the notification
            event.clear()


if __name__ == "__main__":

    t1 = Employee(name='Employee')
    t2 = Printer(name='Printer')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
