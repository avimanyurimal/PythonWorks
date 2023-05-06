def factorial(n):
    """
    Recursive function to calculate the factorial of a number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Prompt the user to enter a positive integer
while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Please enter an integer.")

# Calculate the factorial and print the result
print(n, "! =", factorial(n))
