import datetime

name = input("Enter the name: ")
birthday = int(input("Enter you birthday year eg:1991"))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
now_year = int(date.strftime("%Y"))

age = int(now_year-birthday)
less = int(100-age) 
year = int(now_year+less)
print(f"name is {name} and in {year} will turn 100 years old")


