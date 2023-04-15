import random
# generate a random number between 1 and 20
number = random.randint(1, 20)
# set the number of guesses to 5
num_guesses = 5
# loop through each guess
for i in range(num_guesses):
    # get the player's guess
    guess = int(input("Guess a number between 1 and 20: "))
    # check if the guess is too low
    if guess < number:
        print("Your guess is too low.")
    # check if the guess is too high
    elif guess > number:
        print("Your guess is too high.")
    # the guess is correct, end the game
    else:
        print("Congratulations! You guessed the number.")
        break
# the player has used all their guesses
else:
    print("Sorry, you ran out of guesses.")
    # reveal the number
    print("The number was:", number)
