def list_to_int(numbers):
    """
    Converts a list of integers into a single integer by concatenating all the integers
    """
    return int(''.join(map(str, numbers)))
numbers = [11, 33, 50]
result = list_to_int(numbers)
print(result)
