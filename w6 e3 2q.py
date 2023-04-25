def common_elements(set1, set2):
    return set1.intersection(set2)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common = common_elements(set1, set2)
print(common)
