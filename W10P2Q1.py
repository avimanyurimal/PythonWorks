def sum_naturals(n):
    if n <= 0:
        return 0
    else:
        return n + sum_naturals(n-1)

# Example usage:
n = 5
sum_of_naturals = sum_naturals(n)
print(f"The sum of the first {n} natural numbers is: {sum_of_naturals}")
