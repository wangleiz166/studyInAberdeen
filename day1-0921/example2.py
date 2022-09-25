#print("i love python")

#name = "yellow"
#print(name)

import datetime


name = input("Enter the name: ")
age = int(input("Enter the age: "))


currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
now_year = int(date.strftime("%Y"))

less = int(100-age) 
year = int(now_year+less)
print(f"name is {name} and in {year} will turn 100 years old")






