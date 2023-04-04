# initialize sum to 0
sum = 0

# loop through numbers from 1 to 100
for i in range(1, 101):
    # check if the number is divisible by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        # add the number to the sum
        sum += i

# print the sum
print("The sum of all numbers between 1 and 100 that are divisible by both 3 and 5 is:", sum)
