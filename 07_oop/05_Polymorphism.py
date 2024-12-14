# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it

# Steps:
#     1. create get brand method
#     2. Use __brand to make it private

class Car:
    # brand = None
    # model = None
    def __init__(self,userBrand,userModel):
        # self.brand = userBrand
        # To make it private use __(double underscore). Will be accessible within in the class but not outside.
        self.__brand = userBrand
        self.model = userModel
    
    def get_brand(self):
        return self.__brand + "!"
    
    # polymorphism example
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self,userBrand,userModel,battery_size):
        super().__init__(userBrand,userModel)   #Inherit brand, model attributes from above/up class i.e., Car
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge..."

myCar = Car("Tata", "Safari")
print(myCar.fuel_type())

myTesla = ElectricCar("Tesla", "Model S", "85KWH")
print(myTesla.fuel_type())