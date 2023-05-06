while True:
    try:
        # Prompt the user to enter two integers
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        # Divide the first integer by the second integer
        result = num1 / num2

        # Display the result
        print(f"{num1} divided by {num2} is {result}")

        # Break out of the loop
        break

    except ValueError:
        print("Invalid input. Please enter integers only.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero value for the second integer.")
