def concatenate_strings(str1, str2):
    try:
        return str1 + str2
    except TypeError:
        return None
str1 = "Hello"
str2 = "world!"
result = concatenate_strings(str1, str2)
print(result)  # Output: "Hello world!"

str1 = "Hello"
str2 = 123
result = concatenate_strings(str1, str2)
print(result)  # Output: None
