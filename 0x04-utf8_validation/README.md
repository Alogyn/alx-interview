# 0x04. UTF-8 Validation 🧑‍💻

![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) ![Algorithm](https://img.shields.io/badge/Algorithm-UTF--8_Validation-lightgrey?style=flat-square&logo=python)

## 📖 Project Overview
This project focuses on validating UTF-8 encoding using bitwise operations, UTF-8 encoding rules, and Python programming. The goal is to determine if a given dataset correctly represents UTF-8 encoded data.

## 🎯 Learning Objectives
- 💡 **Bitwise Operations**: Use bitwise manipulation for handling data at the byte level.
- 📜 **UTF-8 Encoding Scheme**: Understand the structure of UTF-8 encoding for 1-4 byte characters.
- 🗂️ **Data Representation**: Efficiently represent data at the byte level.
- 🔄 **Boolean Logic**: Apply logical reasoning to validate encoding patterns.

## 🛠️ Technologies Used
- ![Python](https://img.shields.io/badge/Python-3.4.3-blue?style=flat-square&logo=python) **Python 3.4.3** on **Ubuntu 20.04 LTS**
- **PEP 8** style guide (version 1.7.x) for clean and readable code

## 📋 Requirements
- Python files are interpreted on **Ubuntu 20.04 LTS** using `python3` (version 3.4.3).
- Each file should end with a new line and start with `#!/usr/bin/python3`.
- Code must follow the **PEP 8** style guide.
- Ensure all files are executable.

## 🚀 Concepts Needed
- **Bitwise Operations**:
  - Understanding AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and shifts (`<<`, `>>`).
- **UTF-8 Encoding Scheme**:
  - Understanding how characters are represented in 1-4 bytes.
  - Recognizing valid UTF-8 patterns.
- **Data Representation**:
  - Handling the least significant bits (LSB) of integers to simulate byte-level data.
- **List Manipulation in Python**:
  - Iterating, accessing elements, and using list comprehensions.
- **Boolean Logic**:
  - Applying logical conditions to validate data.

## 📝 Task

### 0. UTF-8 Validation
- **Objective**: Write a method to check if a data set represents a valid UTF-8 encoding.
- **Prototype**: `def validUTF8(data: List[int]) -> bool`
- **Return**: `True` if `data` is valid UTF-8; otherwise, `False`
  
#### Example
```python
data = [65]
print(validUTF8(data)) # True

data = [229, 65, 127, 256]
print(validUTF8(data)) # False
```

## 📂 Project Structure
`0-validate_utf8.py`: Contains the UTF-8 validation function.
`0-main.py`: Test file to validate the implementation.

## ⚙️ How to Run
1. Clone the repository:
```bash
git clone https://github.com/Alogyn/alx-interview
cd alx-interview/0x04-utf8_validation#
```
2. Run the test file:
```bash
./0-main.py
```

## 🌐 Resources
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Bitwise Operators in Python](https://docs.python.org/3.4/library/stdtypes.html#bitwise-operations-on-integer-types)

## 👤 Author
Mohamed Derfoufi
📧 mohamed.derfoufi.tech@gmail.com | 🌐 [Linkdin](https://www.linkedin.com/in/mohamed-derfoufi-b50566309/)
