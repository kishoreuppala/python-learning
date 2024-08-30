age = int(input ("Enter Your age: "))
day = "Wednesday"

price = 12 if age >= 18 else 8

if day ==  "Wednesday":
    price-=2

print(f"Ticket price for you is ${price}")

# children_price = 8
# adult_price = 12

# if day == "Wednesday":
#     children_price-=2
#     adult_price-=2
#     if age < 18:
#         print(f"Ticket price for you is: ${children_price}")
#     elif age >= 18:
#         print(f"Ticket price for you is: ${adult_price}")
# else:
#     if age < 18:
#         print(f"Ticket price for you is: ${children_price}")
#     elif age >= 18:
#         print(f"Ticket price for you is: ${adult_price}")
    
              