import cleaning
import customization
import time
from trolley import Trolley
from controller_support import enable_controller_support
from ai import spawn_customer, spawn_employee, CustomerAI, EmployeeAI
from economy import EconomyManager

# Day/Night Cycle Implementation
class DayNightCycle:
    """Manages day/night cycle with time transitions."""
    
    def __init__(self, cycle_duration=10):
        self.time_of_day = "day"  # "day" or "night"
        self.time_elapsed = 0
        self.cycle_duration = cycle_duration  # seconds for a full cycle
    
    def advance(self):
        """Manually advance the day/night cycle."""
        old_time = self.time_of_day
        self.time_of_day = "night" if self.time_of_day == "day" else "day"
        print(f"\n=== Time Change ===")
        print(f"Transitioning from {old_time} to {self.time_of_day}")
        print(f"Current time of day: {self.time_of_day}")
        print("==================\n")
    
    def update(self, delta_time):
        """Update the day/night cycle based on elapsed time."""
        self.time_elapsed += delta_time
        if self.time_elapsed >= self.cycle_duration / 2:
            old_time = self.time_of_day
            self.time_of_day = "night" if self.time_of_day == "day" else "day"
            self.time_elapsed = 0
            print(f"\nTime changed: {old_time} -> {self.time_of_day}")
    
    def get_time_of_day(self):
        """Get current time of day."""
        return self.time_of_day

def main():
    print("Welcome to Fast Food Simulator!\n")
    enable_controller_support()
    
    # Initialize systems
    trolley = Trolley()
    day_night = DayNightCycle(cycle_duration=10)
    economy = EconomyManager(starting_money=1000)
    
    print(f"Game starts during: {day_night.get_time_of_day()}")
    print(f"Starting balance: ${economy.get_balance():.2f}")
    print(f"Starting score: {economy.get_score()}")
    
    # Initialize AI entities
    customer_counter = 0
    employee_counter = 0
    
    # Spawn initial employee
    employee = spawn_employee(employee_counter, "cashier")
    employee_ai = EmployeeAI(employee)
    employee_counter += 1
    
    while True:
        print("\n" + "="*50)
        print(f"Current Time: {day_night.get_time_of_day().upper()}")
        print(f"Balance: ${economy.get_balance():.2f} | Score: {economy.get_score()}")
        print("="*50)
        print("\nChoose an action:")
        print("1. Clean Restaurant")
        print("2. Clean Restroom")
        print("3. Customize Character")
        print("4. Use Trolley")
        print("5. Advance Day/Night Cycle")
        print("6. Simulate Customer Action")
        print("7. Simulate Employee Work")
        print("8. View Money & Score")
        print("9. View Financial Statistics")
        print("0. Exit")
        choice = input("Your choice: ")
        
        if choice == "1":
            print("\n--- Cleaning Restaurant ---")
            cleaning.restaurant_cleaning()
            economy.add_score(5, "Restaurant cleaning")
        elif choice == "2":
            print("\n--- Cleaning Restroom ---")
            cleaning.restroom_cleaning()
            economy.add_score(5, "Restroom cleaning")
        elif choice == "3":
            print("\n--- Character Customization ---")
            item = input("Enter item type (uniform/hat/accessories): ")
            detail = input("Enter detail: ")
            customization.customize_character(item, detail)
        elif choice == "4":
            print("\n--- Trolley Actions ---")
            action = input("Add or Remove box? (add/remove): ").lower()
            if action == "add":
                box_name = input("Enter box name: ")
                trolley.add_box(box_name)
            elif action == "remove":
                box_name = input("Enter box name: ")
                trolley.remove_box(box_name)
            else:
                print("Invalid action.")
        elif choice == "5":
            print("\n--- Advancing Time ---")
            day_night.advance()
        elif choice == "6":
            print("\n--- Customer Simulation ---")
            customer = spawn_customer(customer_counter)
            customer_ai = CustomerAI(customer)
            customer_counter += 1
            
            # Simulate customer's full cycle
            customer_ai.simulate_action(economy)
        elif choice == "7":
            print("\n--- Employee Simulation ---")
            employee_ai.simulate_work(economy)
        elif choice == "8":
            print("\n--- Current Status ---")
            print(f"Money: ${economy.get_balance():.2f}")
            print(f"Score: {economy.get_score()} points")
            print(f"Time of Day: {day_night.get_time_of_day()}")
        elif choice == "9":
            economy.display_statistics()
        elif choice == "0":
            print("\n--- Final Statistics ---")
            economy.display_statistics()
            print("Exiting Fast Food Simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
