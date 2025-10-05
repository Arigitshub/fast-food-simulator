class Trolley:
    def __init__(self):
        self.contents = []

    def add_box(self, box_name):
        self.contents.append(box_name)
        print(f"Added {box_name} to trolley.")

    def remove_box(self, box_name):
        if box_name in self.contents:
            self.contents.remove(box_name)
            print(f"Removed {box_name} from trolley.")
