# 📝 To-Do List Application

## 📌 Project Overview

The **To-Do List Application** is a simple command-line application developed using Python. It helps users manage their daily tasks efficiently by allowing them to add, view, update, complete, and delete tasks.

This project was developed as part of a **Python Internship Task** to demonstrate basic Python programming concepts and logical problem-solving skills.

---

## 🎯 Features

* ➕ Add new tasks
* 📋 View all tasks
* ✏️ Update existing tasks
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* 🚪 Exit the application
* ⚠️ Input validation for invalid choices and task numbers

---

## 🛠️ Technologies Used

* **Python 3**
* **VS Code**
* Python Built-in Functions and Data Structures

No external Python libraries are required.

---

## 📂 Project Structure

```text
Todo_List_Project/
│
├── todo.py
└── README.md
```

---

## ⚙️ Requirements

Before running the project, make sure Python 3 is installed on your computer.

Check the Python version using:

```bash
python --version
```

or:

```bash
py --version
```

---

## ▶️ How to Run the Project

### Step 1: Clone or Download the Project

Download the project files to your computer.

### Step 2: Open the Project in VS Code

Open the `Todo_List_Project` folder in Visual Studio Code.

### Step 3: Open the Terminal

In VS Code, go to:

```text
Terminal → New Terminal
```

### Step 4: Run the Python Program

Use:

```bash
python todo.py
```

If that doesn't work, use:

```bash
py todo.py
```

---

## 💻 Application Menu

When the program starts, the following menu is displayed:

```text
============================
       TO-DO LIST APP
============================
1. Add Task
2. View Tasks
3. Update Task
4. Complete Task
5. Delete Task
6. Exit
============================
```

---

## 🧪 Example

### Add a Task

```text
Enter your choice: 1

Enter task: Complete Python Internship Task

Task added successfully!
```

### View Tasks

```text
Enter your choice: 2

----- YOUR TASKS -----

1. Complete Python Internship Task - Pending
```

### Complete a Task

```text
Enter your choice: 4

Enter task number to mark as completed: 1

Task marked as completed!
```

The task status will then become:

```text
1. Complete Python Internship Task - Completed
```

---

## 🧠 Python Concepts Used

This project demonstrates the following Python concepts:

* Variables
* Lists
* Dictionaries
* Functions
* `if-elif-else` statements
* `while` loops
* `for` loops
* User input
* Exception handling using `try-except`
* List methods such as `append()` and `pop()`
* `enumerate()`

---

## 📋 Project Workflow

```text
Start
  ↓
Display Menu
  ↓
Choose an Option
  ↓
Add / View / Update / Complete / Delete
  ↓
Display Result
  ↓
Return to Menu
  ↓
Exit
```

---

## 🚀 Future Improvements

The project can be further improved by adding:

* 💾 Permanent task storage using SQLite or JSON
* 🖥️ Graphical User Interface using Tkinter
* 📅 Task deadlines
* 🔔 Reminders and notifications
* 🔍 Search and filter options
* 📊 Task statistics
* 🎨 Improved user interface

---

## 👨‍💻 Author

**Shreya Lanjewar**

### Python Internship Project

---

## 📄 License

This project is created for educational and internship purposes.
