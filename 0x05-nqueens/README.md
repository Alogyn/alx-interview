# 0x05. N Queens ♛

![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) ![Algorithm](https://img.shields.io/badge/Algorithm-Backtracking-lightgrey?style=flat-square&logo=python)

## 📖 Project Overview
The **N Queens** problem is a classic algorithmic challenge of placing `N` non-attacking queens on an `N×N` chessboard. This project involves using backtracking to explore and print all possible solutions, helping you strengthen your understanding of recursion and algorithmic optimization.

## 🎯 Learning Objectives
- ♻️ **Backtracking**: Use backtracking to explore solution paths and revert when necessary.
- 🔄 **Recursion**: Leverage recursion to handle repeated function calls and explore solution spaces.
- 📋 **List Manipulations**: Store and track the position of queens on the chessboard.
- 🖥️ **Command Line Arguments**: Manage input arguments using Python’s `sys` module.

## 🛠️ Technologies Used
- ![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) **Python 3.4.3** on **Ubuntu 20.04 LTS**
- **PEP 8** (v1.7.*) for code style and formatting

## 📋 Requirements
- Files must run on **Ubuntu 20.04 LTS** using `python3` (version 3.4.3).
- Files should start with `#!/usr/bin/python3`.
- Code should conform to **PEP 8** standards.
- Ensure all files are executable and contain complete documentation.

## 🚀 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Alogyn/alx-interview
    cd alx-interview/0x05-nqueens
    ```

2. Run the program:
    ```bash
    ./0-nqueens.py N
    ```
   Replace `N` with the desired board size (an integer ≥ 4).

## 📝 Task Breakdown

### N Queens Challenge ♛:
- **Goal**: Write a program to solve the N queens puzzle, ensuring each queen is placed such that no two queens attack each other.
- **Program Usage**: 
    ```bash
    nqueens N
    ```
- **Error Handling**:
  - If the number of arguments is incorrect, print: `Usage: nqueens N`.
  - If `N` is not an integer, print: `N must be a number`.
  - If `N` < 4, print: `N must be at least 4`.

- **Output**: Each solution is printed in a list format, with each list element representing the row and column position of a queen.

#### Example
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## 🧠 Key Concepts
- **Backtracking Algorithms:** Solve problems by exploring all solutions and discarding those that fail to meet requirements.
- **Recursion:** Efficiently explore solution paths with recursive calls.
- **Command-Line Input:** Handle user input through the command line using Python’s sys module.

## ⚖️ License
This project is licensed under the ALX Software Engineering Program.
© 2024 [ALX.](https://www.alxafrica.com/) All rights reserved.
