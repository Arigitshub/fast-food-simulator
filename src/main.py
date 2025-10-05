import cleaning
import customization
import time
import random
from trolley import Trolley
from controller_support import enable_controller_support
from ai import spawn_customer, spawn_employee, CustomerAI, EmployeeAI, auto_spawn_customers
from economy import EconomyManager

# Day/Night Cycle Implementation
class DayNightCycle:
    """Manages day/night cycle with time transitions and effects."""
    
    def __init__(self, cycle_duration=10):
        self.time_of_day = "day"  # "day" or "night"
        self.time_elapsed = 0
        self.cycle_duration = cycle_duration  # rounds for a full cycle
        self.round_count = 0
    
    def advance(self):
        """Manually advance the day/night cycle."""
        old_time = self.time_of_day
        self.time_of_day = "night" if self.time_of_day == "day" else "day"
        print(f"\n" + "="*50)
        print(f"☕ === TIME CHANGE ===")
        print(f"  {old_time.upper()} → {self.time_of_day.upper()}")
        if self.time_of_day == "night":
            print(f"  🌙 It's getting dark. Fewer customers expected.")
        else:
            print(f"  ☀️ The sun is up! Busy day ahead.")
        print("="*50 + "\n")
    
    def update_round(self):
        """Update based on round progression."""
        self.round_count += 1
        if self.round_count >= self.cycle_duration:
            self.advance()
            self.round_count = 0
    
    def get_time_of_day(self):
        """Get current time of day."""
        return self.time_of_day
    
    def get_time_icon(self):
        """Get icon representing current time."""
        return "☀️" if self.time_of_day == "day" else "🌙"

def simulate_round(day_night, economy, customer_counter, employee_ais, round_num):
    """Simulate a single round of gameplay."""
    print(f"\n" + "#"*50)
    print(f"🎮 ROUND {round_num} - {day_night.get_time_icon()} {day_night.get_time_of_day().upper()}")
    print("#"*50)
    
    time_of_day = day_night.get_time_of_day()
    
    # Auto-spawn customers based on time
    new_customers = auto_spawn_customers(customer_counter, time_of_day)
    customer_counter += len(new_customers)
    
    if not new_customers:
        print("\n🚨 No customers this round!")
    
    # Process each customer
    for customer in new_customers:
        customer_ai = CustomerAI(customer)
        customer_ai.simulate_action(economy, time_of_day)
    
    # Employees work
    print("\n" + "-"*50)
    print("👥 EMPLOYEE ACTIVITIES")
    print("-"*50)
    for emp_ai in employee_ais:
        emp_ai.simulate_work(economy, time_of_day)
    
    # Show round summary
    print("\n" + "="*50)
    print("📊 ROUND SUMMARY")
    print("="*50)
    print(f"💰 Balance: ${economy.get_balance():.2f}")
    print(f"⭐ Score: {economy.get_score()} points")
    print(f"🍔 Total Customers Served: {economy.get_statistics()['customers_served']}")
    print("="*50)
    
    return customer_counter

def main():
    print("\n" + "="*50)
    print("🍔 WELCOME TO FAST FOOD SIMULATOR! 🍔")
    print("="*50)
    enable_controller_support()
    
    # Initialize systems
    trolley = Trolley()
    day_night = DayNightCycle(cycle_duration=5)  # Change time every 5 rounds
    economy = EconomyManager(starting_money=1000)
    
    print(f"\n☀️ Game starts during: {day_night.get_time_of_day().upper()}")
    print(f"💰 Starting balance: ${economy.get_balance():.2f}")
    print(f"⭐ Starting score: {economy.get_score()}")
    
    # Initialize AI entities
    customer_counter = 0
    employee_counter = 0
    
    # Spawn initial employees
    employees = []
    employee_ais = []
    
    print("\n" + "-"*50)
    print("👥 HIRING INITIAL STAFF")
    print("-"*50)
    for role in ["cashier", "cook"]:
        employee = spawn_employee(employee_counter, role)
        employees.append(employee)
        employee_ais.append(EmployeeAI(employee))
        employee_counter += 1
    
    round_num = 0
    
    while True:
        print("\n\n" + "="*50)
        print(f"💼 MAIN MENU - {day_night.get_time_icon()} {day_night.get_time_of_day().upper()}")
        print("="*50)
        print(f"💰 Balance: ${economy.get_balance():.2f} | ⭐ Score: {economy.get_score()}")
        print("="*50)
        print("\nChoose an action:")
        print("1. 🎮 Simulate Round (Auto-play)")
        print("2. 🧹 Clean Restaurant")
        print("3. 🚿 Clean Restroom")
        print("4. 👗 Customize Character")
        print("5. 🛍️ Use Trolley")
        print("6. ⏰ Advance Day/Night Cycle")
        print("7. 👥 Manually Spawn Customer")
        print("8. 👷 Hire New Employee")
        print("9. 📊 View Financial Statistics")
        print("0. 🚪 Exit")
        choice = input("\n👉 Your choice: ")
        
        if choice == "1":
            # Auto-simulate round
            round_num += 1
            customer_counter = simulate_round(day_night, economy, customer_counter, employee_ais, round_num)
            day_night.update_round()
            
        elif choice == "2":
            print("\n🧹 --- Cleaning Restaurant ---")
            cleaning.restaurant_cleaning()
            economy.add_score(5, "Restaurant cleaning")
            
        elif choice == "3":
            print("\n🚿 --- Cleaning Restroom ---")
            cleaning.restroom_cleaning()
            economy.add_score(5, "Restroom cleaning")
            
        elif choice == "4":
            print("\n👗 --- Character Customization ---")
            item = input("Enter item type (uniform/hat/accessories): ")
            detail = input("Enter detail: ")
            customization.customize_character(item, detail)
            
        elif choice == "5":
            print("\n🛍️ --- Trolley Actions ---")
            action = input("Add or Remove box? (add/remove): ").lower()
            if action == "add":
                box_name = input("Enter box name: ")
                trolley.add_box(box_name)
            elif action == "remove":
                box_name = input("Enter box name: ")
                trolley.remove_box(box_name)
            else:
                print("❌ Invalid action.")
                
        elif choice == "6":
            print("\n⏰ --- Advancing Time ---")
            day_night.advance()
            
        elif choice == "7":
            print("\n👥 --- Customer Simulation ---")
            customer = spawn_customer(customer_counter)
            customer_ai = CustomerAI(customer)
            customer_counter += 1
            customer_ai.simulate_action(economy, day_night.get_time_of_day())
            
        elif choice == "8":
            print("\n👷 --- Hiring Employee ---")
            print("Available roles: cashier, cook, cleaner, manager")
            role = input("Enter role: ").lower()
            if role in ["cashier", "cook", "cleaner", "manager"]:
                employee = spawn_employee(employee_counter, role)
                employees.append(employee)
                employee_ais.append(EmployeeAI(employee))
                employee_counter += 1
            else:
                print("❌ Invalid role!")
                
        elif choice == "9":
            economy.display_statistics()
            
        elif choice == "0":
            print("\n" + "="*50)
            print("💼 FINAL STATISTICS")
            print("="*50)
            economy.display_statistics()
            print("\n👋 Exiting Fast Food Simulator. Thanks for playing!")
            print("="*50)
            break
            
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
