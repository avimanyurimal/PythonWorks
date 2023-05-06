try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("The result of the division is:", result)
