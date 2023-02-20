while True:
    a = eval(input("please input the first number :"))
    b = eval(input("please input the second number :"))
    c = eval(input("please input the last number :"))
    if type(a) != int or type(b) != int or type(c) != int:
        print("you input  numbers are wrong,please input again ")
    else:
        break


def no_three_sum(a, b, c):
    sum = 0
    if a != fix_three(a):
        a = 0
    elif b != fix_three(b):
        b = 0
    elif c != fix_three(c):
        c = 0
    sum = a+b+c
    print(sum)


def fix_three(n):
    if n % 3 == 0 and (n < 20 or n > 29):
        n = 0

    return n


no_three_sum(a, b, c)
