# -*- coding: utf-8 *-*

student_marks = {}

def calculate_mark(points, max_points):
    mark = float(points) * 5 / float(max_points) + 1
    mark_rounded = round(mark * 2) / 2
    return mark_rounded

def print_and_exit():
    grade_total = 0
    for name, mark in student_marks.items():
        grade_total = grade_total + mark
        if mark > 4:
            print(name + " has passed with a " + str(mark))
        else:
            print(name + " has failed with a " + str(mark))
    average_grade = grade_total / len(student_marks)
    print("The average grade is: " + str(average_grade))
    exit()

while True:
    student_name = input("Enter name of student: ")
    if student_name == "exit":
        print_and_exit()
    student_points = input("Enter score of student: ")
    if student_points == "exit":
        print_and_exit()
    max_score = input("Enter max score: ")
    if max_score == "exit":
        print_and_exit()
    
    student_grade = calculate_mark(student_points, max_score)
    student_marks[student_name] = student_grade