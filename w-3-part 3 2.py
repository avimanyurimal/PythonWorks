def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def modulus(a, b):
    return a % b
def exponentiation(a, b):
    return a ** b
print("Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1, "+", num2, "=", addition(num1, num2))
print(num1, "-", num2, "=", subtraction(num1, num2))
print(num1, "*", num2, "=", multiplication(num1, num2))
print(num1, "/", num2, "=", division(num1, num2))
print(num1, "%", num2, "=", modulus(num1, num2))
print(num1, "^", num2, "=", exponentiation(num1, num2))
