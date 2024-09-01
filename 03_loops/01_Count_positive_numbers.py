# Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count  = 0
positive_numbers_array = []
for number in numbers:
    # print(number)
    if number > 0:
        count += 1
        positive_numbers_array.append(number)
print(f"Positive numbers: {positive_numbers_array}")
print(f"Count of postive numbers: {count}")