import random

wins = 0
rounds = 0

while True:
    guess = input("Guess the total value of two dice (or type 'q' to quit): ")
    if guess.lower() == 'q':
        break
    
    guess = int(guess)
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    rounds += 1
    
    print(f"The dice rolls are {die1} and {die2}")
    if guess == total:
        print("Congratulations, you win!")
        wins += 1
    else:
        print("Sorry, you lose.")
    
print(f"You played {rounds} rounds and won {wins} times. Your win percentage is {wins/rounds*100:.2f}%")
