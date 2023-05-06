def divide(x, y):
    if y == 0:
        # if the divisor is 0, raise a ZeroDivisionError
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return x / y

# call the divide function with different arguments
print(divide(6, 3))  # prints 2.0
print(divide(4, 0))  # raises a ZeroDivisionError with the message "Cannot divide by zero"
