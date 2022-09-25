#  The speed of light c,
#  is approximately 3 x 108 meters per second. 
#  Write a program that prompts theuser to input a time in seconds and 
#  displays that the distance that light travels in this period.
#  Displaythat distances in meters, kilometres and miles

second = int(input("enter second:"))

light_speed = 3*10**8

meters = second*light_speed

kilometres = int(meters/1000)

distances_meters = int(kilometres*0.612)

print(f"meters is {meters}.m")
print(f"kilometres is {kilometres}.km")
print(f"distances_meters is {distances_meters}.mi")