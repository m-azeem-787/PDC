
import time
import os
from random import randint
from threading import Thread

class MyThreadClass(Thread):
    def __init__(self, name, duration):
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        print("---> Downloading " + self.name +
              " | Process ID: " + str(os.getpid()))

        # Simulate download time
        time.sleep(self.duration)
        print("---> " + self.name + " downloaded successfully!")

def main():
    start_time = time.time()

    # Files to download
    files = [
        "Report.pdf",
        "Assignment.docx",
        "Image.png",
        "Video.mp4",
        "Presentation.pptx",
        "Music.mp3",
        "Data.xlsx",
        "Project.zip",
        "Research.pdf"
    ]

    threads = []

    # Thread Creation
    for file in files:
        duration = randint(1, 10)
        thread = MyThreadClass(file, duration)
        threads.append(thread)

    # Thread Running
    for thread in threads:
        thread.start()

    # Thread Joining
    for thread in threads:
        thread.join()

    print("\nAll files downloaded successfully!")

    # Execution Time
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
