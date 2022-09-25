# 2010年2月5日被称为一个神奇的日期，
# 因为当它被写成如下时，
# 月份*日期等于年份。5/2/10. 
# 编写一个函数，作为参数接收日、月和两位数的年，
# 如果该年是一个神奇的日期，则返回真，
# 否则返回假。


def magic_year(day,month,year):
    day_month_value = day*month
    if day_month_value == year:
        return True
    else:
        return False

day = int(input("enter day"))
month = int(input("enter month"))
year = int(input("enter year"))

is_true = magic_year(day,month,year)

if is_true:
    print("is true")
else:
    print("is false")    

