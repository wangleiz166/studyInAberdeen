def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1

Iterable = [0,1,2,3]
Iterable.index(1)
value = 1
print(linear_search(value,Iterable))