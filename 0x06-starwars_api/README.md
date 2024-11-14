# 0x06. Star Wars API 🌌

![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat-square&logo=javascript) ![API](https://img.shields.io/badge/API-Star_Wars-blue?style=flat-square&logo=api)

## 📖 Project Overview
In this project, you’ll create a script that interacts with the **Star Wars API** to fetch and display character names from a specified Star Wars movie. The objective is to demonstrate your skills in making HTTP requests, handling asynchronous operations, and managing command-line inputs in JavaScript.

## 🎯 Learning Objectives
- 🌐 **API Interaction**: Retrieve data from an external API and parse JSON responses.
- 🔄 **Asynchronous Programming**: Manage asynchronous calls with callbacks, promises, and `async/await`.
- 🖥️ **Command Line Arguments**: Access and process command-line arguments in Node.js.
- 📚 **Array Manipulation**: Iterate over and format data for output.

## 🛠️ Technologies Used
- ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat-square&logo=javascript) **JavaScript (ES6)**
- ![Node.js](https://img.shields.io/badge/Node.js-v10.14.x-green?style=flat-square&logo=node.js) **Node.js v10.14.x**
- **request module** for HTTP requests
- **semistandard** for code style (Airbnb style + semicolons)

## 📋 Requirements
- Files must be executable on **Ubuntu 20.04 LTS** using `node` (version 10.14.x).
- Files should start with `#!/usr/bin/node`.
- Code must be semistandard-compliant.
- Use `let` and `const` instead of `var`.
- Install and use the **request** module.

## 🚀 Installation

1. **Install Node.js v10**:
    ```bash
    curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```

2. **Install semistandard**:
    ```bash
    sudo npm install semistandard --global
    ```

3. **Install the request module**:
    ```bash
    sudo npm install request --global
    export NODE_PATH=/usr/lib/node_modules
    ```

4. **Clone the Repository**:
    ```bash
    git clone https://github.com/Alogyn/alx-interview
    cd alx-interview/0x06-starwars_api
    ```

## 📝 Task: Star Wars Characters 🌠

### Objective
Create a script, `0-starwars_characters.js`, that prints all character names of a Star Wars movie based on the provided Movie ID.

### Usage
```bash
./0-starwars_characters.js <Movie ID>
```

- **Movie ID:** A positional argument representing the ID of the movie. For example, 3 corresponds to Return of the Jedi.

### Example
```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
```

### Requirements
- Use the Star Wars API (https://swapi-api.hbtn.io/api/films/:id) to fetch data.
- Display each character name on a new line, maintaining the order provided by the API.
- request module is required for making HTTP requests.

## 🧠 Key Concepts and Techniques
- HTTP Requests in JavaScript: Using the request module to fetch data from external APIs.
- Asynchronous Operations: Managing API calls using callbacks, promises, and async/await.
- Command-Line Arguments: Accessing arguments with process.argv.
- Data Parsing and Display: Parsing JSON responses and iterating over arrays to display data.

## 🌐 Resources
- [A Guide to Making HTTP Requests in Node.js](https://www.memberstack.com/blog/node-http-request)
- [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- [Asynchronous JavaScript Guide](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
- [How to Parse Command Line Arguments in Node.js](https://tecadmin.net/how-to-parse-command-line-arguments-in-nodejs/#google_vignette)
- [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## ⚖️ License
This project is part of the ALX Software Engineering Program.
© 2024 ALX. All rights reserved.
