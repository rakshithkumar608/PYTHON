import datetime
import random
import time

class BusBookingSystem:
    def __init__(self):
        # Initialize bus data
        self.buses = {
            "BUS001": {
                "route": "Mangalore → Banglore",
                "departure": "08:00 AM",
                "arrival": "12:00 PM",
                "price": (800-2000),
                "total_seats": 40,
                "booked_seats": set(),
                "type": "AC Deluxe"
            },
            "BUS002": {
                "route": "Banglore - Mangalore",
                "departure": "02:00 PM",
                "arrival": "06:00 PM",
                "price": 2000,
                "total_seats": 30,
                "booked_seats": set(),
                "type": "AC Deluxe"
            },
            "BUS003": {
                "route": "Banglore - Delhi",
                "departure": "10:00 AM",
                "arrival": "02:30 PM",
                "price": 2600,
                "total_seats": 35,
                "booked_seats": set(),
                "type": "Premium"
            }
        }
        
        # Initialize some random bookings for demo
        self._simulate_existing_bookings()
        
        # Booking history
        self.booking_history = []
        self.booking_counter = 1000
    
    def _simulate_existing_bookings(self):
        """Simulate some existing bookings for realistic demo"""
        for bus_id in self.buses:
            num_bookings = random.randint(5, 15)
            booked_seats = random.sample(range(1, self.buses[bus_id]["total_seats"] + 1), num_bookings)
            self.buses[bus_id]["booked_seats"] = set(booked_seats)
    
    def display_header(self):
        """Display system header"""
        print("\n" + "="*60)
        print("🚌 REAL-TIME BUS TICKET BOOKING SYSTEM 🚌")
        print("="*60)
        print(f"📅 Current Date & Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
    
    def display_available_buses(self):
        """Display all available buses with real-time seat availability"""
        print("\n📋 AVAILABLE BUSES:")
        print("-" * 80)
        print(f"{'Bus ID':<8} {'Route':<25} {'Departure':<10} {'Arrival':<10} {'Price':<8} {'Available':<10} {'Type'}")
        print("-" * 80)
        
        for bus_id, bus_info in self.buses.items():
            available_seats = bus_info["total_seats"] - len(bus_info["booked_seats"])
            print(f"{bus_id:<8} {bus_info['route']:<25} {bus_info['departure']:<10} "
                  f"{bus_info['arrival']:<10} ${bus_info['price']:<7.2f} {available_seats:<10} {bus_info['type']}")
        print("-" * 80)
    
    def display_seat_map(self, bus_id):
        """Display seat map for selected bus"""
        if bus_id not in self.buses:
            print("❌ Invalid bus ID!")
            return False
        
        bus_info = self.buses[bus_id]
        total_seats = bus_info["total_seats"]
        booked_seats = bus_info["booked_seats"]
        
        print(f"\n🪑 SEAT MAP FOR BUS {bus_id} ({bus_info['route']})")
        print(f"🟢 Available | 🔴 Booked | Total Seats: {total_seats}")
        print("-" * 50)
        
        # Display seats in rows of 4 (2+2 configuration)
        for row in range(0, total_seats, 4):
            left_seats = []
            right_seats = []
            
            for i in range(4):
                seat_num = row + i + 1
                if seat_num <= total_seats:
                    if seat_num in booked_seats:
                        symbol = "🔴"
                    else:
                        symbol = "🟢"
                    
                    if i < 2:
                        left_seats.append(f"{symbol}{seat_num:2d}")
                    else:
                        right_seats.append(f"{symbol}{seat_num:2d}")
            
            left_side = " ".join(left_seats).ljust(10)
            right_side = " ".join(right_seats)
            print(f"{left_side}    {right_side}")
        
        print("-" * 50)
        return True
    
    def book_ticket(self, bus_id, seat_numbers, passenger_info):
        """Book tickets for specified seats"""
        if bus_id not in self.buses:
            return False, "Invalid bus ID!"
        
        bus_info = self.buses[bus_id]
        
        # Check if seats are valid and available
        for seat_num in seat_numbers:
            if seat_num < 1 or seat_num > bus_info["total_seats"]:
                return False, f"Invalid seat number: {seat_num}"
            
            if seat_num in bus_info["booked_seats"]:
                return False, f"Seat {seat_num} is already booked!"
        
        # Book the seats
        for seat_num in seat_numbers:
            bus_info["booked_seats"].add(seat_num)
        
        # Generate booking details
        booking_id = f"BKG{self.booking_counter}"
        self.booking_counter += 1
        
        total_amount = len(seat_numbers) * bus_info["price"]
        
        booking_details = {
            "booking_id": booking_id,
            "bus_id": bus_id,
            "route": bus_info["route"],
            "departure": bus_info["departure"],
            "seats": seat_numbers,
            "passenger_info": passenger_info,
            "total_amount": total_amount,
            "booking_time": datetime.datetime.now(),
            "status": "Confirmed"
        }
        
        self.booking_history.append(booking_details)
        return True, booking_details
    
    def print_ticket(self, booking_details):
        """Print ticket details"""
        print("\n" + "="*50)
        print("🎫 TICKET CONFIRMATION")
        print("="*50)
        print(f"Booking ID: {booking_details['booking_id']}")
        print(f"Route: {booking_details['route']}")
        print(f"Departure: {booking_details['departure']}")
        print(f"Passenger: {booking_details['passenger_info']['name']}")
        print(f"Phone: {booking_details['passenger_info']['phone']}")
        print(f"Seat Numbers: {', '.join(map(str, booking_details['seats']))}")
        print(f"Total Amount: ${booking_details['total_amount']:.2f}")
        print(f"Booking Time: {booking_details['booking_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Status: {booking_details['status']}")
        print("="*50)
        print("🚌 Thank you for choosing our service!")
        print("Please arrive 15 minutes before departure.")
        print("="*50)
    
    def simulate_real_time_bookings(self):
        """Simulate other passengers booking tickets in real-time"""
        if random.random() < 0.3:  # 30% chance of simulation
            bus_id = random.choice(list(self.buses.keys()))
            bus_info = self.buses[bus_id]
            available_seats = [i for i in range(1, bus_info["total_seats"] + 1) 
                             if i not in bus_info["booked_seats"]]
            
            if available_seats:
                seats_to_book = random.randint(1, min(3, len(available_seats)))
                selected_seats = random.sample(available_seats, seats_to_book)
                
                for seat in selected_seats:
                    bus_info["booked_seats"].add(seat)
                
                print(f"⚡ REAL-TIME UPDATE: {seats_to_book} seat(s) just booked on {bus_id}!")
                time.sleep(1)
    
    def run(self):
        """Main booking system loop"""
        while True:
            self.display_header()
            
            # Simulate real-time bookings
            self.simulate_real_time_bookings()
            
            print("\n📱 MAIN MENU:")
            print("1. View Available Buses")
            print("2. Book Ticket")
            print("3. View Booking History")
            print("4. Exit")
            
            try:
                choice = input("\nEnter your choice (1-4): ").strip()
                
                if choice == "1":
                    self.display_available_buses()
                    input("\nPress Enter to continue...")
                
                elif choice == "2":
                    self.display_available_buses()
                    
                    bus_id = input("\nEnter Bus ID: ").strip().upper()
                    
                    if not self.display_seat_map(bus_id):
                        input("Press Enter to continue...")
                        continue
                    
                    try:
                        seat_input = input("\nEnter seat numbers (comma-separated, e.g., 1,2,3): ")
                        seat_numbers = [int(x.strip()) for x in seat_input.split(",")]
                        
                        if not seat_numbers:
                            print("❌ Please enter at least one seat number!")
                            input("Press Enter to continue...")
                            continue
                        
                        # Get passenger information
                        print("\n👤 PASSENGER INFORMATION:")
                        name = input("Enter passenger name: ").strip()
                        phone = input("Enter phone number: ").strip()
                        email = input("Enter email (optional): ").strip()
                        
                        if not name or not phone:
                            print("❌ Name and phone number are required!")
                            input("Press Enter to continue...")
                            continue
                        
                        passenger_info = {
                            "name": name,
                            "phone": phone,
                            "email": email
                        }
                        
                        # Attempt booking
                        success, result = self.book_ticket(bus_id, seat_numbers, passenger_info)
                        
                        if success:
                            print("✅ Booking Successful!")
                            self.print_ticket(result)
                        else:
                            print(f"❌ Booking Failed: {result}")
                        
                        input("\nPress Enter to continue...")
                    
                    except ValueError:
                        print("❌ Invalid seat number format!")
                        input("Press Enter to continue...")
                
                elif choice == "3":
                    print("\n📜 BOOKING HISTORY:")
                    if not self.booking_history:
                        print("No bookings found.")
                    else:
                        for booking in self.booking_history[-5:]:  # Show last 5 bookings
                            print(f"ID: {booking['booking_id']} | Route: {booking['route']} | "
                                  f"Seats: {booking['seats']} | Amount: ${booking['total_amount']:.2f}")
                    input("\nPress Enter to continue...")
                
                elif choice == "4":
                    print("\n👋 Thank you for using our Bus Booking System!")
                    print("Have a safe journey! 🚌")
                    break
                
                else:
                    print("❌ Invalid choice! Please try again.")
                    input("Press Enter to continue...")
            
            except KeyboardInterrupt:
                print("\n\n👋 System interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")
                input("Press Enter to continue...")

# Run the booking system
if __name__ == "__main__":
    booking_system = BusBookingSystem()
    booking_system.run()