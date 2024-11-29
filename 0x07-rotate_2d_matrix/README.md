# 0x07. Rotate 2D Matrix 🔄

![Python](https://img.shields.io/badge/Python-3.8.10-blue?style=flat-square&logo=python) ![Algorithm](https://img.shields.io/badge/Algorithm-Matrix_Manipulation-lightgrey?style=flat-square&logo=python)

## 📖 Project Overview
This project focuses on implementing an **in-place** algorithm to rotate an `n x n` 2D matrix by **90 degrees clockwise**. The task challenges you to understand and apply concepts like matrix transposition, reversing rows, and optimizing in-place operations in Python.

## 🎯 Learning Objectives
- 🧩 **Matrix Manipulation**: Learn to handle 2D data structures in Python effectively.
- 🚀 **In-place Operations**: Minimize space complexity by modifying the matrix directly.
- 🔄 **Matrix Transposition and Row Reversal**: Master the two-step process for rotating a matrix.

## 🛠️ Technologies Used
- ![Python](https://img.shields.io/badge/Python-3.8.10-blue?style=flat-square&logo=python) **Python 3.8.10** on **Ubuntu 20.04 LTS**
- **Pycodestyle** (v2.8.0) for code style and formatting

## 📋 Requirements
- Files must run on **Ubuntu 20.04 LTS** using `python3` (version 3.8.10).
- Files should start with `#!/usr/bin/python3`.
- Code must adhere to **Pycodestyle** standards.
- No external modules may be imported.
- Functions and modules must be documented.

## 🚀 Installation and Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Alogyn/alx-interview
    cd /alx-interview/0x07-rotate_2d_matrix
    ```

2. **Run the Script**:
    ```bash
    ./main_0.py
    ```

## 📝 Task: Rotate 2D Matrix 🔄

### Objective
Rotate an `n x n` 2D matrix **90 degrees clockwise** **in-place** without returning anything.

### Function Prototype
```python
def rotate_2d_matrix(matrix):
```
- **Input**: A 2D matrix represented as a list of lists.
- **Output**: None. The matrix is rotated in-place.
- **Assumptions**:
    - The matrix will always be 2-dimensional and non-empty.
### Example
**Input**:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
**Output**:
```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```
###Steps to Rotate
1. Transpose the Matrix:
- Swap rows with columns.
```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
→ 
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```
2. Reverse Each Row:
- Reverse the elements in each row.
```python
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
→ 
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```
## 🌐 Resources
- **Python Official Documentation**:
    - [Data Structures (list comprehensions, nested list comprehension)](https://docs.python.org/3/tutorial/datastructures.html)
    - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- **GeeksforGeeks Articles**:
    - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
    - [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)
- **TutorialsPoint**:
    - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm) for basics of list manipulation in Python.

## 🌐Additional Resources
- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=yM9Xbi-MigE)

## ⚖️ License
This project is part of the ALX Software Engineering Program.
© 2024 ALX. All rights reserved.
