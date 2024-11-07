# 0x02. Minimum Operations ⚙️

![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) ![Algorithm](https://img.shields.io/badge/Algorithm-Dynamic_Programming-lightgrey?style=flat-square&logo=python)

## 📖 Project Overview
This project tackles the **Minimum Operations** problem, where the goal is to determine the smallest number of "Copy All" and "Paste" operations required to reach exactly `n` characters in a text file that starts with a single character 'H'. This problem provides a great opportunity to apply **dynamic programming**, **greedy algorithms**, and **prime factorization** concepts for optimization.

## 🎯 Learning Objectives
- 🧩 **Dynamic Programming**: Learn to solve complex problems by breaking them into simpler subproblems.
- 🔍 **Prime Factorization**: Utilize prime factorization to reduce the problem complexity.
- ⚙️ **Greedy & Optimization Techniques**: Find the most efficient solution by making optimal choices at each step.

## 🛠️ Technologies Used
- ![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) **Python 3.4.3** on **Ubuntu 20.04 LTS**
- **PEP 8** (v1.7.x) for code style and formatting

## 📋 Requirements
- Files should be interpreted on **Ubuntu 20.04 LTS** using `python3` (version 3.4.3).
- Each file should start with `#!/usr/bin/python3`.
- All code should conform to **PEP 8** standards.
- All files must be executable.
- Include comprehensive documentation for all modules, classes, and functions.

## 🚀 Installation and Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Alogyn/alx-interview
    cd alx-interview/0x02-minimum_operations
    ```

2. **Run the Program**:
    ```bash
    ./0-main.py
    ```

## 📝 Task: Minimum Operations ⚙️
### Objective
Write a function `minOperations(n)` to compute the minimum number of operations needed to end up with exactly `n` characters in a file containing a single character `H`.

### Function Prototype
```python
def minOperations(n: int) -> int
```

### Returns
- The integer count of operations if n is possible, otherwise returns 0.

### Example
```python
# Example usage:
n = 9
# H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
# Number of operations: 6

print(minOperations(9))  # Output: 6
```

### Example Output
```bash
$ ./0-main.py
Min # of operations to reach 4 characters: 4
Min # of operations to reach 12 characters: 7
```

## 🧠 Key Concepts and Techniques
- **Dynamic Programming:** Helps in building the solution by solving overlapping subproblems.
- **Prime Factorization:** Reduces the solution to the sum of the prime factors of n.
- **Greedy Algorithms:** Choose optimal steps for minimal operations.

## 🌐 Resources
- [Dynamic Programming Guide](https://www.geeksforgeeks.org/dynamic-programming/)
- [Prime Factorization](https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-factorization-prealg/v/prime-factorization)
- [Greedy Algorithms](https://www.geeksforgeeks.org/greedy-algorithms/)

## ⚖️ License
This project is part of the ALX Software Engineering Program.
© 2024 ALX. All rights reserved.
