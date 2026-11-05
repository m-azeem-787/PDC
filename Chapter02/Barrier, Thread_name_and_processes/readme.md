# Parallel Image Processing Using Python Threads and Barrier

## Overview

This project demonstrates Python multithreading and synchronization using the `threading` module.

An actual image is divided into three horizontal sections, and each section is assigned to a separate thread. Each thread converts its assigned section into grayscale independently.

A **Barrier** is used to synchronize the three threads, ensuring that all threads complete their processing stage before continuing. Finally, the processed sections are combined to display the complete grayscale image.

## Features

- Loads and displays an actual image using Pillow.
- Splits the image into three horizontal sections.
- Assigns each section to a separate thread.
- Processes all three sections concurrently.
- Uses `threading.Barrier(3)` for thread synchronization.
- Combines the processed sections in their original order.
- Displays the final grayscale image using Matplotlib.
- Measures the total execution time.

## Technologies Used

- **Python** – Main programming language.
- **Threading** – Creates and manages multiple threads.
- **Barrier** – Synchronizes threads at a common point.
- **Pillow (PIL)** – Opens, splits, crops, and processes images.
- **Matplotlib** – Displays the original, split, and processed images.

## Project Structure

```text
Parallel-Image-Processing/
│
├── Thread_name_and_processes.py
├── HighRes.jpg
└── README.md
```

## Requirements

Install the required Python libraries:

```bash
pip install pillow matplotlib
```

## How It Works

### 1. Image Loading
The program loads `HighRes.jpg` and displays the original image.

### 2. Image Splitting
The image is divided into three horizontal sections:

- Section 0 – Top portion
- Section 1 – Middle portion
- Section 2 – Bottom portion

The three sections are displayed before processing begins.

### 3. Thread Creation
Three threads are created using a custom class `MyThreadClass`, which inherits from Python's `Thread` class.

Each thread receives:
- A thread name.
- Its section number.
- Its assigned image section.

### 4. Parallel Image Processing
Each thread executes its `run()` method and converts its assigned image section into grayscale using:

```python
grayscale_section = self.section.convert("L")
```

### 5. Barrier Synchronization
The program uses:

```python
processing_barrier = Barrier(3)
```

Each thread reaches the following synchronization point after completing its processing:

```python
processing_barrier.wait()
```

The threads wait until all three have reached the barrier. Once all threads arrive, they are released and continue execution.

### 6. Combining the Image
After all threads finish, the main thread retrieves the processed sections and combines them into one complete grayscale image.

### 7. Final Output
Matplotlib displays the final grayscale image. The program also prints the total processing time.
<img width="755" height="217" alt="image" src="https://github.com/user-attachments/assets/539ebd06-f2ab-44e0-9f0b-a2663d23a972" />
<img width="389" height="410" alt="image" src="https://github.com/user-attachments/assets/e505dc23-335a-4102-91eb-de3d2eeabfe5" />


## How to Run

1. Clone or download this repository.
2. Place your image in the same directory as the Python script.
3. Make sure the image is named `HighRes.jpg`, or update the filename in the code.
4. Install the required libraries.
5. Run the program:

```bash
python File.py
```
