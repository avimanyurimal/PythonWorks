while True:
    try:
        number = float(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
