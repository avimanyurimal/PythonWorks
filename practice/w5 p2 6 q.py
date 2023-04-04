p=0
n=0
c=0
while true:
    num=int(input("Enter a number:"))
    if num==0:
        break
    elif num>0:
        p+=1
    elif num<0:
        n+=1
    else:
        c+=0
print("the number of positive numbers entered",p)
print("the number of negative numbers entered",n)
print("the number is zero entered",c)
