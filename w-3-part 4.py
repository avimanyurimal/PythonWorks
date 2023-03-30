def percentage():
    assignment1 = float(input("Enter your score for Assignment 1 (out of 100): "))
    assignment2 = float(input("Enter your score for Assignment 2 (out of 100): "))
    assignment3 = float(input("Enter your score for Assignment 3 (out of 100): "))
    assignment4 = float(input("Enter your score for Assignment 4 (out of 100): "))
    assignment5 = float(input("Enter your score for Assignment 5 (out of 100): "))
    total_score = assignment1 + assignment2 + assignment3 + assignment4 + assignment5
    max_score = 500
    overall_grade = (total_score / max_score) * 100
    print("Your overall grade is: {:.2f}%".format(overall_grade))
