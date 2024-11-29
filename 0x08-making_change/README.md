# 0x08. Making Change 💰

![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) ![Algorithm](https://img.shields.io/badge/Algorithm-Dynamic_Programming-lightgrey?style=flat-square&logo=python)

## 📖 Project Overview
This project involves solving the **coin change problem**, a classic challenge in algorithms. The objective is to determine the minimum number of coins required to meet a given amount using the provided denominations. This task allows you to apply **greedy algorithms** and **dynamic programming** to develop efficient solutions for optimization problems.

## 🎯 Learning Objectives
- 💡 **Greedy Algorithms**: Understand and apply a greedy approach to solve the problem efficiently in certain cases.
- 🧩 **Dynamic Programming**: Utilize overlapping subproblems and optimal substructure to implement a robust solution.
- 🚀 **Algorithm Optimization**: Analyze and improve the time and space complexity of your solution.
- 🖥️ **Python Programming**: Write concise and efficient Python code using loops, conditionals, and list manipulations.

## 🛠️ Technologies Used
- ![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) **Python 3.4.3** on **Ubuntu 20.04 LTS**
- **PEP 8** (v1.7.x) for code style and formatting

## 📋 Requirements
- Files must run on **Ubuntu 20.04 LTS** using `python3` (version 3.4.3).
- Files should start with `#!/usr/bin/python3`.
- Code must adhere to **PEP 8** standards.
- Functions and modules must be documented.
- No external libraries or modules may be imported.

## 🚀 Installation and Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Alogyn/alx-interview
    cd alx-interview/0x08-making_change
    ```

2. **Run the Script**:
    ```bash
    ./0-main.py
    ```

## 📝 Task: Change Comes from Within 💡

### Objective
Write a function, `makeChange`, to determine the minimum number of coins needed to meet a given total.

### Function Prototype
```python
def makeChange(coins, total):
```
- **Arguments**:
  - `coins`: A list of integers representing coin denominations.
  - `total`: An integer representing the target amount.
- **Returns**:
  - The minimum number of coins needed to meet the total.
  - If the total is `0` or less, return `0`.
  - If it’s not possible to meet the total, return `-1`.

### Example Usage
**Input**:
```python
print(makeChange([1, 2, 25], 37))   # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))   # Output: -1
```

**Output**:
```bash
$ ./0-main.py
7
-1
```

### Notes
- Assume infinite availability of each coin denomination.
- The runtime of your solution will be evaluated.

## 🧠 Key Concepts and Techniques
- **Greedy Algorithms**:
  - Attempt to choose the largest denomination first.
  - Suitable when denominations allow for a greedy approach to produce the optimal solution.
- **Dynamic Programming**:
  - Solve using subproblem recursion.
  - Track minimum coins required for each sub-total iteratively.
- **Algorithmic Complexity**:
  - Aim for optimal time and space complexity to handle large inputs efficiently.

## 🌐 Resources
- **Python Official Documentation**:
  - [More Control Flow Tools (for loops, if statements)](https://docs.python.org/3/tutorial/controlflow.html)

- **GeeksforGeeks Articles**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

- **YouTube Tutorials**:
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jgiZlGzXMBw) for a visual and step-by-step explanation of the dynamic programming approach.

## 🌐 Additional Resources
- [Mock Technical Interview](https://www.youtube.com/watch?v=9BSSIsJ-fWg)

## ⚖️ License
This project is part of the ALX Software Engineering Program.
© 2024 ALX. All rights reserved.
