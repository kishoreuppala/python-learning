# Compute the factorial of a number using a while loop
#Factorial of 5 -> 5 * 4 * 3 * 2 * 1
n=int(input("Enter any number: "))
original_number=n
i=1
while n > 0:
        # i = n * i
        i *= n
        # print(i)
        n -= 1

print(f"Factorial of {original_number} is: {i}")
