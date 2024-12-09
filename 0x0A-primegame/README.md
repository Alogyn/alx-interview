# 0x0A. Prime Game 🎲

![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) ![Algorithm](https://img.shields.io/badge/Algorithm-Game_Theory-lightgrey?style=flat-square&logo=python)

## 📖 Project Overview
In this project, you’ll implement a solution to a two-player game involving prime numbers. Maria and Ben take turns choosing a prime number and removing it along with its multiples from a set of consecutive integers. The challenge is to determine the winner across multiple rounds, assuming both players play optimally. This task combines concepts from **game theory**, **prime number algorithms**, and **dynamic programming**.

## 🎯 Learning Objectives
- 🧮 **Prime Numbers**: Understand and implement efficient algorithms for identifying prime numbers.
- ♻️ **Sieve of Eratosthenes**: Use the sieve algorithm to precompute prime numbers for optimization.
- 🎮 **Game Theory**: Analyze turn-based games and determine strategies for optimal play.
- 🚀 **Dynamic Programming**: Use memoization or caching to optimize repeated calculations.

## 🛠️ Technologies Used
- ![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) **Python 3.4.3** on **Ubuntu 20.04 LTS**
- **PEP 8** (v1.7.x) for code style and formatting

## 📋 Requirements
- Files must run on **Ubuntu 20.04 LTS** using `python3` (version 3.4.3).
- Files should start with `#!/usr/bin/python3`.
- Code must adhere to **PEP 8** standards.
- No external libraries or modules may be imported.
- Functions and modules must be documented.

## 🚀 Installation and Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Alogyn/alx-interview
    cd alx-interview/0x0A-primegame
    ```

2. **Run the Script**:
    ```bash
    ./main_0.py
    ```

## 📝 Task: Prime Game 🎲

### Objective
Write a function, `isWinner`, to determine the winner of a series of rounds in the prime game.

### Function Prototype
```python
def isWinner(x, nums):
```

- Arguments:
  - `x`: The number of rounds to be played.
  - `nums`: A list of integers representing the maximum number for each round.

- Returns:
  - The name of the player with the most wins ("`Maria`" or "`Ben`").
  - `None` if there is no clear winner.

### Example
- Input:
```python
x = 3
nums = [4, 5, 1]
```

Output:
```python
"Ben"
```

- Explanation:
  - **Round 1** (n = 4): Ben wins.
  - **Round 2** (n = 5): Maria wins.
  - **Round 3** (n = 1): Ben wins.
  - Result: Ben wins 2 rounds, Maria wins 1.

### Example Output
```bash
$ ./main_0.py
Winner: Ben
```

## 🧠 Key Concepts and Techniques
- Prime Numbers:
  - Identify primes using efficient methods like the Sieve of Eratosthenes.
- Game Theory:
  - Analyze turn-based games and simulate optimal strategies.
- Dynamic Programming:
  - Use caching or memoization to store results for repeated subproblems.
- Algorithm Complexity:
  - Optimize for both time and space complexity to handle large inputs.

## 🌐 Resources
- **Prime Numbers and Sieve of Eratosthenes**:
  - [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/cc-fourth-grade-math/imp-factors-multiples-and-patterns/imp-prime-and-composite-numbers/v/prime-numbers): Introduction to prime numbers.
  - [Sieve of Eratosthenes in Python](https://www.geeksforgeeks.org/sieve-of-eratosthenes/): A step-by-step guide to implementing the sieve algorithm in Python.
- **Game Theory Basics**:
  - [Game Theory Introduction](https://www.investopedia.com/terms/g/gametheory.asp): A simple explanation of game theory and strategic decision-making.
- **Dynamic Programming**:
  - [What Is Dynamic Programming With Python Examples](https://skerritt.blog/dynamic-programming/): An introduction to dynamic programming with Python examples.
- **Python Official Documentation**:
  - [Python Lists](https://docs.python.org/3/tutorial/introduction.html#lists): Managing lists in Python, useful for tracking the game state.

## 🌐 Additional Resources
- [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=Jw2pniZCLi8)

## ⚖️ License
This project is part of the ALX Software Engineering Program.  
© 2024 ALX. All rights reserved.
