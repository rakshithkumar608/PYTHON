#1. Basic Counting with while Loop:

# Write a program that counts from 1 to 10 using a while loop.

i = 1
while i<=10:
    print(i)
    i += 1


# 2. Odd Numbers Printer:

# Create a program that prints all odd numbers between 1 and 20 using a while loop.   

i = 1
while i<=20:
   print(i)
   i += 2

   #another meeathod
for i in range(1, 21, 2):
    print(i)


####
for i in range(1, 21):
    if i%2==1:
        print(i)


# 3.Ticket Booking Simulation:

# Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked."

available_seats = 8
while available_seats > 0:
    print(f"Available seats: {available_seats}")
    booking  = input("Do yoy want to book a seat (yes/no):")
    seat_number = int(input("Enter the seat number to book (1-8): "))
    if booking.lower() == "yes":
        if seat_number <= 8:
            available_seats = -1
            print("Seat booked")
    else:
        print("No booking made")
        print("All Seats are booked!")

#4. Countdown Timer:

# Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.

import time

# Basic Countdown Timer
def basic_countdown():
    """Simple countdown from 10 to 1"""
    print("🎉 NEW YEAR COUNTDOWN STARTING! 🎉")
    print("-" * 30)
    
    countdown = 10
    
    while countdown > 0:
        print(f"⏰ {countdown}")
        countdown -= 1
        time.sleep(1)  # Wait for 1 second
    
    print("🎊 Happy New Year! 🎊")