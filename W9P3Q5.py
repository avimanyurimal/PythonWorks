def find_largest_integer(lst):
    try:
        largest_int = max(lst)
        return largest_int
    except ValueError:
        print("Error: The list is empty.")
my_list = [1, 4, 6, 3, 9, 2]
largest_int = find_largest_integer(my_list)
print(largest_int)  # Output: 9
empty_list = []
largest_int = find_largest_integer(empty_list)  # Output: Error: The list is empty.
