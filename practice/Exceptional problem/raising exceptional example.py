def divide(x,y):
    if y==0:
        raise ValueError("cannot divide by zero")
    return x/y
 #Now try without any message, is there any difference?
try:
    result= divide(10,0)
    print(result)
except ValueError as e:
    print(e)        