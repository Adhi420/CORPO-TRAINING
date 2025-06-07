# Class and Object in Python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(self.brand, "is driving")

my_car = Car("Tesla")
my_car.drive()
