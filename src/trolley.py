"""Trolley system to carry boxes."""

class Trolley:
    """Trolley class for carrying boxes."""
    
    def __init__(self):
        """Initialize the trolley."""
        self.boxes = []
        self.capacity = 10
    
    def add_box(self, box):
        """Add a box to the trolley.
        
        Args:
            box: The box item to add
        """
        if len(self.boxes) < self.capacity:
            self.boxes.append(box)
            print(f"Added box to trolley. Total boxes: {len(self.boxes)}")
        else:
            print("Trolley is full!")
    
    def remove_box(self):
        """Remove a box from the trolley."""
        if self.boxes:
            box = self.boxes.pop()
            print(f"Removed box from trolley. Remaining boxes: {len(self.boxes)}")
            return box
        else:
            print("Trolley is empty!")
            return None
