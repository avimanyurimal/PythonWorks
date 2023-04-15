string = input("Enter a string: ")
vowel_count = 0
for char in string:
    if char in "aeiouAEIOU":
        vowel_count += 1
print("The number of vowels in the string is:", vowel_count)
