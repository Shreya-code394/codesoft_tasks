# 🧮 Simple Calculator – Python Internship Task

## 📌 Project Overview

This project is a **Simple Calculator** developed using Python. It performs basic arithmetic operations based on the user's input.

The calculator allows the user to enter two numbers and select an arithmetic operation. It then performs the selected calculation and displays the result.

This project was created as part of a **Python Internship Task** to practice basic Python programming concepts such as user input, conditional statements, arithmetic operators, and error handling.

---

## 🎯 Objective

The main objectives of this project are:

* Take two numbers as input from the user.
* Allow the user to select an arithmetic operation.
* Perform the selected calculation.
* Display the calculated result.
* Handle invalid choices.
* Prevent division by zero errors.

---

## ⚙️ Features

The calculator supports the following operations:

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* ⚠️ Division-by-zero error handling
* ❌ Invalid operation handling
* 🔢 Supports decimal numbers

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Code Editor:** Visual Studio Code
* **Interface:** Command Line / Terminal

---

## 📂 Project Structure

```text
Calculator/
│
├── calculator.py
└── README.md
```

---

## 💻 How to Run the Project

### Step 1: Clone or Download the Project

Download the project or clone the GitHub repository.

### Step 2: Open the Project in VS Code

Open the `Calculator` folder in Visual Studio Code.

### Step 3: Open the Terminal

In VS Code, go to:

**Terminal → New Terminal**

### Step 4: Run the Python File

Execute the following command:

```bash
python calculator.py
```

---

## 📝 How to Use

After running the program, enter two numbers.

Example:

```text
Enter first number: 20
Enter second number: 5
```

Then select an operation:

```text
Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)

Enter your choice (1/2/3/4): 1
```

Output:

```text
Result = 25.0
```

---

## 📊 Example Operations

| Choice | Operation      | Example | Result |
| ------ | -------------- | ------- | ------ |
| 1      | Addition       | 20 + 5  | 25     |
| 2      | Subtraction    | 20 - 5  | 15     |
| 3      | Multiplication | 20 × 5  | 100    |
| 4      | Division       | 20 ÷ 5  | 4      |

---

## 🧠 Python Concepts Used

This project demonstrates the following Python concepts:

* `input()` function
* `float()` data type conversion
* Variables
* Arithmetic operators
* `if-elif-else` conditional statements
* Nested conditions
* Error handling using conditional checks
* Console output using `print()`

---

## 🚨 Error Handling

The program handles division by zero.

For example:

```text
Enter first number: 10
Enter second number: 0
Enter your choice (1/2/3/4): 4

Error: Cannot divide by zero.
```

It also handles invalid operation choices:

```text
Enter your choice (1/2/3/4): 7

Invalid choice! Please select 1, 2, 3, or 4.
```

---

## 📸 Sample Output

```text
===== SIMPLE CALCULATOR =====

Enter first number: 15
Enter second number: 3

Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)

Enter your choice (1/2/3/4): 4

Result = 5.0
```

---

## 🚀 Future Improvements

The calculator can be improved by adding:

* Continuous calculations without restarting the program.
* Modulus operation (`%`).
* Power operation (`**`).
* Square root calculation.
* A graphical user interface (GUI).
* Calculation history.
* Better input validation.

---

## 👩‍💻 Author

**Shreya Lanjewar**

### Python Internship Task

This project was developed to strengthen basic Python programming and problem-solving skills.

---

## 📄 License

This project is created for educational and internship purposes.
