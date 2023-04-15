# get the number from the user
num = int(input("Enter a number: "))

# initialize the min digit to 9 (the largest possible single digit number)
min_digit = 9

# loop through each digit in the number
while num > 0:
    # get the last digit of the number
    digit = num % 10
    # check if the current digit is smaller than the min digit
    if digit < min_digit:
        min_digit = digit
    # remove the last digit from the number
    num //= 10

# print the minimum digit
print("The smallest digit in the number is:", min_digit)
