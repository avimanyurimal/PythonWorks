matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]  # create a 3x3 matrix filled with 1's

# ask user for input
row = int(input("Enter the row number (1-3): "))
column = int(input("Enter the column number (1-3): "))

# update matrix with user's input
matrix[row-1][column-1] = "X"

# print updated matrix
for row in matrix:
    print(row)
