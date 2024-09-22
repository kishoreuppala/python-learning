#  Function that greets a user. If no name is provided, it should greet with a default name.

#Method1
# def greet(user="Guest"):
#     print(f"Welcome, {user}!")
# # greet(input("Enter username: "))
# greet("Kishore")

#Method2
def greet():
    user=input("Enter Username: ")
    if not user:
        user="Guest"
    print(f"Welcome, {user}!")

greet()

