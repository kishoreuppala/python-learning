# Function that accepts any number of keyword arguments and prints them in the format key: value.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(Name="Kishore",Job="IT")
print_kwargs(Name="Joshith",Class="UKG")
print_kwargs(Age="1.5yrs")