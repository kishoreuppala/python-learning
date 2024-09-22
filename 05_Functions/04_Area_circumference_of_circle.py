# Function that returns both the area and circumference of a circle given its radius

import math
def find_circle_stats(radius):
    area=math.pi * radius ** 2
    circumference=2*math.pi*radius
    return area, circumference

a, c = find_circle_stats(2)
print(f"Area: {a:.2f}, \nCircumference: {c:.2f}") #:.2f ->To display two decimal numbers
    
