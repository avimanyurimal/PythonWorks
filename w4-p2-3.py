"""To check the leap year or not"""
def leap_year():
    leap_year=int(input("Enter a year:"))
    if leap_year%4==0:
        print("Leap year")
    else:
            print("Not a leap year")
