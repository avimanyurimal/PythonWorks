try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
