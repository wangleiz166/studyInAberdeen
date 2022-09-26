
# for i in range(5, 101):
#      if i % 5 == 0:
#         print(i)


# num1 = int(input("enter:"))
# num2 = int(input("enter:"))
# num3 = int(input("enter:"))
# num4 = int(input("enter:"))
# num5 = int(input("enter:"))

# count = num1+num2+num3+num4+num5

# print(count)


# for i in range(5):
# num = int(input("enter:"))
# count = count + num

# print(count)

# list = [1, 2, 3, 4, 5]
# for k, v in enumerate(list):
# print(k)
# print(v)

# num = 10
# while(num>0):
# num += num
# print(num)
# if num > 100:
# break


# import random

# num = random.randint(1, 10)

# user_num = int(input("enter:"))

# while user_num != num:
#     if user_num > num:
#         print("Too high, try again")
#     else:
#         print("Too low, try again")

#     user_num = int(input("enter:"))

# print("right")     


# for i in range(1,10):
#     if i == 3:
#         continue
#     print(i)

# for i in range(2,11):
#     print(i)

# i = 1
# while i < 10:
#     i = i + 1
#     print(i)


def doubles(num):
    num = num * 2
    return num

num = int(input("enter:"))  

for i in range(3):
   num = doubles(num)
   print(num)
