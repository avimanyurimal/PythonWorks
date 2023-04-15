# get the number from the user
num = int(input("Enter a number: "))

# initialize the max digit to 0
max_digit = 0

# loop through each digit in the number
while num > 0:
    # get the last digit of the number
    digit = num % 10
    # check if the current digit is greater than the max digit
    if digit > max_digit:
        max_digit = digit
    # remove the last digit from the number
    num //= 10

# print the maximum digit
print("The largest digit in the number is:", max_digit)
