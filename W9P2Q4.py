import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

while True:
    try:
        # Prompt the user to guess the number
        guess = int(input("Guess the secret number between 1 and 10: "))

        # Check if the guess is correct
        if guess == secret_number:
            print("Congratulations! You guessed the secret number.")
            break
        else:
            print("Sorry, that's not the secret number.")

    except ValueError:
        print("Invalid input. Please enter a numeric value between 1 and 10.")
    except:
        print("An error occurred. Please try again.")
