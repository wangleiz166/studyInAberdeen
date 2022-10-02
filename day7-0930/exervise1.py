def sortAndSearch(count):
     list = []
     for i in range(count):
         num = int(input("enter:"))
         list.append(num)

     print(bubbleSort(list))
     
     find_value = int(input("enter your find num:"))
     re = BinarySearch(find_value,list)
     if re == -1:
        print("buzai")
     else:
        print("zai")   

def bubbleSort(arr):
     n = len(arr)
     # 遍历所有数组元素
     for i in range(n):
         for j in range(0, n-i-1):
             if arr[j] > arr[j+1] :
                 arr[j], arr[j+1] = arr[j+1], arr[j]

     return arr   


def BinarySearch(item, sequence):
    low = 0
    high = len(sequence)-1
    pos = -1
    while low <= high and pos == -1:
        mid = (low + high)//2
        if sequence[mid] < item:
            low = mid + 1
        elif sequence[mid] > item:
            high = mid - 1
        else:
            pos= mid

    return pos

times = int(input("enter times:"))
sortAndSearch(times)  