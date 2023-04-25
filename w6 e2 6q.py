my_list = []

while True:
    value = input("Enter an integer value (or 'done' to finish): ")
    
    if value == 'done':
        break
        
    try:
        value = int(value)
        if value > 100:
            value = 'over'
        my_list.append(value)
    except ValueError:
        print("Invalid input. Please enter an integer value or 'done' to finish.")

print("Final list:")
print(my_list)
