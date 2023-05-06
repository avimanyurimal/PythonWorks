try:
    user_input = input("Enter some text: ")
    print("You entered:", user_input)
    
except EOFError:
    print("Error: End of file reached.")
