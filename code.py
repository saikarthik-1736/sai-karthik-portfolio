marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    print("Grade: A+ | Excellent! You are a Topper!")
elif marks >= 80:
    print("Grade: A | Very Good!")
elif marks >= 70:
    print("Grade: B | Good Job!")
elif marks >= 60:
    print("Grade: C | Average, Work Harder!")
elif marks >= 50:
    print("Grade: D | Just Passed!")
elif marks >= 35:
    print("Grade: E | Barely Passed!")
else:
    print("Grade: Fail | Better Luck Next Time!")