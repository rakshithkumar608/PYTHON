# age = 16
# has_student_id = True

# if age < 18 and has_student_id:
#     print("You are eligible for the student discount!")
# else:
#     print("You are not eligible for the student discount.")


attendence = 75
is_student = True  
has_attendance_record = True
is_teacher_friend = True
if attendence >= 75 and is_student and has_attendance_record:
   print("You are eligible for the exam.")
elif attendence < 75 and is_student and has_attendance_record and is_teacher_friend==True:
   print("You are  eligible for the exam.")
else:
    print("You are not eligible for the exam.")


age = 65

if age < 5:
    print("Ticket is free.")
elif age <= 12:
    print("You get a child discount.")
elif age >= 70:
    print("You get a senior citizen discount.")
else:
    print("You pay the full fare.")

