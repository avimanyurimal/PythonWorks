sum = 0
while True:
    num =int(input("Enter a positive integer:"))
    if num>100:
        continue
    if num<=0:
        break
    sum+=num
print("the sum is :",sum)
