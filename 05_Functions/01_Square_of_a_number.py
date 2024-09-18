# Calculate and return the square of a number

num=int(input("Enter any number: "))

def square(num):
    return num ** 2     # Recommended way - Use return
    # print(f"Square of {num} is: {result}")
     

def cube(num):
    return num ** 3
    # print(f"Cube root of {num} is: {result}")

result=square(num)
result2=cube(num)

print(f"Square of {num} is: {result}")
print(f"Cube root of {num} is: {result2}")


#Logic without function
# num=int(input("Enter any number: "))
# square= num ** 2
# print(f"Square of {num} is: {square}")
