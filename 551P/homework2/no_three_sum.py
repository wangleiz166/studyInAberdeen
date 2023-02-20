# by Lei Wang
# Student ID：52210762
# 01/10/22 23:59
# github: https://github.com/wangleiz166/studyInAberdeen

# Write a program called “no_three_sum”, which take three integer values a, b, and c as
# arguments and returns their sum. However, if any of the values is a multiple of three e.g. 3, 6, 9,
# 12, … then that value counts as 0, except the multiples of three between 20 and 29. Write a
# separate helper function "def fix_three(n): "that takes in an integer value and returns that value
# fixed for the rule. Then make use of this helper function through “no_three_sum”


while True:
    try:
        # enter number a and check
        a = int(input("please enter number a:"))
        break
    except:
        print("number a type wrong! please enter int")
while True:
    try:
        # enter number b and check
        b = int(input("please enter number b:"))
        break
    except:
        print("number b type wrong! please enter int")
while True:
    try:
        # enter number c and check
        c = int(input("please enter number c:"))
        break
    except:
        print("number c type wrong! please enter int")

# main function
# parameter: n int
# return: n int


def fix_three(n):
    if n % 3 == 0 and n not in [i for i in range(20, 30)]:
        n = 0
    return n

# main function
# parameter: a,b,c int
# return: int


def no_three_sum(a, b, c):
    sum = fix_three(a) + fix_three(b) + fix_three(c)
    return sum


print(no_three_sum(a, b, c))
