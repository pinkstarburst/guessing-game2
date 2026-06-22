import random

secret_number = random.randint(1, 10)

print("Welcome to the Guessing Game!")
print("You have 3 attempts.")

for attempt in range(3):
    guess = int(input("Guess a number from 1-10: "))

    if guess == secret_number:
        print("🎉 You win!")
        break
    else:
        print("Wrong!")

if guess != secret_number:
    print(f"❌ You lose! The number was {secret_number}")

print("Thanks for playing!")
