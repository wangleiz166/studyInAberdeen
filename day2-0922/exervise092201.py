#输入件数
items = int(input("enter items"))

#定义价格每个1元
price = 1

all_price = price * items

if items < 10:
    check_out_price = all_price
elif items >=10 and items <= 19:
    check_out_price = all_price * 0.8    
elif items >=20 and items <=30:
    check_out_price = all_price * 0.7
else:     
    check_out_price = all_price * 0.5

print(f"iteams is {items}, all the price is {all_price},and you need pay {check_out_price}")   