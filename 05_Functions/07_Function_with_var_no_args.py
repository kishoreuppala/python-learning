# function that takes variable number of arguments and returns their sum
def sum_all(*args):
    # for - just for testing
    print(args)
    for i in args:
        print(i * 2)
    #Return sum
    return sum(args)

print(sum_all(5,5))
# print(sum_all(5,5,5))
# print(sum_all(5,5,5,5))


