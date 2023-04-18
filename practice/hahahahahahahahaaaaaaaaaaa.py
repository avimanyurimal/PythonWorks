import random
random = 0
win = 0
while True:
    guess = input("guess the value of two dice(2-12)or enter 'q' to quite the game:")
    if guess == "q":
       break
    guess = int(guess)
    if guess < 2 or guess > 12:
        print("you have enter the invalid guess plesse enter the value between 2-12")
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll = roll1+roll2
    if roll == guess:
        print("congratulation")
        win+= 1
    else:
        print("sorry,",roll)
    random+= 1
if round > 0:
    win_percent = 100*win/round
    print(f"you played", round, "rounds and won", win, "of them", win_percent,"%")
else:
    print("you didnt played another round")
