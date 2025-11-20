#!/usr/bin/python3

'''

This code finds the highest, lowest and average marks from student grades given 
by the user without the use of inbuilt functions sum(), min(), max()

'''
print("WELCOME TO MK's STUDENT GRADE ANAYLZER")
grades = input("Enter student grades seeparated by a space: ")
grades_list = grades.split(" ")

count = len(grades_list)
grades_list = [int(g) for g in grades_list]

Sum = 0
for i in grades_list:
    Sum += i

avg = Sum / count

max_num = grades_list[0]
for i_max in grades_list:
    if i_max > max_num:
        max_num = i_max

low_num = grades_list[0]
for low in grades_list:
    if low < low_num:
        low_num = low

print("This are the student grades\n",grades_list)
print(f"The highest grade: {max_num}\nThe lowest grade: {low_num}\nThe average grade: {avg}")

