filename = "example.txt"
try:
    # Open the file for reading
    with open(filename, "r") as file:
        # Read the contents of the file
        contents = file.read()

        # Count the number of lines in the file
        num_lines = len(contents.split("\n"))

        # Print the result
        print(f"The file '{filename}' has {num_lines} lines of text.")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except IOError:
    print(f"Error: Could not read file '{filename}'.")
