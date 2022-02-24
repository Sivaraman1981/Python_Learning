#Program1
#Python Program to find sum of array

Method1:

array1 = [12,3,4,15]
sumofarray= sum(array1)

print ("Sum of the array is",sumofarray)

Method2:

def sumofarray(array1):
    sum = 0
    for i in array1:
        sum =sum + i
    return (sum)

array2=[12,3,4,15]

sumofarray1= sumofarray(array2)

print ("Sum of the array is",sumofarray1)

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Sum of the array is 34

#Program2
#Python Program to find max of array

Method1:
array1 = [12,3,4,15]
maxofarray= max(array1)

print ("Sum of the array is",maxofarray)

Method2:
def maxofarray(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max=arr[i]
    return max

arr = [10, 324, 45, 90, 9808]
n = len(arr)
largestnois = maxofarray(arr,n)
print ("Largest in given array is",largestnois)

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Largest in given array is 9808

#Program3
#Python Program for array rotation
# slicing approach to rotate the array

def rotateList(arr,d,n):
  arr[:]=arr[d:n]+arr[0:d]
  return arr
 
arr = [1, 2, 3, 4, 5, 6]
print(arr)
print("Rotated list is")
print(rotateList(arr,2,len(arr))) 

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
[1, 2, 3, 4, 5, 6]
Rotated list is
[3, 4, 5, 6, 1, 2]

#Program4
#Python Program for Reversal algorithm for array rotation

 
# Function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    n = len(arr)
    rverseArray(arr, 0, d-1)
    rverseArray(arr, d, n-1)
    rverseArray(arr, 0, n-1)

    #print("leftRotate call::",arr)
#Function reverse array
    
def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
    #print("rverseArray call::",arr)        
# Function to print an array
def printArray(arr):
    #print("printarray call::",arr)
    for i in range(0, len(arr)):
        print (arr[i])
  
# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
print("before function start::",arr)
leftRotate(arr, 2) # Rotate array by 2
printArray(arr)

 
Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
before function start:: [1, 2, 3, 4, 5, 6, 7]
3
4
5
6
7
1
2

#Program 5
#Python Program for Find reminder of array multiplication divided by n

arr=[3,2,5,8,6,1,4]
arr1=[]
a=1
n=4

for i in range(0,len(arr)):
    #print("a*arr[i]::",a*arr[i])
    a=a*arr[i]
    arr1.append(a)
print(arr)
print(arr1)
print(arr1[-1]%n)

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
[3, 2, 5, 8, 6, 1, 4]
[3, 6, 30, 240, 1440, 1440, 5760]
0


