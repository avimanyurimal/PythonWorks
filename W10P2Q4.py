import os
input_file_path = input("Enter the input file path: ")
if not os.path.exists(input_file_path):
    print("Error: Input file does not exist.")
    exit()
old_word = input("Enter the word to replace: ")
new_word = input("Enter the replacement word: ")

output_file_path = input("Enter the output file path: ")
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Loop through each line in the input file
    for line in input_file:
        new_line = line.replace(old_word, new_word)
        output_file.write(new_line)

print("Replacement complete.")
