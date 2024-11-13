import random

def guess_the_number():
    number_to_guess = random.randint(1, 1000)
    print("Guess my number between 1 and 1000 with the fewest guesses:")

    max_attempts = 10
    attempts = 0
    
    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}/{max_attempts}: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {number_to_guess}.")
        
    if attempts <= 10:
        print("Either you know the secret or you got lucky!")
    else:
        print("You should be able to do better!")

guess_the_number()
