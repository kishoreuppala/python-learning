# Add a static method to the Car class that returns a general description of a car.

# Description
# Class can access the static method but not the objects
class Car:
    total_car_objects = 0
    
    def __init__(self,userBrand,userModel):
        # self.brand = userBrand
        # To make it private use __(double underscore). Will be accessible within in the class but not outside.
        self.__brand = userBrand
        self.model = userModel
        # self.total_car_objects += 1 # Not recommended
        Car.total_car_objects += 1

    @staticmethod
    def general_description():  # "self" not required if it is a static method, because it is accessible to class only but not to objects
        return "Description of the Car."

myCar1 = Car("Tata", "Safari")

# print(myCar1.__general_description())
print(Car.general_description())