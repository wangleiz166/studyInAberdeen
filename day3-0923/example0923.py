value1 = 1
value2 = 2

def fun():
    a = input("enter aaa")
    print(a)
    global value3
    value3 = 3
    # print(value1)
    # print(value2)
    # print(value3)

fun()

print(value1)
print(value2)
print(value3)