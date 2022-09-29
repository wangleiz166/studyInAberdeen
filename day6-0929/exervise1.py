import random
 
num1 = random.randint(0,999)
num2 = random.randint(0,999)
print(f"{num1} + {num2} = ?")
guess = float(input("enter"))

num3 = num1 + num2



if guess == num3:
    print("yes")
else:
    print("no")    