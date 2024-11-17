    # Create a Car class with attributes like brand and model. Then create an instance of this class

class Car:
    # brand = None
    # model = None
    def __init__(self,userBrand,userModel):
        self.brand = userBrand
        self.model = userModel

my_car = Car("Toyota", "Corolla")
print("My Car: ", my_car.brand,my_car.model)

# self practice
class emp():
    def __init__(self,uName,uMobile):
        self.name = uName
        self.mobile = uMobile
my_details = emp("Kishore","9999999999")
print("Details: ", my_details.name,my_details.mobile)