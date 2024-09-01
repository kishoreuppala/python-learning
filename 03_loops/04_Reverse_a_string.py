# Reverse a string using a loop
mystring=str(input("Enter any string: "))
reversed_string=""
for character in mystring:
    # print(str)
    reversed_string = character + reversed_string
    # print(reversed_string)
print(f"Reversed string: {reversed_string}")
    