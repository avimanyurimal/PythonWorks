# initialize the sum to 0
total_sum = 0

# loop through numbers 1 to 100
for i in range(1, 101):
    # check if the number is not divisible by both 3 and 5
    if i % 3 != 0 or i % 5 != 0:
        # add the number to the sum
        total_sum += i

# print the total sum
print("The sum of all numbers between 1 and 100 that are not divisible by both 3 and 5 is:", total_sum)
