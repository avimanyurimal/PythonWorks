while True:
    try:
        # Prompt the user to enter a list of numbers
        numbers = input("Enter a list of numbers separated by spaces: ")

        # Convert the input string to a list of floats
        numbers_list = [float(num) for num in numbers.split()]

        # Calculate the average of the numbers
        average = sum(numbers_list) / len(numbers_list)

        # Display the average
        print(f"The average of the numbers is {average}")

        # Break out of the loop
        break

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
