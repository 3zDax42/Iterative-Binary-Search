def Is_It_Prime(num):
    for i in range(num):
        dividend = i+2
        if dividend == (num//2):
            return True
        if (num % dividend) == 0:
            return False
        print (dividend)
print(Is_It_Prime(2))

def binary_Search(arr, low, high, x):
    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
        

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_Search(arr, 0, len(arr)-1, x)
if result != -1:
    print ("Element is present at index", result)
else:
    print("Element is null")
        
