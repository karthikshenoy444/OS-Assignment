# Python Multithreading Programs

This repository contains two Python programs demonstrating **multithreading, synchronization, and concurrent processing** using Python.

## 📌 Programs Included

### 1. Producer-Consumer Problem

This program demonstrates the classic **Producer-Consumer problem** using Python's `threading.Condition`.

The producer generates items and places them into a shared buffer, while the consumer removes and processes those items.

#### Concepts Used

* Python `threading`
* `Condition`
* Thread synchronization
* Shared buffer
* Producer-Consumer problem
* `wait()` and `notify_all()`
* Thread creation and joining

#### How It Works

* The buffer can store a maximum of **5 items**.
* The producer creates **15 items**.
* If the buffer is full, the producer waits.
* If the buffer is empty, the consumer waits.
* `Condition` is used to coordinate the producer and consumer.
* `notify_all()` wakes up waiting threads when the buffer state changes.

#### Example Output

```text
[Producer-1] produced Producer-1-item0 (buffer size: 1)
[Consumer-1] consumed Producer-1-item0 (buffer size: 0)
[Producer-1] produced Producer-1-item1 (buffer size: 1)
[Consumer-1] consumed Producer-1-item1 (buffer size: 0)
...
All items produced and consumed. Done.
```

---

### 2. Multithreaded Matrix Multiplication

This program demonstrates **parallel matrix multiplication** using multiple threads.

A `100 × 100` matrix is multiplied by another `100 × 100` matrix. Each thread is assigned a set of rows to calculate.

The program also provides a **real-time visualization** of the computation using Matplotlib.

#### Concepts Used

* Python `threading`
* NumPy
* Matrix multiplication
* Parallel processing
* Thread synchronization
* `Lock`
* Matplotlib
* Real-time animation
* Progress visualization

#### How It Works

1. Two random `100 × 100` matrices are generated.
2. The rows are randomly shuffled.
3. The rows are divided among **8 worker threads**.
4. Each thread calculates its assigned rows.
5. A `Lock` protects the shared result matrix and progress variables.
6. Matplotlib displays the matrices and updates the result as rows are completed.
7. A progress bar shows how many rows have been calculated.

#### Visualization

The program displays:

* **Left Matrix** – First input matrix
* **Right Matrix** – Second input matrix
* **Result Matrix** – Rows being calculated by different threads
* **Progress Bar** – Number of completed rows

---

## 🛠️ Requirements

Make sure Python is installed on your system.

Install the required libraries using:

```bash
pip install numpy matplotlib
```

The following modules are part of Python's standard library and do not need separate installation:

```text
threading
time
random
```

---

## 📂 Project Structure

```text
Python-Multithreading/
│
├── producer_consumer.py
├── matrix_multiplication.py
└── README.md
```

You can rename the Python files according to your preference.

---

## ▶️ How to Run

### Producer-Consumer

```bash
python producer_consumer.py
```

### Matrix Multiplication

```bash
python matrix_multiplication.py
```

The matrix multiplication program will open a graphical window showing the real-time computation.

---

## 🧠 Key Learning Outcomes

Through these programs, the following concepts can be understood:

* Creating and managing threads
* Synchronizing multiple threads
* Handling shared resources
* Using `Condition` for thread communication
* Using `Lock` to prevent race conditions
* Dividing computational work between threads
* Understanding concurrent execution
* Visualizing multithreaded computation

---

## ⚙️ Technologies Used

* **Python**
* **NumPy**
* **Matplotlib**
* **Python Threading**

---

## 📚 Conclusion

These programs provide practical demonstrations of **multithreading and synchronization in Python**.

The Producer-Consumer program focuses on communication and synchronization between threads, while the Matrix Multiplication program demonstrates how computational work can be divided among multiple worker threads and visualized in real time.
