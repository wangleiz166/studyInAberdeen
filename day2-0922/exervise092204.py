# 在公历中，一个月的长度从 28 天到 31 天不等。
# 编写一个程序，从用户那里读取月份的名称作为字符串。
# 然后显示该月的天数。提示：如果月份是二月，
# 则应显示“28 或 29 天”以考虑闰年


month = int(input("enter month:"))

big_month_list = [1,3,5,7,8,10,12]

if (month in big_month_list):
    print("month is 31 days")
elif month == 2:
    print("month is 28 or 29 days")
else:
    print("month is 30 days")    

