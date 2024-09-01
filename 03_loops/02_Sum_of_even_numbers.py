# Calculate the sum of even numbers up to a given number n.
n = int(input("Enter a number: "))
i = 1
sum=0
myarray = []

# Using while loop
# while i < n:
#     if (i % 2 == 0):
#         myarray.append(i)
#         sum += i
#         print(i)
#         print(sum)        
#     i += 1

#Using for loop
for i in range(1, n+1):
    if (i % 2 == 0):
        myarray.append(i)
        sum += i
        # print(i)
        # print(sum)

print(f"List of Even numbers upto given number: {n} -> {myarray}")
print(f"Sum of even numbers: {sum}")
    

        

