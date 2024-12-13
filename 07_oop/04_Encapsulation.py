# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it

# Steps:
#     1. create get brand method
#     2. Use __brand to make it private

class Car:
    # brand = None
    # model = None
    def __init__(self,userBrand,userModel):
        # self.brand = userBrand
        # To make it private use __(double underscore)
        self.__brand = userBrand
        self.model = userModel
    
    def get_brand(self):
        return self.__brand + "!"

myTesla = Car("Tesla", "Model S")
# print(myTesla.__brand)
print(myTesla.get_brand())