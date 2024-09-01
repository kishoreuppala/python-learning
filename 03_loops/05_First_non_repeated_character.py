# Given a string, find the first non-repeated character.
mystring=str(input("Enter any string: "))
non_repeatable_chars=[]
for char in mystring:
    # print(char)
    if mystring.count(char) == 1:
        non_repeatable_chars.append(char)
        break   #optimisation->will break loop once it finds first non-repeated char.
print('First Non repeatable characters: ', non_repeatable_chars[0])
