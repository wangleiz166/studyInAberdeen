#only_even([1,3,5,2,1])
# def only_pos(t):
#    result = []
#    for s in t:
#       if s >= 0:
#       result.append(s)
# return result


def only_even(list):
    result = []
    for s in list:
        if s%2 == 0:
           result.append(s)

    return result        

print(only_even([1,3,5,2,1]))