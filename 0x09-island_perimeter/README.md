# 0x09. Island Perimeter 🌴

![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) ![Algorithm](https://img.shields.io/badge/Algorithm-Grid_Traversal-lightgrey?style=flat-square&logo=python)

## 📖 Project Overview
In this project, you’ll implement a function to calculate the **perimeter of an island** represented in a 2D grid. The challenge requires iterating over the grid, identifying land cells (`1`), and determining their contribution to the total perimeter based on adjacency rules.

## 🎯 Learning Objectives
- 🌊 **Grid Navigation**: Traverse 2D arrays and analyze neighboring cells.
- 🧮 **Conditional Logic**: Apply logic to determine perimeter contributions.
- 🚀 **Algorithmic Thinking**: Break down the problem into manageable tasks.
- 🖥️ **Python Programming**: Use nested loops and conditional statements effectively.

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
    cd alx-interview/0x09-island_perimeter
    ```

2. **Run the Script**:
    ```bash
    ./0-main.py
    ```

## 📝 Task: Island Perimeter 🌴

### Objective
Write a function, `island_perimeter`, that calculates the perimeter of an island in a 2D grid.

### Function Prototype
```python
def island_perimeter(grid):
```
- **Arguments**:
    - `grid`: A list of lists of integers, where:
        - `0` represents water.
        - `1` represents land.
- **Returns**:
    - An integer representing the perimeter of the island.

### Rules
- Each cell is square, with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- The grid is rectangular, with a width and height not exceeding `100`.
- The island:
    - Is completely surrounded by water.
    - Contains no internal lakes.

### Example
- Input Grid:
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

- Output:
```python
12
```

### Example Output
```bash
$ ./0-main.py
12
```

### Notes
- A land cell contributes `4` to the perimeter by default.
- For each adjacent land cell, subtract `1` from the perimeter.

## 🧠 Key Concepts and Techniques
- **Grid Navigation**:
    - Use nested loops to iterate through rows and columns.
    - Check adjacent cells for land (`1`) or water (`0`).
- **Perimeter Calculation**:
    - Add `4` for each land cell.
    - Subtract `1` for each adjacent land cell.
- **Efficiency**:
    - Optimize for grids up to `100 x 100` in size.

## 🌐 Resources
- **Python Official Documentation**:
    - [Nested Lists](https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions): Understanding how to work with lists within lists in Python.
- **GeeksforGeeks Articles**:
    - [Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/): A guide to working with 2D arrays in Python effectively.
- **TutorialsPoint**:
    - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.
- **YouTube Tutorials**:
    - [Python 2D arrays and lists](https://www.youtube.com/watch?feature=shared&v=aNzepGawwCI)

## 🌐 Additional Resources
- [Mock Technical Interviews](https://www.youtube.com/watch?feature=shared&v=fFgEM6CMQc4)

## ⚖️ License
This project is part of the ALX Software Engineering Program.  
© 2024 ALX. All rights reserved.
