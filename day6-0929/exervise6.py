
while True:
    try:
        long_value = float(input("enter:"))
        time_value = float(input("enter:"))
        print(time_value * long_value)
        break
    except:
        print("error") 