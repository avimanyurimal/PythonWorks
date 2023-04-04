# get user input
n = int(input("Enter the number of terms: "))

# initialize the first two terms of the series
a, b = 0, 1

# print the first n terms of the series
for i in range(n):
    print(a, end=' ')
    a, b = b, a+b
