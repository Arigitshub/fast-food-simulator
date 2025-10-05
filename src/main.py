import cleaning
import customization
from trolley import Trolley
from controller_support import enable_controller_support

# Day/Night Cycle Placeholder
# TODO: Implement full day/night cycle system
class DayNightCycle:
    """Placeholder for day/night cycle logic."""
    
    def __init__(self):
        self.time_of_day = "day"  # "day" or "night"
        self.time_elapsed = 0
        self.cycle_duration = 300  # seconds for a full cycle
    
    def update(self, delta_time):
        """Update the day/night cycle. To be implemented."""
        self.time_elapsed += delta_time
        if self.time_elapsed >= self.cycle_duration / 2:
            self.time_of_day = "night" if self.time_of_day == "day" else "day"
            self.time_elapsed = 0
    
    def get_time_of_day(self):
        """Get current time of day."""
        return self.time_of_day

def main():
    print("Welcome to Fast Food Simulator!\n")
    enable_controller_support()
    trolley = Trolley()
    
    # Initialize day/night cycle (placeholder)
    day_night = DayNightCycle()
    print(f"Game starts during: {day_night.get_time_of_day()}")
    
    while True:
        print("\nChoose an action:")
        print("1. Clean Restaurant")
        print("2. Clean Restroom")
        print("3. Customize Character")
        print("4. Use Trolley")
        print("5. View Lobby Filter Demo")
        print("0. Exit")
        choice = input("Your choice: ")
        
        if choice == "1":
            print("\n--- Cleaning Restaurant ---")
            cleaning.restaurant_cleaning()
        elif choice == "2":
            print("\n--- Cleaning Restroom ---")
            cleaning.restroom_cleaning()
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
            print("\n--- Lobby Filter Demo ---")
            lobbies = [
                {"name": "Server 1", "player_count": 2},
                {"name": "Server 2", "player_count": 5},
                {"name": "Server 3", "player_count": 4},
            ]
            filtered = [l['name'] for l in cleaning.lobby_filter(lobbies, {'min_players': 3})]
            print("Lobbies with >3 players:", filtered)
        elif choice == "0":
            print("Exiting Fast Food Simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
