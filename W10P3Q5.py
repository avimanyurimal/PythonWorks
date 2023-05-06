def factorial(n):
    """
    Recursive function to calculate the factorial of a number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Prompt the user to enter a positive integer
n = int(input("Enter a positive integer: "))

# Calculate the factorial and print the result
print(n, "! =", factorial(n))
