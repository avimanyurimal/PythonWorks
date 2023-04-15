a=0
b=0
c=0
while True:
    num=int(input("Enter a number:"))
    
    if num>0:
        a=a+1
    elif num<0:
        b=b+1
    else:
        c=c+1

    choice=input("want to continue? yes/no")
    if choice=="y":
        continue
    else:
        break
print("the number of positive number are",a)
print("the number of positive number are",b)
print("the number of zero are",c)
    
