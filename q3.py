# This line of code checks if the grade of a student is a pass or fail.
grade = int(input("Enter your grade (0-100): "))
if grade <= 30:
    print ("You have and F grade. You have failed the course. Better luck next time. Study harder and try again.")
elif 31 <= grade <= 49:
    print ("You have a D grade. You have failed the course. Better luck next time. Study harder and try again.")
elif 50 <= grade <= 59:
    print ("You have a C grade. You have passed the course. Congratulations! Keep up the good work.")
elif 60 <= grade <= 69:
    print ("You have a B grade. You have passed the course. Congratulations! Keep up the good work.")
elif 70 <= grade <= 100:
    print ("You have an A grade. You have passed the course with distinction. Excellent work! Keep it up.")
else:
    print("Invalid grade entered. Please enter a grade between 0 and 100.")
