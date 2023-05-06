def gcd(a, b):
    """
    Recursive function to find the greatest common divisor of two positive integers.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

try:
    num1 = int(input("Enter the first positive integer: "))
    num2 = int(input("Enter the second positive integer: "))

    if num1 <= 0 or num2 <= 0:
        print("Please enter only positive integers.")
    else:
        print("The greatest common divisor of", num1, "and", num2, "is:", gcd(num1, num2))

except ValueError:
    print("Please enter only positive integers.")
