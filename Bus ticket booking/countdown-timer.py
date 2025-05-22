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

# Enhanced Countdown Timer with visual effects
def enhanced_countdown():
    """Enhanced countdown with visual effects"""
    print("🎆 ENHANCED NEW YEAR COUNTDOWN! 🎆")
    print("=" * 40)
    
    countdown = 10
    
    while countdown > 0:
        # Different visual effects for different numbers
        if countdown <= 3:
            print(f"🔥 {countdown} 🔥")
        elif countdown <= 5:
            print(f"⭐ {countdown} ⭐")
        else:
            print(f"⏰ {countdown}")
        
        countdown -= 1
        time.sleep(1)
    
    # Celebration message
    print("\n" + "🎊" * 20)
    print("🎉 HAPPY NEW YEAR! 🎉")
    print("🎊" * 20)
    print("🥳 Wishing you joy and happiness! 🥳")

# Customizable Countdown Timer
def custom_countdown():
    """Countdown timer with user input"""
    try:
        start_number = int(input("Enter countdown start number (default 10): ") or "10")
        
        if start_number <= 0:
            print("Please enter a positive number!")
            return
        
        print(f"\n🚀 COUNTDOWN FROM {start_number}! 🚀")
        print("-" * 30)
        
        countdown = start_number
        
        while countdown > 0:
            print(f"⏰ {countdown}")
            countdown -= 1
            time.sleep(1)
        
        print("🎊 Happy New Year! 🎊")
        
    except ValueError:
        print("Please enter a valid number!")

# Countdown with progress bar
def countdown_with_progress():
    """Countdown with visual progress bar"""
    print("📊 COUNTDOWN WITH PROGRESS BAR 📊")
    print("=" * 40)
    
    total_time = 10
    countdown = total_time
    
    while countdown > 0:
        # Calculate progress
        progress = (total_time - countdown) / total_time
        bar_length = 20
        filled_length = int(bar_length * progress)
        
        # Create progress bar
        bar = "█" * filled_length + "░" * (bar_length - filled_length)
        percentage = progress * 100
        
        print(f"⏰ {countdown:2d} |{bar}| {percentage:5.1f}%")
        
        countdown -= 1
        time.sleep(1)
    
    print(f"⏰  0 |{'█' * bar_length}| 100.0%")
    print("\n🎊 Happy New Year! 🎊")

# Multiple countdown timers
def multiple_countdowns():
    """Run multiple different countdown styles"""
    print("🎪 MULTIPLE COUNTDOWN STYLES 🎪")
    print("=" * 40)
    
    # Style 1: Numbers only
    print("\n1️⃣ Basic Numbers:")
    countdown = 5
    while countdown > 0:
        print(countdown)
        countdown -= 1
        time.sleep(0.8)
    
    # Style 2: With words
    print("\n2️⃣ With Words:")
    countdown = 5
    numbers_in_words = ["Five", "Four", "Three", "Two", "One"]
    index = 0
    
    while countdown > 0:
        print(f"{numbers_in_words[index]}!")
        countdown -= 1
        index += 1
        time.sleep(0.8)
    
    # Style 3: Visual countdown
    print("\n3️⃣ Visual Countdown:")
    countdown = 5
    
    while countdown > 0:
        stars = "⭐" * countdown
        print(f"{countdown} {stars}")
        countdown -= 1
        time.sleep(0.8)
    
    print("\n🎊🎉 HAPPY NEW YEAR! 🎉🎊")

# Interactive countdown menu
def countdown_menu():
    """Interactive menu for different countdown options"""
    while True:
        print("\n🎯 COUNTDOWN TIMER MENU 🎯")
        print("=" * 30)
        print("1. Basic Countdown (10 to 1)")
        print("2. Enhanced Countdown (with effects)")
        print("3. Custom Countdown (choose start number)")
        print("4. Countdown with Progress Bar")
        print("5. Multiple Countdown Styles")
        print("6. Exit")
        print("-" * 30)
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            print()
            basic_countdown()
        
        elif choice == "2":
            print()
            enhanced_countdown()
        
        elif choice == "3":
            print()
            custom_countdown()
        
        elif choice == "4":
            print()
            countdown_with_progress()
        
        elif choice == "5":
            print()
            multiple_countdowns()
        
        elif choice == "6":
            print("\n👋 Thanks for using the countdown timer!")
            break
        
        else:
            print("❌ Invalid choice! Please try again.")
        
        input("\nPress Enter to return to menu...")

# Simple version - exactly what was requested
def simple_countdown():
    """Simple countdown as requested"""
    countdown = 10
    
    while countdown > 0:
        print(countdown)
        countdown -= 1
    
    print("Happy New Year!")

# Run the program
if __name__ == "__main__":
    print("🎊 Welcome to the Countdown Timer Program! 🎊")
    print("\nChoose version:")
    print("1. Simple (basic requirement)")
    print("2. Interactive Menu (multiple options)")
    
    try:
        version = input("\nEnter choice (1 or 2): ").strip()
        
        if version == "1":
            print("\n" + "="*30)
            simple_countdown()
        elif version == "2":
            countdown_menu()
        else:
            print("\nRunning simple version...")
            print("="*30)
            simple_countdown()
    
    except KeyboardInterrupt:
        print("\n\n👋 Countdown interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Running simple countdown...")
        simple_countdown()