# 编写一个函数，将三个数字作为参数，
# 并将这些参数的中值作为其结果返回。
# 包括一个主程序，从用户那里读取三个数值，
# 并显示它们的中位数。


def get_ascending_order(num1,num2,num3):
    ascend_num1 = int(num1/2)
    ascend_num2 = int(num2/2)
    ascend_num3 = int(num3/2)
     
    list = [int(num1),int(num2),int(num3)]
    list.sort()

    print(f"list is {list}")

    middle_num = int(list[1])

    print(f"middle num js {middle_num}")
    print(f"num1's ascending order is {ascend_num1}")
    print(f"num2's ascending order is {ascend_num2}")
    print(f"num3's ascending order is {ascend_num3}")

num1 = int(input("enter num1"))
num2 = int(input("enter num2"))
num3 = int(input("enter num3"))


get_ascending_order(num1,num2,num3)