# Problem: Add a method to the Car class that displays the full name of the car (brand and model).
# Problem: Add some functinoality to an existing class

# self practice
class emp():
    def __init__(self,uName,uMobile):
        self.name = uName
        self.mobile = uMobile

    def id(self):
        # Extract first two and last two digits from mobile
        first_two = str(self.mobile)[:2]
        last_two = str(self.mobile)[-2:]
        # Return name appended with these digits
        return f"{self.name}{first_two}{last_two}"
my_details = emp("Kishore","9999999999")
print("Details: ", my_details.name,my_details.mobile)
print("ID Details: ", my_details.id())