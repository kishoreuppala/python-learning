import time
print("This is first line")
username=str(input("Enter Username: "))
print(f"Username Provided: {username}")

# Internal flow works as follows:
# >>> file=open('01_Sample.py')
# >>> file.readline()
# 'import time\n'
# >>> file.readline()
# 'print("This is first line")\n'
# >>> file.readline()
# 'username=str(input("Enter Username: "))\n'
# >>> file.readline()
# 'print(f"Username Provided: {username}")'
# >>> file.readline()
# ''
# >>> file.readline()
# ''


# Running with __next__() to produce raw output
# >>> file=open('01_Sample.py')
# >>> file.__next__() 
# 'import time\n'
# >>> file.__next__()
# 'print("This is first line")\n'
# >>> file.__next__()
# 'username=str(input("Enter Username: "))\n'
# >>> file.__next__()
# 'print(f"Username Provided: {username}")\n'
# >>> file.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# To read all lines using for loop
# for line in open('01_Sample.py').readlines()

#Print lines using for loop
# >>> for line in open('01_Sample.py'):
# ...     print(line,end='')
# ...


# Print using while loop
# >>> file=open('01_Sample.py')
# >>> while True:
# ...     line=file.readline() 
# ...     if not line: break    
# ...     print(line, end='')
# ...


# Memory references and iteration in Python -Examples "List" and "File"
# >>> myList=[1, 2, 3, 4]
# >>> I=iter(myList)
# >>> I
# <list_iterator object at 0x0000012D573E7B20>
# >>> I.__next__()
# 1
# >>> I
# <list_iterator object at 0x0000012D573E7B20>
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# NOTE: Iter() with List always point to the same loation but it will internally roate to the next item. 
#  
#
# iter() object will be AVAILABLE BY DEFAULT FOR FILES but for "List" it is not the case.
# >>> f=open('01_Sample.py')
# >>> iter(f) is f
# True
# >>> iter(f) is f.__iter__()
# True

# BELOW OUTPUT is for List
# >>> iter(myList) is myList
# False

# Dictionaries also iterables
# >>> Dict={'a': 1, 'b': 2} 
# >>> for key in Dict.keys(): 
# ...     print(key)
# ...
# a
# b

# Manual iteration - Dictionary. Both next(value) and __next__ working is same.
# IndentationError: unexpected indent
# >>> Dict={'a': 1, 'b': 2}
# >>> I=iter(Dict)
# >>> I
# <dict_keyiterator object at 0x0000012D573E05E0>
# >>> next(I)
# 'a'
# >>> next(I)
# 'b'
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# Iterating range(0,5)
# range(0, 5)
# >>> R=range(5)
# >>> iter(R)
# <range_iterator object at 0x0000012D570AAF10>
# >>> I=iter(R)
# >>> next(I)
# 0
# >>> next(I)
# 1
# >>> next(I)
# 2
# >>> next(I)
# 3
# >>> next(I)
# 4
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration