"""Program to print BMI of the persons"""
#prompt user to input their weight and height
def func():
    weight=float(input("Enter your weight in kg:"))
    height=float(input("Enter your height in cm:"))
    Bmi=weight/(height/100)**2
    print("Bmi is",Bmi)
    if Bmi<18.5:
        print("user is underweight")
    elif 18.5<=Bmi<25:
        print("user is normal weight")
    elif 25<=Bmi<30:
        print("user is overweight")
    elif Bmi>=30:
        print("User is obese")
        
