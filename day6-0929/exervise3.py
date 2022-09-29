total = 0
while True:
    try:
       age = int(input("enter"))
       if age < 3:
          total += 0
       elif age > 10:
          total += 10
             
    except:
        print("exit")
        break 


print(total)