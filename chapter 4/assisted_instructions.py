import random

def ask_question():
    a, b = random.randint(1, 9), random.randint(1, 9)
    while True:
        answer = int(input(f"How much is {a} times {b}? "))
        if answer == a * b:
            print("Very good!")
            break
        else:
            print("No. Please try again.")

ask_question()
