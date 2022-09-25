#编写一个程序，询问用户两个房间的长度和宽度。然后它应该通知用户说这些区域是否相同，或者如果不同，哪个房间更大

user1_width = int(input("user1 enter width:"))
user1_high = int(input("user1 enter high:"))
user2_width = int(input("user2 enter width:"))
user2_high = int(input("user2 enter high:"))

user1_area = user1_width*user1_high
user2_area = user2_width*user2_high

if user1_area == user2_area:
    print("user1 = user2")
else:
    if user1_area > user2_area:
       print("user1 is bigger than user2")
    else:
       print("user2 is bigger than user1")
