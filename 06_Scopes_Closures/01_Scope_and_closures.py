username = "Uppala"

def func1():
    username = "Kishore"
    # print(username)

print(username) #Will prefer global variable only
func1() #Will print "Kishore"
# =======================

def func2():
    global x    #Global keyword should be avoided all the times.
    x = 33

func2()
print(x)


def f1():
    # x = 99    #If this x is disabled then it will print global x value
    def f2():
        print (x)   #Closure example
    f2()
f1()
myResult = f1()
# myResult()

# Closure Example
def closure_example(num):
    def actual(x):
        return x ** num
    return actual

#Sample closure values replacement
# def closure_example(2):
    # def actual(x):
        # return x ** 2
        # return actual

a = closure_example(2)
b = closure_example(3)

# print(a)  #Print memory location
# print(b)
print(a(2))
print(b(3))
