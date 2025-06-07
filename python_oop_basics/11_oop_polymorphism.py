# Polymorphism in Python
class Bird:
    def move(self):
        print("Bird flies")

class Fish:
    def move(self):
        print("Fish swims")

def show_movement(animal):
    animal.move()

show_movement(Bird())
show_movement(Fish())
