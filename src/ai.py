"""Customer and Employee AI System

Placeholder for future AI behavior implementation.
"""

import random


class Customer:
    """Represents a customer entity with basic AI behavior."""
    
    def __init__(self, name):
        self.name = name
        self.hunger_level = random.randint(50, 100)
        self.patience = random.randint(30, 100)
        self.order = None
    
    def place_order(self):
        """Placeholder for customer order placement logic."""
        menu_items = ["burger", "fries", "soda", "chicken sandwich", "salad"]
        self.order = random.choice(menu_items)
        print(f"{self.name} ordered: {self.order}")
        return self.order
    
    def update_patience(self, amount):
        """Decrease patience over time."""
        self.patience -= amount
        if self.patience <= 0:
            print(f"{self.name} left due to low patience!")
            return False
        return True


class Employee:
    """Represents an employee entity with basic AI behavior."""
    
    def __init__(self, name, role):
        self.name = name
        self.role = role  # e.g., "cashier", "cook", "cleaner"
        self.energy = 100
        self.efficiency = random.randint(60, 100)
    
    def perform_task(self, task):
        """Placeholder for employee task execution logic."""
        if self.energy <= 0:
            print(f"{self.name} is too tired to work!")
            return False
        
        print(f"{self.name} ({self.role}) is performing: {task}")
        self.energy -= random.randint(5, 15)
        return True
    
    def rest(self):
        """Employee takes a rest to recover energy."""
        self.energy = min(100, self.energy + 20)
        print(f"{self.name} is resting. Energy: {self.energy}")


def spawn_customer(customer_id):
    """Spawns a new customer with random attributes."""
    names = ["Alex", "Jamie", "Taylor", "Jordan", "Casey", "Morgan"]
    customer = Customer(f"{random.choice(names)}_{customer_id}")
    print(f"New customer spawned: {customer.name}")
    return customer


def spawn_employee(employee_id, role):
    """Spawns a new employee with specific role."""
    names = ["Bob", "Alice", "Charlie", "Diana", "Eve", "Frank"]
    employee = Employee(f"{random.choice(names)}_{employee_id}", role)
    print(f"New employee hired: {employee.name} as {role}")
    return employee


# TODO: Implement advanced AI behaviors:
# - Customer pathfinding to counter
# - Customer mood and reaction to wait times
# - Employee task prioritization
# - Employee collaboration logic
# - AI decision-making based on game state
