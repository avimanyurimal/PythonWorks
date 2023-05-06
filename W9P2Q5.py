while True:
    try:
        # Prompt the user to enter a list of integers
        numbers = input("Enter a list of integers separated by spaces: ")

        # Convert the input string to a list of integers
        numbers_list = [int(num) for num in numbers.split()]

        # Calculate the sum of the integers
        total = sum(numbers_list)

        # Display the sum
        print(f"The sum of the numbers is {total}")

        # Break out of the loop
        break

    except ValueError:
        print("Invalid input. Please enter integer values only.")
