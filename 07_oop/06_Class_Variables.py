# Add a class variable to Car that keeps track of the number of cars created

class Car:
    total_car_objects = 0
    
    def __init__(self,userBrand,userModel):
        # self.brand = userBrand
        # To make it private use __(double underscore). Will be accessible within in the class but not outside.
        self.__brand = userBrand
        self.model = userModel
        # self.total_car_objects += 1 # Not recommended
        Car.total_car_objects += 1

myCar1 = Car("Tata", "Safari")
myCar2 = Car("Tata","Nexon")
# myCar3 = Car("Maruthi", "Suzuki")
print("Total Car class objects: ", Car.total_car_objects)
# print("Not recommended way to query same: ", myCar2.total_car_objects)