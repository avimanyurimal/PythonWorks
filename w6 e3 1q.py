def filter_strings_with_a(strings):
    """
    Filters out strings from the input list that do not contain the letter 'a'
    and returns a new list with only the filtered strings.
    """
    filtered_strings = []
    for string in strings:
        if 'a' in string:
            filtered_strings.append(string)
    return filtered_strings
strings = ['apple', 'banana', 'cat', 'dog']
filtered_strings = filter_strings_with_a(strings)
print(filtered_strings)
