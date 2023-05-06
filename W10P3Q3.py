numbers = []
while True:
    try:
        user_input = input("Enter an integer (or 'done' to finish): ")
        if user_input == 'done':
            break
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter an integer or 'done' to finish.")

if len(numbers) == 0:
    print("You didn't enter any numbers.")
else:
    total = sum(numbers)
    print(f"The sum of the numbers is {total}.")
