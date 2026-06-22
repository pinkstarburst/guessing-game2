import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number from 1-10"))

if guess == secret_number:
    print("You Win!")
else:
    print(f"You Lose! The number was {secret_number}")

print("Thanks for playing!")




print("this is guessing game 2.0")


