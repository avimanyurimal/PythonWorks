# Open the original text file for reading
with open("original_text.txt", "r") as orig_file:
    # Open the new text file for writing
    with open("new.txt", "w") as new_file:
        # Read the lines of the original file and write every other line to the new file
        lines = orig_file.readlines()
        for i in range(0, len(lines), 2):
            new_file.write(lines[i])
