"""Customer and Employee AI System
Implements AI behavior for customers and employees.
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

# CustomerAI and EmployeeAI classes for enhanced simulation

class CustomerAI:
    """AI controller for customer behavior."""
    
    def __init__(self, customer):
        self.customer = customer
        self.state = "entering"  # entering, ordering, waiting, leaving
    
    def simulate_action(self, economy_manager=None):
        """Simulate a complete customer action cycle."""
        print(f"\n--- {self.customer.name} Actions ---")
        
        # Enter
        if self.state == "entering":
            print(f"{self.customer.name} enters the restaurant.")
            self.state = "ordering"
        
        # Order
        if self.state == "ordering":
            order = self.customer.place_order()
            self.state = "waiting"
            
            # Process payment through economy manager
            if economy_manager:
                from economy import PRICES
                # Normalize order name for price lookup
                order_key = order.replace(" ", "_")
                if order_key in PRICES:
                    price = PRICES[order_key]
                    economy_manager.add_money(price, f"Customer order: {order}")
                    economy_manager.add_score(10, f"Served {self.customer.name}")
                else:
                    print(f"Warning: Price not found for {order}")
        
        # Leave
        if self.state == "waiting":
            print(f"{self.customer.name} receives order and leaves satisfied.")
            self.state = "leaving"
            return True  # Completed
        
        return False  # Still in progress

class EmployeeAI:
    """AI controller for employee behavior."""
    
    def __init__(self, employee):
        self.employee = employee
        self.tasks_completed = 0
    
    def simulate_work(self, economy_manager=None):
        """Simulate employee work actions."""
        print(f"\n--- {self.employee.name} Work Shift ---")
        
        # Choose a random task
        tasks = ["cleaning tables", "serving food", "taking orders", "restocking"]
        task = random.choice(tasks)
        
        # Perform the task
        if self.employee.perform_task(task):
            self.tasks_completed += 1
            
            # Reward through economy manager
            if economy_manager:
                if "clean" in task:
                    economy_manager.add_score(5, f"{self.employee.name} cleaned")
                economy_manager.add_score(3, f"{self.employee.name} completed {task}")
            
            print(f"{self.employee.name} completed {task}. Total tasks: {self.tasks_completed}")
            return True
        else:
            # Employee needs rest
            self.employee.rest()
            return False
