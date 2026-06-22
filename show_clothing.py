#!/usr/bin/env python3
def main():
    clothing = input("What are you wearing? ")
    confirm = input(f"You said: {clothing}. Is that correct? (yes/no) ")
    if confirm.strip().lower() in ("yes", "y"):
        print(f"Confirmed: you're wearing {clothing}.")
    else:
        new = input("Okay, please enter what you're wearing: ")
        print(f"Got it: you're wearing {new}.")

if __name__ == "__main__":
    main()
