"""
---------------------------------------------------------
Python Utility Tools Script
---------------------------------------------------------
This file exists for reference and contains multiple 
small Python functions such as:
✔ Joke generator
✔ Password generator
✔ Fibonacci series
✔ Prime number checker
✔ Console menu-driven application

Purpose:
- To increase Python code weight in GitHub repo
- Keep repository language identified as Python
---------------------------------------------------------
"""

import random
import time

# ------------ Random Joke Generator ------------
jokes = [
    "Why do Python developers wear glasses? Because they can’t C!",
    "Programmer Day: When debugging is your cardio.",
    "I told my computer I needed a break, and it said 'No problem — I'll go to sleep!'",
    "Why was the JavaScript developer sad? Because he didn’t Node how to Express himself.",
    "I would tell you a UDP joke… but you might not get it.",
]

def tell_joke():
    return random.choice(jokes)


# ------------ Password Generator ------------
def generate_password(length=10):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    return ''.join(random.choice(letters) for _ in range(length))


# ------------ Fibonacci ------------
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a+b
    return result


# ------------ Prime Checker ------------
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


# ------------ Menu Driven App ------------
def main():
    while True:
        print("\n=== Python Utility Tools ===")
        print("1. Tell a joke")
        print("2. Generate password")
        print("3. Fibonacci series")
        print("4. Prime number check")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            print("Joke:", tell_joke())

        elif choice == '2':
            print("Password:", generate_password())

        elif choice == '3':
            n = int(input("How many numbers?: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == '4':
            number = int(input("Enter number: "))
            print("Prime:", is_prime(number))

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
#----------------
import requests

def get_weather(city):
    API = "https://wttr.in/{}?format=3".format(city)
    try:
        data = requests.get(API).text
        print("Weather:", data)
    except:
        print("Error fetching weather")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
#-------------
import smtplib
from email.mime.text import MIMEText

def send_mail(to, msg):
    sender = "your_email@gmail.com"
    password = "your_password_or_app_password"

    email = MIMEText(msg)
    email['From'] = sender
    email['To'] = to
    email['Subject'] = "Python Email Test"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(email)

if __name__ == "__main__":
    send_mail("receiver@gmail.com", "Hello from Python!")
#--------------
import time
import random
from os import system

board = [" "] * 20
snake = 10

while True:
    food = random.randint(0,19)
    if food != snake:
        break

while True:
    system("cls" if system=="nt" else "clear")
    board = [" "] * 20
    board[snake] = "🐍"
    board[food]  = "🍎"
    print("".join(board))

    move = input("L/R: ").lower()
    snake += -1 if move=="l" else 1
    snake = snake % 20

    if snake == food:
        print("\nYou Ate the Apple! 🎉")
        break
    time.sleep(0.1)
#-------------
import psutil
import time

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    print(f"CPU: {cpu}% | RAM: {ram}%")
    time.sleep(1)
#----------------
"""
Task Manager CLI App (Medium Level)

Features:
✔ Add task
✔ View tasks
✔ Delete task
✔ Auto save to tasks.json (persistent)
✔ Good for real-use & repo readability
"""

import json
import os

FILE = "tasks.json"


# -------- Load Saved Tasks --------
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


# -------- Save Tasks --------
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# -------- Display Tasks --------
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet! Add one.\n")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()


# -------- Main Menu --------
def main():
    tasks = load_tasks()

    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == '1':
            task = input("Enter task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added ✔")

        elif choice == '2':
            show_tasks(tasks)

        elif choice == '3':
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: ")) - 1
                if 0 <= num < len(tasks):
                    removed = tasks.pop(num)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number ❌")
            except:
                print("Please enter a number only!")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()

