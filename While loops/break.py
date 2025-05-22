sheep_count = 1
while sheep_count <= 10:
    print(f"sheep{sheep_count}")
    if sheep_count == 5:
        print("That's enough counting!")
        break
    sheep_count += 1


pin = "1234"
trails = 1

while trails<=3:
    input_pin = input(f"Trail-{trails} |Enter your 4 digit PIN:")
    trails += 1
    if input_pin == pin:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN. Try again!")

available_seats = 5

while available_seats > 0:
    print(f"{available_seats} seats available.")
    booking = input("Do you want to book a seat? (yes/no): ").lower()
    
    if booking == "yes":
        available_seats = -1
        print("Seat booked!")
    else:
        print("No booking made.")

print("All seats are booked!")