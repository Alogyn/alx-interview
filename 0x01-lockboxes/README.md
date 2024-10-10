# 0x01. Lockboxes 🔐

Welcome to the **Lockboxes** project, part of the ALX Interview Preparation curriculum. In this project, you'll use your algorithmic skills to determine if all boxes in a list can be unlocked. You’ll apply concepts such as list manipulation, graph theory, recursion, and set operations to create an efficient solution.

## 📝 Learning Objectives

By completing this project, you will:

- 🔑 **Understand List Manipulation:** Learn how to access, iterate over, and modify lists dynamically in Python.
- 🌐 **Apply Graph Theory Concepts:** Explore how boxes and keys can be represented as nodes and edges in a graph, making traversal algorithms useful.
- 🧠 **Optimize Algorithm Complexity:** Understand how to measure and optimize time and space complexity using Big O notation.
- ♻️ **Work with Recursion:** Implement recursive solutions to traverse through boxes and keys efficiently.
- 📚 **Use Queues and Stacks:** Understand when to use data structures such as queues and stacks for breadth-first and depth-first search algorithms.
- ⚡ **Utilize Set Operations:** Efficiently track visited boxes and available keys using sets.

## 📂 Project Structure

This project includes the following:

### **Task 0: Lockboxes**  
   - **File:** [0-lockboxes.py](./0-lockboxes.py)  
   - **Description:** Implement the `canUnlockAll` method, which determines if all boxes can be opened based on the keys found in each box.
     - Prototype: `def canUnlockAll(boxes)`
     - **Input:** `boxes` is a list of lists, where each inner list represents a box containing keys to other boxes.
     - **Output:** Return `True` if all boxes can be opened, `False` otherwise.

## 🛠️ Example

```python
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False

## 📚 Resources

### Read or Watch:

- 📘 [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)
- 🎥 [Graph Theory Basics (Khan Academy)](https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:graph-theory)
- 📚 [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)
- 🧠 [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)
- 📦 [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/queue-in-python/)
- 🔗 [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html#sets)

## ⚙️ Setup Instructions

To get started with this project, follow these steps:

1. **Install Python**:
   - Make sure you have Python 3.4.3 or later installed on your system. If not, you can install it using the following command:
     ```bash
     sudo apt-get update
     sudo apt-get install python3
     ```

2. **Clone the repository**:
   - Clone this project to your local machine:
     ```bash
     git clone https://github.com/Alogyn/alx-interview.git
     cd alx-interview/0x01-lockboxes
     ```

3. **Make the script executable**:
   - Ensure that all your Python scripts are executable:
     ```bash
     chmod u+x *.py
     ```

4. **Run the code**:
   - You can test the code by running:
     ```bash
     ./main_0.py
     ```

## 🧑‍💻 Requirements

- Your code should be documented.
- Your code must follow the **PEP 8** style guidelines (version 1.7.x).
- All your files should be executable.

### Environment:

- All scripts will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.4.3**.

## 📜 License

This project is licensed under the terms of the [MIT License](https://opensource.org/licenses/MIT).

---

© 2024 [ALX](https://www.alxafrica.com/). All rights reserved.
