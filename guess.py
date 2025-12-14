import random

print("Welcome to the Number Guessing Game!")

secret_number = random.randint(1, 10)  # Computer chooses a number
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("🎉 Correct! You guessed the number!")
else:
    print("❌ Wrong! The correct number was:", secret_number)
