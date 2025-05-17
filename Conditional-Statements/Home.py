# 1. Basic Conditions:

# Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price.
gender = input("Gender:")
age = int(input("Age:"))
if gender == "female":
        print("Ticket is free.")
else:
        if age < 5:
            print("Ticket is free.")
        elif age <= 12:
            print("You get a child discount.")
        elif age >= 60:
            print("You get a senior citizen discount.")
        else:
            print("You pay the full fare.")


#2. Meal Time Checker:

# Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
# Breakfast: 8 AM
# Lunch: 1 PM
# Dinner: 8 PM
# If none of these times, print "It's not meal time."


time = 16
if time == 8:
    print("It's too early for breakfast.")
elif time == 13:
    print("It's too early for lunch.")
elif time == 20:    
    print("It's too early for dinner.")
else:
    print("It's not meal time.")


#3. Simple Eligibility Check:

# Write a program that checks whether a person is eligible for a library membership. If they are under 18, they get a student membership. If they are 60 or older, they get a senior citizen membership. Otherwise, they get a regular membership.

age  = int(input("Age:"))
is_student = True
if age <= 18 and is_student:
    print("You are eligible for a student membership.")
elif age >=60:
    print("You are eligible for a senior citizen membership.")    
else:
    print("You are eligible for a regular membership.")     