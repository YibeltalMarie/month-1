

class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

class Car():
    def __init__(self,numbers_of_doors,make,model):
        self.__numbers_of_doors = numbers_of_doors

    def describe(self):
        return "They have doors,tire,break"

class Bike(Vehicle):
    def describe (self):
        return "They have two motor"

vehicle = Vehicle(20,"2025-model")
print(vehicle.make)
print(vehicle.model)
car = Car(4,2024,"model")
print(car.describe())
print(car._Car__numbers_of_doors)

