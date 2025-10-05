"""Money and Score System

Placeholder for future economy implementation.
"""


class EconomyManager:
    """Manages money, scoring, and financial transactions."""
    
    def __init__(self, starting_money=1000):
        self.money = starting_money
        self.score = 0
        self.total_earnings = 0
        self.total_expenses = 0
        self.transaction_history = []
    
    def add_money(self, amount, reason=""):
        """Add money to the player's balance."""
        if amount < 0:
            print("Cannot add negative money. Use spend_money instead.")
            return False
        
        self.money += amount
        self.total_earnings += amount
        self.transaction_history.append({"type": "income", "amount": amount, "reason": reason})
        print(f"+ ${amount:.2f} - {reason}")
        print(f"Current balance: ${self.money:.2f}")
        return True
    
    def spend_money(self, amount, reason=""):
        """Spend money from the player's balance."""
        if amount < 0:
            print("Cannot spend negative money. Use add_money instead.")
            return False
        
        if self.money < amount:
            print(f"Insufficient funds! Need ${amount:.2f}, have ${self.money:.2f}")
            return False
        
        self.money -= amount
        self.total_expenses += amount
        self.transaction_history.append({"type": "expense", "amount": amount, "reason": reason})
        print(f"- ${amount:.2f} - {reason}")
        print(f"Current balance: ${self.money:.2f}")
        return True
    
    def add_score(self, points, reason=""):
        """Add points to the player's score."""
        if points < 0:
            print("Cannot add negative score.")
            return False
        
        self.score += points
        print(f"+ {points} points - {reason}")
        print(f"Total score: {self.score}")
        return True
    
    def get_balance(self):
        """Get the current money balance."""
        return self.money
    
    def get_score(self):
        """Get the current score."""
        return self.score
    
    def get_statistics(self):
        """Get financial statistics."""
        return {
            "balance": self.money,
            "score": self.score,
            "total_earnings": self.total_earnings,
            "total_expenses": self.total_expenses,
            "net_profit": self.total_earnings - self.total_expenses,
            "transactions": len(self.transaction_history)
        }
    
    def display_statistics(self):
        """Display financial statistics to the console."""
        stats = self.get_statistics()
        print("\n=== Financial Statistics ===")
        print(f"Balance: ${stats['balance']:.2f}")
        print(f"Score: {stats['score']}")
        print(f"Total Earnings: ${stats['total_earnings']:.2f}")
        print(f"Total Expenses: ${stats['total_expenses']:.2f}")
        print(f"Net Profit: ${stats['net_profit']:.2f}")
        print(f"Total Transactions: {stats['transactions']}")
        print("==========================\n")


# Placeholder for price constants
PRICES = {
    "burger": 5.99,
    "fries": 2.99,
    "soda": 1.99,
    "chicken_sandwich": 6.49,
    "salad": 4.99,
}

REWARDS = {
    "serve_customer": 10,
    "clean_restaurant": 5,
    "clean_restroom": 5,
    "complete_order": 15,
}


# TODO: Implement advanced economy features:
# - Dynamic pricing based on demand
# - Employee wages and scheduling
# - Ingredient purchasing and inventory
# - Restaurant upgrades and investments
# - Daily/weekly financial reports
# - Achievement-based bonuses
