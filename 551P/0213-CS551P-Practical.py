def very_easy():

    long = float(input("insert long feet"))
    width = float(input("insert width feet"))

    area = long * width

    print(f"area is {area} feet")

#very_easy()

#2
def easy():
    zodiac_list = ["dragon","snake","horse","sheep","monkey","rooster","dog","pig","rat","Ox","Tiger","Hare"]
    year = int(input("insert your year"))

    if year > 2000 :
        key = int((year-2000)%12)
        print(f"zodiac is {zodiac_list[key]}")
    
    if year == 2000:
        print(f"zodiac is dragon")

    if year < 2000:
        key = 12-int((2000-year)%12)
        print(f"zodiac is {zodiac_list[key]}")

#3

#easy()

def easy2():
      year = int(input("insert your year"))
      
      if year%400 == 0:
          print("it is a leap year")
      else:
        if year%100 == 0:
          print("it is not a leap year")
        elif year%4 == 0:
          print("it is a leap year")
        else:
          print("it is not a leap year")
#easy2()

#5

def medium1():
    str = input("insert your word")
    
    length = len(str)
    half_length = length // 2

    front_half_str = ''
    backward_str = ''

    for i in range(half_length):
        front_half_str += str[i]
        backward_str +=str[-(i+1)]

    #print(backward_str)
    if front_half_str == backward_str:
        print("it is a palindrome")

#medium1()

#6

#A prime number is an integer greater than 1.
#It is only divisible by 1 and itself.

def medium2():
    number = int(input("insert your word"))
    
    if number < 1:
        print("it is not a prime")
        
    for i in range(2,number):
        if number%i == 0:
            print("it is not a prime")
            return False
            
    return True

#7

import re

def is_good_password(password):
    if len(password) < 8:
        return False
    elif not re.search('[A-Z]', password):
        return False
    elif not re.search('[a-z]', password):
        return False
    elif not re.search('[0-9]', password):
        return False
    else:
        return True


password = input('Please enter a password: ')
if is_good_password(password):
    print('Good password!')
else:
    print('Bad password!')
    


#8
import random

# Generate 6 random numbers between 1 and 49
numbers = random.sample(range(1, 50), 6)

numbers.sort()

print(numbers)

#9 默认参数默认值只会被定义一次  后面就不会再被重置了
#[0, 1]
#[3,2,1,0,1,4]
#[0,1,0,1,4]


#10
with open(__file__) as f:
    print(f.read())

#该程序使用内置open函数打开包含当前代码 ( __file__) 的文件。然后，它读取文件的内容并使用print函数将它们打印到控制台。这会将程序的源代码输出到控制台，有效地创建它自己的副本。

class Parent:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}!")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def say_hello(self):
        super().say_hello()
        print(f"I'm {self.age} years old.")

child = Child("Alice", 7)
child.say_hello()  # 输出 "Hello, Alice!" 和 "I'm 7 years old."
