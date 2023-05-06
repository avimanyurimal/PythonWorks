filename = input("Enter the file name: ")

vowels = ["a", "e", "i", "o", "u"]
count = 0

with open(filename, "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            if word[0].lower() in vowels:
                count += 1

print(f"Number of words that start with a vowel: {count}")
