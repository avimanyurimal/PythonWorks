def is_unique(lst):
    """
    Check if a list contains only unique elements.
    """
    # Create an empty set to store the unique elements
    unique_set = set()

    # Loop over each element in the list
    for elem in lst:
        # If the element is already in the set, it's a duplicate, so return False
        if elem in unique_set:
            return False
        # Otherwise, add the element to the set
        else:
            unique_set.add(elem)

    # If the loop completes without finding any duplicates, return True
    return True
my_list = [1, 2, 3, 4, 5]
result = is_unique(my_list)
print(result)  # True

my_list = [1, 2, 3, 3, 4, 5]
result = is_unique(my_list)
print(result)  # False
