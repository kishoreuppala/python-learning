age=int(input ("Enter age: \n"))

if age < 13:
    print("Child")
elif age < 19:
    print("Teenager")
elif age < 59:
    print("Adult")
else:
    print("Senior")