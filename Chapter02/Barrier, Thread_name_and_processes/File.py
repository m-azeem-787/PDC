
from PIL import Image
from threading import Barrier, Thread
from time import sleep
import matplotlib.pyplot as plt
import time
import os

num_workers = 3

# Barrier for 3 worker threads
processing_barrier = Barrier(num_workers)

# Store processed image sections
processed_sections = {}

# Thread Class
class MyThreadClass(Thread):

    def __init__(self, name, section_number, section):
        Thread.__init__(self)

        self.name = name
        self.section_number = section_number
        self.section = section

    # Each thread executes this method
    def run(self):

        print("Process ID: {}".format(os.getpid()))
        print("{}: Processing started".format(self.name))

        # Convert assigned section to grayscale
        grayscale_section = self.section.convert("L")

        # Simulate processing time
        sleep(2)
        # Store processed section
        processed_sections[self.section_number] = grayscale_section
        print("{}: Processing completed".format(self.name))

        # Wait until all 3 threads finish processing
        processing_barrier.wait()
        print("{}: Passed the barrier".format(self.name))


def main():

    start_time = time.time()

    image = Image.open("HighRes.jpg").convert("RGB")
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

    width, height = image.size
    section_height = height // num_workers

    sections = []

    print("IMAGE PROCESSING STARTED")

    # Split image into 3 horizontal sections
    for i in range(num_workers):
        top = i * section_height

        # Include remaining pixels in the last section
        bottom = (
            height if i == num_workers - 1
            else (i + 1) * section_height
        )

        section = image.crop((0, top, width, bottom))
        sections.append(section)

        print("Image split: Section {}".format(i))

    # Display split sections
    fig, axes = plt.subplots(1, num_workers, figsize=(12, 4))

    for i, section in enumerate(sections):
        axes[i].imshow(section)
        axes[i].set_title("Section {}".format(i))
        axes[i].axis("off")

    plt.suptitle("Image Split into 3 Sections")
    plt.tight_layout()
    plt.show()

    # Thread Creation
    thread1 = MyThreadClass("Thread#1", 0, sections[0])
    thread2 = MyThreadClass("Thread#2", 1, sections[1])
    thread3 = MyThreadClass("Thread#3", 2, sections[2])

    # Thread Running
    thread1.start()
    thread2.start()
    thread3.start()

    # Thread Joining
    thread1.join()
    thread2.join()
    thread3.join()

    # Combine processed sections
    final_image = Image.new("L", (width, height))

    for i in range(num_workers):
        top = i * section_height
        final_image.paste(processed_sections[i], (0, top))

    # Display final grayscale image
    plt.figure(figsize=(8, 6))
    plt.imshow(final_image, cmap="gray")
    plt.title("Final Grayscale Image")
    plt.axis("off")
    plt.show()

    end_time = time.time()

    print("All sections combined successfully!")
    print("Total processing time: {:.2f} seconds".format(
        end_time - start_time
    ))
    print("End")

if __name__ == "__main__":
    main()
