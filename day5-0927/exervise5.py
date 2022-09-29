from audioop import lin2lin


import math

def make_number(list):
    for i in list:
        print(i)
        pow_value = math.pow(i,2)
        print(pow_value)
        g_value = i ** 0.5
        print(g_value)


make_number([18, 25, 3, 88, 60, 22, 89, 99, 20, 150])