def is_palindrome(s):
    """
    Recursive function to check if a given string is a palindrome.
    """
    # Base case: the string is empty or has only one character
    if len(s) <= 1:
        return True
    
    # Recursive case: check if the first and last characters are the same and recurse on the rest of the string
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Prompt the user to enter a string
s = input("Enter a string: ")

# Call the is_palindrome function and print the result
if is_palindrome(s):
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")
