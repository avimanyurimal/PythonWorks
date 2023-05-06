numbers = []
while True:
    try:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input == 'done':
            break
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number or 'done' to finish.")

if len(numbers) == 0:
    print("You didn't enter any numbers.")
else:
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average}.")
