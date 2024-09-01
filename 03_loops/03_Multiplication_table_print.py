# Print the multiplication table for a given number up to 10, but skip the fifth iteration
# 3 X 1 = 3

n=int(input("Enter any number: "))
i=1

#Using for loop
for i in range(1, 11):
    if i == 5: continue
    print(f"{n} X {i} = {n * i}")

#Using while loop
# while i < 11:
#     if i == 5: 
#         i += 1
#         continue
#     print(f"{n} X {i} = {n * i}")
#     i += 1
