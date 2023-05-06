while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        
        result = numerator / denominator
        
        print("The result of division is:", result)
        break
        
    except ValueError:
        print("Entered value is wrong. Please enter a numeric value.")
        continue
        
    except ZeroDivisionError:
        print("Can't divide by zero. Please enter a non-zero denominator.")
        continue
