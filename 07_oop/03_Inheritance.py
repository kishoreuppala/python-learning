# Inheritance: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    # brand = None
    # model = None
    def __init__(self,userBrand,userModel):
        self.brand = userBrand
        self.model = userModel
class ElectricCar(Car):
    def __init__(self,userBrand,userModel,battery_size):
        super().__init__(userBrand,userModel)   #Inherit brand, model attributes from above/up class i.e., Car
        self.battery_size = battery_size

myTesla = ElectricCar("Tesla", "Model S","85KWH")
print(myTesla.brand,myTesla.model,myTesla.battery_size)