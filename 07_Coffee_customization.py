#Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso
ordersize=str(input("Order size?(Small, Medium (OR) Large?): "))
extrashot=str(input("Need extrashot of espresso? (True/False): "))

# extrashot=True
# if extrashot:
if extrashot == "True":
    coffee = ordersize + "Coffee with an extra shot of espresso"
else:
    coffee = ordersize + "Coffee"

print(f"Order: {coffee}")



