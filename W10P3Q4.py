def recursive_product(numbers):
    if len(numbers) == 0:
        return 1
    else:
        return numbers[0] * recursive_product(numbers[1:])
numbers = [1, 2, 3, 4, 5]
product = recursive_product(numbers)
print(product)  # Output: 120
