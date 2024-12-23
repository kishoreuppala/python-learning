# Use a property decorator in the Car class to make the model attribute read-only

class Car:
    total_car_objects = 0
    
    def __init__(self,userBrand,userModel):
        # self.brand = userBrand
        # To make it private use __(double underscore). Will be accessible within in the class but not outside.
        self.__brand = userBrand
        self.__model = userModel
        # self.total_car_objects += 1 # Not recommended
        Car.total_car_objects += 1
    
    @property           # Makes - we can call model using only this method, and we can't overwrite model.
    def model(self):        
        return self.__model

myCar1 = Car("Tata", "Safari")
# myCar1.model="NewModel"

print(myCar1.model)