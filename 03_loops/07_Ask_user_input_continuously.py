# Keep asking the user for input until they enter a number between 1 and 10
number=int(input("Enter a number between 1 and 10: "))
while True:
    if 1 <= number <= 10:
        print(f"Viola! You entered: {number}")
        break
    else:
        number=int(input("Enter a number between 1 and 10: "))
