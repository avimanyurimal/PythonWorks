positive_count = 0
negative_count = 0
zero_count = 0

while True:
    num = input("Enter a number (type 'stop' to end): ")
    if num == 'stop':
        break
    
    num = int(num)
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive numbers entered:", positive_count)
print("Negative numbers entered:", negative_count)
print("Zeroes entered:", zero_count)
