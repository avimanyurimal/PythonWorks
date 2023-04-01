"""To print Grade by taking percentage from user of herald college kathmandu"""
def percentage():
    percentage=float(input("Enter your percentage:"))
    """Conditions for Grading"""
    if percentage>70:
        print("The Grade is A")
    elif percentage>60:
        print("The Grade is B")
    elif percentage>50:
        print("The Grade is c")
    elif percentage>40:
        print("The Grade is D")
    else:
        print("The Grade is fail")
