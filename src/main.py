import cleaning
import customization
from trolley import Trolley
from controller_support import enable_controller_support

def main():
    print("Welcome to Fast Food Simulator!\n")
    enable_controller_support()

    trolley = Trolley()
    print("\n--- Cleaning Routine ---")
    cleaning.restaurant_cleaning()
    cleaning.restroom_cleaning()

    print("\n--- Character Customization ---")
    customization.customize_character("uniform", "red apron")
    customization.customize_character("hat", "chef cap")
    customization.customize_character("accessories", "badge")

    print("\n--- Trolley Demo ---")
    trolley.add_box("Chicken Box")
    trolley.add_box("Fries Box")
    trolley.remove_box("Chicken Box")

    print("\n--- Lobby Filter Demo ---")
    lobbies = [
        {"name": "Server 1", "player_count": 2},
        {"name": "Server 2", "player_count": 5},
        {"name": "Server 3", "player_count": 4},
    ]
    filtered = [l['name'] for l in cleaning.lobby_filter(lobbies, {'min_players': 3})]
    print("Lobbies with >3 players:", filtered)

if __name__ == "__main__":
    main()
