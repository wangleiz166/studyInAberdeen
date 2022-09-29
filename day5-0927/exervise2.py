#sumDigits("234") → 9

def sumDigits(str):
    total = 0
    for i in range(len(str)):
         value = int(str[i])
         total += value

    return total


print(sumDigits("234"))         
