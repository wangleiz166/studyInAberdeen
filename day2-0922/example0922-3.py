#Write a program that asks the user for the temperature of water and itdisplays as a result 
# the state of the water (e.g. liquid, gas, ice)

temperature = int(input("enter the temperature:"))

if temperature < 0:
   print("ice state")
elif temperature <= 212 and temperature > 32:
   print("gas state")
else:
   print("liquid state")       