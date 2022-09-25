# 编写一个名为gcd的函数，它接收两个数字（x和y）
# 并通过采用欧几里得算法返回这些数字的最大公除数。
# 假设x大于y，你必须遵循这个算法：用x除以y，
# 得到余数r当r不同于0时将x设为y的值将y设为r的值将r设为x除以y的余数返回
# gcd即y通过用一些测试数据进行测试，确保该函数工作。
# 你可以在python shell中测试这个函数。想一想可能出现的情况：
# ● 两个质数● 两个相同的数● 两个有公因数的数● 两个没有公因数的数

def gcd(x,y):
   r = x%y
   if r != 0:
      x = y
      y = r
      r = x%y 

   return r   

x = int(input("enter x"))
y = int(input("enter y"))

print(gcd(x,y))


