# Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)
pet=str(input("Pet Species: "))
age=int(input("Enter Age: "))

if pet == "Dog":
    if age < 2:
        food="Puppy Food"
    else: food="Moderate amount of Dog food"
elif pet == "Cat":
    if age < 5:
        food="Junior Cat Food"
    else: food="Senior Cat Food"
else: 
    print(f"Recommending food only for Dogs and Cats.")
    exit()

print(f"Recommendation for {age} years {pet} is: {food}")
