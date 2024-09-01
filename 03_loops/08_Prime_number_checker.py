# Check if a number is prime
number=int(input("Enter any number: "))
#Assume it is a prime unless we find a divisor
is_prime=True

if number > 1:
    #Loop and check if it is divisible by numbers within its range
    for i in range(2, number):
        if (number % i) == 0:
            is_prime=False
            break
    if is_prime:
        print(f"{number} is a Prime number.")
    else:
        print(f"{number} is NOT a prime number.")
else:
    print(f"{number} is NOT a prime number.")