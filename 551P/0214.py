# def factorial(n):
#     if n == 0:
#          #print('n==0')
#          return 1
#     else:
#         #print(n)
#         return n* factorial(n-1)

# number = int(input('enter number'))
# print(factorial(number))


# location = -1

# def search(array, n):
#     x = 0

#     while x < len(array):
#         if array[x] == n:
#             globals()['location'] = x
#             return True
#         x += 1

#     return False

# array = [3, 4, 5, 7, 9, 1, 2]
# y = 5

# if search(array, y):
#     print("Hurray! Found at location", location)
# else:
#     print("Oops, not found!")


location = -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            globals()['location'] = mid
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


array = [1,2,3,4,5,7,9]

target = 3

if binary_search(array,target):
    print(f"hurrary!, {location+1}")
else:
    print("not found!")