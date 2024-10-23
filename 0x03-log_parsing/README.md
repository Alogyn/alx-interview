# 0x03. Log Parsing 📄

Welcome to the **Log Parsing** project! This project is part of the ALX Interview Preparation curriculum. It focuses on reading data from stdin in real-time, parsing log entries, and computing metrics from the processed data.

## 📝 Learning Objectives

By completing this project, you will:

- 📜 **File I/O in Python:** Learn how to read from `sys.stdin` line by line.
- 🛠️ **Signal Handling:** Handle keyboard interruption (CTRL + C) using Python signals.
- 📊 **Data Processing:** Parse strings to extract data and compute summaries.
- 🔍 **Regular Expressions:** Use regex to validate and process log format.
- 🧮 **Dictionaries in Python:** Count occurrences of status codes and aggregate file sizes.
- ❗ **Exception Handling:** Learn how to handle possible exceptions during data parsing.

## 📚 Concepts

To complete this project successfully, you'll need to be familiar with these concepts:

- **File I/O in Python:** [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- **Signal Handling in Python:** [Python Signal Handling](https://docs.python.org/3/library/signal.html)
- **Data Processing:** Parsing and aggregating log data.
- **Regular Expressions:** [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- **Dictionaries in Python:** [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- **Exception Handling:** [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

## 📂 Project Structure

This project includes the following tasks:

- **Task 0: Log Parsing**  
   - **File:** [0-stats.py](./0-stats.py)  
   - **Description:** A Python script that reads stdin line by line and computes metrics.  
   - **Input Format:**  
     ```
     <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
     ```
   - **Output:** After every 10 lines or keyboard interruption, print:  
     ```
     Total file size: <total size>
     <status code>: <number>
     ```
     where `<total size>` is the sum of all previous `<file size>`. Status codes should be printed in ascending order.

## ⚙️ Setup Instructions

1. **Install Python3 on Ubuntu 20.04**:  
   If you don't already have Python installed, use the following commands:
   ```bash
   sudo apt update
   sudo apt install python3
   python3 --version
   ```

2. **Clone the repository:**
   Clone this project to your local machine:
   ```bash
   git clone https://github.com/Alogyn/alx-interview/0x03-log_parsing
   cd alx-interview/0x03-log_parsing
   ```

3. **Make the script executable:**
   Ensure your script has execute permissions:
   ```bash
   chmod +x 0-stats.py
   ```

4. **Running the script:**
   You can use a generator script to create log entries and pipe them into your script:
   ```bash
   ./0-generator.py | ./0-stats.py
   ```

## 🧪 Example Test Case

The following example demonstrates how the script behaves when parsing logs from stdin:

```bash
alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
alexa@ubuntu:~/0x03-log_parsing$
```

## 💡 Additional Resources

- Mock Technical Interview: Practice technical interviews by using the log parsing concept and similar algorithms to prepare for real-time problem-solving scenarios.
- PEP 8 Style Guide: [PEP 8](https://peps.python.org/pep-0008/) – Style guide for Python code.

## 📜 License

This project is licensed under the terms of the [MIT License](https://opensource.org/licenses/MIT).

---

© 2024 [ALX](https://www.alxafrica.com/). All rights reserved.
