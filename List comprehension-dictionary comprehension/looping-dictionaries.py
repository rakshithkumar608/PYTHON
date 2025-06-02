student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for student in student_marks:
    print(student)


student_marks = {"Anand": 85, "Geetha": 90, "Kumar": 78}

for marks in student_marks.values():
    print(marks)   



student_marks = {"Anant": 90, "Bharat": 85, "Chitra": 92}
for student, marks in student_marks.items():
    print(f"{student}-----{marks}")