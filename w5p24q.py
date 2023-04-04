"""multiplication table of the input positive integer"""
num=int(input("Enter a number:"))#prompt the user to enter a positive integer

for i in range(1,11):
    print(num,"*",i,"=",num*i)#print the multiplication table of entered integer
