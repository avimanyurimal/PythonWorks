import random

print("Welcome to the dice game!")

while True:
    # Generate random dice rolls
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    # Prompt the player to guess the total value
    guess = int(input("Guess the total value of the dice rolls (2-12): "))

    # Check if the guess is correct
    if guess == total:
        print("Congratulations, you guessed the correct value!")
    else:
        print(f"Sorry, the correct value was {total}.")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "n":
        break

print("Thanks for playing!")
