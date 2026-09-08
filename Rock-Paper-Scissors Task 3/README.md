# 🎮 Rock-Paper-Scissors Game — Task 3

## 📌 Project Overview

This project is a simple **Rock-Paper-Scissors Game** developed using Python as part of my internship Task 4.

The game allows the user to choose **Rock, Paper, or Scissors**, while the computer randomly selects one of the three choices. The program then compares both choices and determines the winner according to the standard game rules.

The game also includes **score tracking** and allows the user to play multiple rounds.

---

## 🎯 Objectives

The main objectives of this project are:

* To practice Python programming fundamentals.
* To work with user input.
* To use Python's `random` module.
* To implement conditional statements.
* To use loops for multiple rounds.
* To implement score tracking.
* To create an interactive command-line game.
* To handle invalid user input.

---

## 🕹️ Game Rules

The game follows these rules:

| User Choice | Beats       |
| ----------- | ----------- |
| 🪨 Rock     | ✂️ Scissors |
| ✂️ Scissors | 📄 Paper    |
| 📄 Paper    | 🪨 Rock     |

If both the user and computer select the same option, the result is a **Tie**.

---

## ✨ Features

* 🎮 Interactive command-line interface
* 🪨 Rock, Paper, and Scissors choices
* 🤖 Random computer selection
* 🏆 Automatic winner detection
* 🤝 Tie detection
* 📊 Score tracking
* 🔄 Multiple rounds
* ❌ Invalid input handling
* 🚪 Play Again option
* 🏅 Final score and overall winner

---

## 🛠️ Technologies Used

* **Python 3**
* **Random Module**
* **VS Code**
* **Command Line / Terminal**

---

## 📂 Project Structure

```text
Task-4-Rock-Paper-Scissors/
│
├── rock_paper_scissors.py
└── README.md
```

---

## ⚙️ How to Run the Project

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the Python version using:

```bash
python --version
```

or:

```bash
py --version
```

### Step 2: Clone the Repository

Clone this repository using:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### Step 3: Open the Project

Open the project folder in **VS Code**.

### Step 4: Run the Program

Open the VS Code terminal and run:

```bash
python rock_paper_scissors.py
```

If `python` does not work, use:

```bash
py rock_paper_scissors.py
```

---

## 🎮 How to Play

1. Run the Python program.
2. Enter one of the following choices:

   * `rock`
   * `paper`
   * `scissors`
3. The computer will randomly select its choice.
4. The program will display:

   * Your choice
   * Computer's choice
   * Game result
   * Current score
5. Enter `yes` to play another round.
6. Enter `no` to end the game.
7. The final score and overall winner will be displayed.

---

## 💻 Sample Output

```text
=============================================
     ROCK - PAPER - SCISSORS GAME
=============================================

Rules:
Rock beats Scissors
Scissors beats Paper
Paper beats Rock

Enter your choice (rock/paper/scissors): rock

Your choice      : rock
Computer choice  : scissors

🎉 Result: YOU WIN!

-------------------------
       SCORE
-------------------------
Your Score     : 1
Computer Score : 0

Do you want to play again? (yes/no): no

=============================================
             FINAL SCORE
=============================================

Your Score     : 1
Computer Score : 0

🏆 Congratulations! You are the overall winner!

Thank you for playing! 😊
```

---

## 🧠 Python Concepts Used

This project demonstrates the following Python concepts:

* Variables
* Lists
* User Input
* String Methods
* `if`, `elif`, and `else`
* `while` loop
* `random.choice()`
* Comparison Operators
* Logical Operators
* Score Tracking
* Input Validation

---

## 🚀 Future Improvements

The project can be improved by adding:

* GUI interface using Tkinter
* Best-of-3 or Best-of-5 game mode
* Game history
* Difficulty levels
* Sound effects
* Graphical animations
* Leaderboard system

---

## 📌 Internship Task

**Task:** 4 — Rock-Paper-Scissors Game

**Language:** Python

**Project Type:** Command-Line Application

**Status:** Completed ✅

---

## 👩‍💻 Author

**Shreya Lanjewar**

This project was created as part of my Python internship task.

---

## ⭐ Conclusion

The Rock-Paper-Scissors Game is a beginner-friendly Python project that demonstrates fundamental programming concepts such as user input, random selection, conditional logic, loops, and score tracking.

It provides an interactive way to practice Python programming while building a simple and functional command-line application.
