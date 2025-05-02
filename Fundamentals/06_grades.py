"""
Ask user to enter the exam grade
90 and above = A
80 - 89 = B
70 - 79 = C
60 - 69 = D
Lower than 60 = F
"""

grade = int(input("Enter your grade: "))

if grade >= 90:
    print(f'You scored an A ')
elif grade < 90 and grade >= 80:
    print("You scored an B")
elif grade < 80 and grade >= 70:
    print("You scored a C ")
elif grade < 70 and grade >= 60:
    print("You scored a D ")
else:
    print("You failed the test :( ")


