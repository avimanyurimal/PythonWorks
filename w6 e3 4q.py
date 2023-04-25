def filter_vowel_strings(strings_set):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {string for string in strings_set if string[0].lower() in vowels}
strings = {'apple', 'banana', 'cat', 'dog', 'Eagle'}
vowel_strings = filter_vowel_strings(strings)
print(vowel_strings)
