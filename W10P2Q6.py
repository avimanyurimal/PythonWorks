def binary_to_decimal(binary):
    """
    Convert a binary number to its decimal equivalent using recursion.

    :param binary: A string representing the binary number.
    :return: The decimal equivalent of the binary number.
    """
    if len(binary) == 1:
        return int(binary)
    else:
        return int(binary[-1]) + 2 * binary_to_decimal(binary[:-1])

# Prompt the user to enter a binary number
binary = input("Enter a binary number: ")

# Convert the binary number to decimal using recursion
decimal = binary_to_decimal(binary)

# Print the result
print(f"The decimal equivalent of {binary} is {decimal}.")
