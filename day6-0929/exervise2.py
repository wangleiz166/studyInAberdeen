list = []
list2 = []
while True:
    num = int(input("enter:")) 
    if num > 0:
       list.append(num)
    elif num == 0:
        break   
    else:
       list2.append(num)

print(list)
print(list2)