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

