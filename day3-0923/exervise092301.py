#给定以下代码：
#  不使用 Python，你认为 x 的值是多少？ 
# 现在运行你的代码，看看你是否猜对了！ 
# 使用 www.pythontutor.com 了解 x 的值如何变化。
#  在 Python 中输入代码，如果复制/粘贴会出现语法错误！

def mysteryNumber(x):
    x= x*x
    print("The value of x is now ", x)
    x = 2
    print("Value of x is", x)

x = 1    
mysteryNumber(x)

print("The value of x after calling mysterNumber is: ", x)