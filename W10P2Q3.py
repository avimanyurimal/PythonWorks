while True:
    try:
        num = int(input("Enter a positive integer: "))
        if num < 0:
            raise ValueError("You entered a negative integer. Please enter a positive integer.")
        break
    except ValueError as e:
        print(e)
