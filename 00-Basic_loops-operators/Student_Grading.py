#!/usr/bin/python3

#This code grades a students marks and gives remarks accordingly.

marks = float(input("Enter marks (0 - 100): "))

if 80 <= marks <= 100:
    grade = "A"
    remark = "Excellent"
elif 70 <= marks < 80:
    grade = "B"
    remark = "Good job"
elif 60 <= marks < 70:
    grade = "C"
    remark = "Good job"
elif 50 <= marks < 60:
    grade = "D"
    remark = "Needs improvement"
else:
    grade = "Fail"
    remark = "Try harder next time"

print(f"Grade:{grade} | {remark}")
