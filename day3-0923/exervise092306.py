# 如果给你三根棍子，你可能会也可能不会把它们排列成三角形。
# 例如，如果其中一根长 12 英寸，另外两根长 1 英寸，很明显，您将无法让短棍在中间相遇。
# 对于任意三个长度，有一个简单的测试，看是否有可能形成三角形：
# 如果三个长度中的任何一个大于其他两个长度之和，则不能形成三角形。
# 否则，可以。 （如果两个长度之和等于第三个，它们形成所谓的“退化”三角形）。
# 编写一个名为 is_triangle 的函数，它接受三个整数作为参数，
# 并根据您是否可以形成三角形返回真或假 从给定长度的棍子。
# 接下来，编写程序提示用户输入三个棍子长度并使用 is_triangle 检查给定长度的棍子是否可以形成三角形并向用户显示消息

def is_triangle(l1,l2,l3):
   if l1>l2+l3:
      return False
   elif l2>l1+l3:
      return False
   elif l3>l1+l2:
      return False
   else:
      return True

l1 = int(input("enter l1"))
l2 = int(input("enter l2"))
l3 = int(input("enter l3"))      

if is_triangle(l1,l2,l3):
    print("it's can triangle")
else:
    print("it's cant't triangle")    