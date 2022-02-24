#searching sorting
#Program1  
#Python Program for Linear Search

def l_search(arr,n):
    for i in range(len(arr)):
        if arr[i]==n:
            return i
    return -1
arr=(10, 20, 80, 30, 60, 50, 110, 100, 130, 170) 
n=60
print(l_search(arr,n))

output:


========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
4


#Program2 
#Python Program for Binary Search (Recursive and Iterative)

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 4
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Element is present at index 2


#Program3 
#Python Program for Insertion Sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
arr = [22, 15, 9, 17, 6,3]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])

Output:

========================================= RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Sorted array is:
3
6
9
15
17
22


#Program4 
#Python Program for Bubble Sort

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [64,14, 45, 12, 29, 11, 80]
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i],end=" ")

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Sorted array is:
 11  12  14  29  45  64  80 
