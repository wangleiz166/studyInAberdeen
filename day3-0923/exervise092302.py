# 费马最后定理（有时也称为费马猜想，特别是在较早的文本中）指出，
# 没有三个正整数a、b和c满足方程对于任何大于2的整数值，
# 编写一个名为checkFermat的函数，该函数需要四个参数（a、b、c和n），
# 检查费马定理是否成立，
# 如果n大于2，并且证明该定理是真的，
# 那么程序应该打印，"天哪，费马错了！" 
# 否则，程序应该打印："不，这行不通。
# "有趣的事实是，安德鲁-怀尔斯教授证明了费马是错的，并获得了诺贝尔奖

a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
n = int(input("enter n"))

def checkFermat(a,b,c,n):
    c_value = c**n
    ab_value = a**n+b**n 
    if c_value == ab_value:
        print("true")
    else:
        if n>2:
          print("Holysmokes, Fermat was wrong!")
        else:
          print("No, that doesn’t work")

checkFermat(a,b,c,n)
