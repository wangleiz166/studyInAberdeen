import math

x1 = int(input("enter x1"))
y1 = int(input("enter y1"))
x2 = int(input("enter x2"))
y2 = int(input("enter y2"))

#1
math_value = math.sqrt((x2-x1)**2+((y2-y1)**2))
#2
math_value2 = ((x2-x1)**2+(y2-y1)**2)**0.5

print(f"the math value is {math_value} and {math_value2}")