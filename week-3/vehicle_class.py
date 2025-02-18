class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self,numbers_of_doors,make,model):
        super().__init__(make,model)
        self.__numbers_of_doors = numbers_of_doors

    def describe(self):
        return f"It's a car which has , doors:{self._Car__numbers_of_doors},make:{self.make},model:{self.model}"

class Bike(Vehicle):
    def __init__(self,while_size,type_bike,make,model):
        super().__init__(make,model)
        self.while_size = while_size
        self.type_bike = type_bike
    def describe (self):
        return (f"It's a motor bike which has , make:{self.make},model:{self.model},"
                f"type of bike:{self.type_bike},while size: {self.while_size}")


vehicle = Vehicle('Toyota',"Corolla")
print(vehicle.make)
print(vehicle.model)
car = Car(4,"Honda","CR-V")
bike = Bike("700c","Narrow and smooth","BMC Roadmachine","Road bikes")
print(car.describe())
print(bike.describe())
print(car._Car__numbers_of_doors)

