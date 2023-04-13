def create_rug(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("#", end="")
        print()

# Get user input for number of rows and columns
rows = int(input("Enter the number of rows for the rug: "))
cols = int(input("Enter the number of columns for the rug: "))

# Create the rug
create_rug(rows, cols)