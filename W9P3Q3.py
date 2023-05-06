try:
    amount = float(input("Enter an amount of money: "))
    
    if amount < 10000:
        raise ValueError("Amount should be greater than or equal to 10,000.")
    
    print("The amount entered is:", amount)
    
except ValueError as e:
    print("Error:", e)
