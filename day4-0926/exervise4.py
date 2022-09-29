# def getHighest(list):
#     lenValue = len(list) - 1
#     highest = 0
#     for k,num in enumerate(list):
#          i = k - lenValue
#          if num > highest:
#             highest = num
#          if  i == 0:
#             break
                    
#     return highest

# times = int(input("enter:"))

# list = []

# for i in range(times):
#     i = i+1
#     num = int(input("enter num"))
#     list.append(num)

# hightest = getHighest(list)    
# print(hightest)

number = int(input("Enter a number: "))
highest = number

while number != 0:
    if number > highest:
        highest = number
    number = int(input("Enter a number: "))

print("Highest number: ", highest)

