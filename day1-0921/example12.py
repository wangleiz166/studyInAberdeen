#Write a program that asks the user for their height in feet and inches and converts it into centimeter.
#1英寸= 2.54厘米
#1英尺= 12英寸

type = int(input("enter your height in feet type(1:inches 2:converts)"))

if type == 1:
    #英寸
    height = int(input("enter your height in feet by inches:"))
    cm_height = height*2.54
else:
    #英尺 
    height = int(input("enter your height in feet by centimeter:"))
    cm_height = height*2.54*12

print(f"your height is {cm_height}.cm")    


