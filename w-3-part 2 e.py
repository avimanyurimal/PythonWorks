def improved_average():
    num1=float(input("Enter the number:"))
    num2=float(input("Enter the number:"))
    num3=float(input("Enter the number:"))
    num4=float(input("Enter the number:"))
    num5=float(input("Enter the number:"))
    mean=(num1+num2+num3+num4+num5)/5
    median=(5+1)/2
    mode=3*median-(2*mean)
    print("mean:",mean,", median:",median,"and mode:",mode)
