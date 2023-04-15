num = int(input("Enter a number: "))
digit_sum = 0
while num > 0:
    digit = num % 10
    digit_sum += digit
    num //= 10
print("The sum of the digits of the number is:", digit_sum)
