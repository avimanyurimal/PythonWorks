# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Try to convert the string to an integer
try:
    number = int(user_input)
except ValueError:
    print("The string cannot be converted to an integer.")
else:
    print("The integer value is", number)
