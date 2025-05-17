
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



# day = "Saturday"
# is_raining = False

# if day == "Saturday" or day == "Sunday":
#     if not is_raining:
#         print("Let's visit Mysuru!")
#     else:
#         print("It's raining, let's stay home.")
# else:
#     print("It's a weekday, let's wait for the weekend.")