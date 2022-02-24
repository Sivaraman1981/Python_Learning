#List
#Program1
#Python program to interchange first and last elements in a list

def interchange_list(list):
    temp=0
    temp=list[0]
    list[0]=list[-1]
    list[-1]=temp
    

list=[11,54,60,98,26]

interchange_list(list)
print(list)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
[26, 54, 60, 98, 11]

#Program2
#Python program to swap two elements in a list

def s_list(list,p3,p4):

      list[p3],list[p4]=list[p4],list[p3]
        
list=[23,12,32,54,65,76,89]

p3=3
p4=4
print("Before Swap:::",list)
s_list(list,p3,p4)
print("After Swap:::",list)


output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Before Swap::: [23, 12, 32, 54, 65, 76, 89]
After Swap::: [23, 12, 32, 65, 54, 76, 89]

#Program3
#Python program Ways to find length of list

Method1:

a = []
a.append("Hello")
a.append("Geeks")
a.append("For")
a.append("Geeks")
print("The list is: ", (a))
print("The length of list is method1: ", len(a))

n = len([10, 20, 30])
print("The length of list is method2: ", n)

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
The list is:  ['Hello', 'Geeks', 'For', 'Geeks']
The length of list is method1:  4
The length of list is method2:  3

#Program4
#Python program Ways to find length of list

test_list = [ 1, 6, 3, 5, 3, 4 ]
print("Checking if 4 exists in list ( using loop ) :method1 ")

for i in test_list:
    if(i == 4) :
        print ("Element Exists")

print("Checking if 4 exists in list ( using in ) ::method2 ")
if (4 in test_list):
    print ("Element Exists")

test_list = [10, 15, 23, 17, 44, 28]
 
print("Checking if 15 exists in list:method13")
exist_count = test_list.count(15)
 
if exist_count > 0:
    print("Yes, 15 exists in list")
else:
    print("No, 15 does not exists in list")


Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Checking if 4 exists in list ( using loop ) :method1 
Element Exists
Checking if 4 exists in list ( using in ) ::method2 
Element Exists
Checking if 15 exists in list:method13
Yes, 15 exists in list

#Program5
#Python program Different ways to clear a list in Python


test_list = [10, 15, 23, 17, 44, 28]
print('Before clear:Method1', test_list) 
test_list.clear()
print('After clear:Method1', test_list) 

test_list1 = [10, 15, 23, 17, 44, 28]
test_list2 = [11, 5, 22, 7, 4, 8]
print('Before clear:Method2', test_list1) 
del test_list1[:]
print('After clear:Method2', test_list1) 

print('Before clear:Method3', test_list2) 
test_list2 =[]
print('After clear:Method3', test_list2) 

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Before clear:Method1 [10, 15, 23, 17, 44, 28]
After clear:Method1 []
Before clear:Method2 [10, 15, 23, 17, 44, 28]
After clear:Method2 []
Before clear:Method3 [11, 5, 22, 7, 4, 8]
After clear:Method3 []

#Program6
#Reversing a List in Python


lst = [10, 11, 12, 13, 14, 15]
print("Before reverse:Method1",lst)
new_lst = lst[::-1]
print("After reverse:Method1",new_lst)

def Reverse(lst):
    lst.reverse()
    return lst
     
lst = [10, 11, 12, 13, 14, 15]
print("After reverse:Method2",Reverse(lst))

def Reverse1(lst):
    return [ele for ele in reversed(lst)]
     
lst = [10, 11, 12, 13, 14, 15]
print("After reverse:Method3",Reverse1(lst))

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Before reverse:Method1 [10, 11, 12, 13, 14, 15]
After reverse:Method1 [15, 14, 13, 12, 11, 10]
After reverse:Method2 [15, 14, 13, 12, 11, 10]
After reverse:Method3 [15, 14, 13, 12, 11, 10]

#Program7
#Python program to find sum of elements in list

list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print("Sum of all elements in given list:Method1 ", total)

total = 0
ele = 0
 
list1 = [12, 15, 44, 88, 28]
 
while(ele < len(list1)):
    total = total + list1[ele]
    ele += 1

print("Sum of all elements in given list using While loop:Method2 ", total)

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Sum of all elements in given list:Method1  74
Sum of all elements in given list using While loop:Method2  187

#Program8
#Multiply all numbers in the list

def multiply(lst):
	result =1
	for i in lst:
		result =result * i
	return result

list1 = [1, 2, 3 , 5]
list2 = [3, 2, 4]
print(multiply(list1))
print(multiply(list2))

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
30
24


#Program9
#Python program to find smallest number in a list

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Smallest element is:Method1", *list1[:1])
list1 = [10, 90, 6, 45, 9]
print("Smallest element is:Method2", min(list1))

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Smallest element is:Method1 4
Smallest element is:Method2 6

#Program10
#Python program to find largest number in a list

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Smallest element is:Method1", list1[-1])
list1 = [10, 900, 6, 45, 9]
print("Smallest element is:Method2", max(list1))

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Smallest element is:Method1 99
Smallest element is:Method2 900


#Program11
#Python program to find second largest number in a list

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Smallest element is:Method1", list1[-2])
list1 = [10, 89, 6, 678, 999]
new_list = set(list1)
new_list.remove(max(new_list))

print("Smallest element is:Method2", max(new_list))

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Smallest element is:Method1 45
Smallest element is:Method2 678

#Program12
#Python program to find second largest number in a list

list1 = [1000,298,3579,100,200,-45,900]
n = 4
  
list1.sort()
print(list1)
print(list1[-n:])

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
[-45, 100, 200, 298, 900, 1000, 3579]
[298, 900, 1000, 3579]

#Program13
#Python program to print even numbers in a list



list1 = [10, 22, 4, 45, 66, 90]
for num in list1:
    if num % 2 == 0:
            print(num, end=" ")

list1 = [10, 21, 4, 45, 66, 93]
li_even=[]

for i in list1 :
    if i%2 == 0:
        li_even.append(i)
print("\neven number list is [method2]:" ,li_even)

list1 = [10, 24, 4, 45, 66, 93]
num = 0
print("Using while loop::")
while(num < len(list1)):
    if list1[num] % 2 == 0:
        print(list1[num], end=" ")
    num = num + 1

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
10 22 4 66 90 
even number list is [method2]: [10, 4, 66]
Using while loop::
10 24 4 66 

#Program14
#Python program to print odd numbers in a list

list1 = [10, 21, 4, 45, 66, 90]
for num in list1:
    if num % 2 == 1:
            print(num, end=" ")

list1 = [10, 11, 4, 45, 65, 93]
li_even=[]

for i in list1 :
    if i%2 == 1:
        li_even.append(i)
print("\nodd number list is [method2]:" ,li_even)

list1 = [10, 24, 4, 45, 66, 93]
num = 0
print("Using while loop::")
while(num < len(list1)):
    if list1[num] % 2 == 1:
        print(list1[num], end=" ")
    num = num + 1

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
21 45 
odd number list is [method2]: [11, 45, 65, 93]
Using while loop::
45 93 

#Program15
#Python program to print all even numbers in a range

start, end = 4, 19

print("All the even in the range given::4,19")
for num in range(start, end + 1):
    if num % 2 == 0:        
        print(num, end = " ")

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
All the even in the range given::4,19
4 6 8 10 12 14 16 18 


#Program16
#Python program to print all odd numbers in a range

start, end = 4, 19

print("All the even in the range given::4,19")
for num in range(start, end + 1):
    if num % 2 == 1:        
        print(num, end = " ")

output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
All the even in the range given::4,19
5 7 9 11 13 15 17 19 

#Program17
#Python program to print positive numbers in a list

list1 = [11, -21, 0, -45, 66, -93]
for num in list1:
    if num >= 0:
        print(num, end = " ")

list1 = [10, 24, -4, 45, -66, 93]
num = 0
print("\nUsing while loop::")
while(num < len(list1)):
    if list1[num] >= 0:
        print(list1[num], end=" ")
    num = num + 1

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
11 0 66 
Using while loop::
10 24 45 93 

#Program18
#Python program to print negative numbers in a list

list1 = [11, -21, 0, -45, 66, -93]
for num in list1:
    if num < 0:
        print(num, end = " ")

list1 = [10, 24, -4, 45, -66, 93]
num = 0
print("\nUsing while loop::")
while(num < len(list1)):
    if list1[num] < 0:
        print(list1[num], end=" ")
    num = num + 1


output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
-21 -45 -93 
Using while loop::
-4 -66 

#Program19
#Python program to print all positive numbers in a range

start, end = -4, 19

print("All the even in the range given::-4,19")
for num in range(start, end + 1):
    if num >= 0:        
        print(num, end = " ")

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
All the even in the range given::-4,19
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 


#Program20
#Python program to print all negative numbers in a range

start, end = -4, 19

print("All the even in the range given::-4,19")
for num in range(start, end + 1):
    if num < 0:        
        print(num, end = " ")

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
All the even in the range given::-4,19
-4 -3 -2 -1 

#Program21
#Remove multiple elements from a list in Python

list1=[2,4,6,3,9,5,-6]
list1.pop(4)
print(list1)
list1.remove(2)
print(list1)
del list1[1:4]
print(list1)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
[2, 4, 6, 3, 5, -6]
[4, 6, 3, 5, -6]
[4, -6]


#Program22
#Python – Remove empty List from List

test_list = [5, 6, [], 3, [], [], 9]
print("The original list is : ",str(test_list))
res = list(filter(None, test_list))
print ("List after empty list removal : ", str(res))

l2=[2,4,[],6,[],5,9,[],7,4,1,4,6]
print("The original list is : " + str(l2))
res = [ele for ele in l2 if ele != []]
print ("List after empty list removal : ",str(res))

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
The original list is :  [5, 6, [], 3, [], [], 9]
List after empty list removal :  [5, 6, 3, 9]
The original list is : [2, 4, [], 6, [], 5, 9, [], 7, 4, 1, 4, 6]
List after empty list removal :  [2, 4, 6, 5, 9, 7, 4, 1, 4, 6]

#Program23
#Python | Cloning or Copying a list

def Cloning(li1):
    li_copy = li1[:]
    return li_copy
   
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:method1", li1)
print("After Cloning:method1", li2)

def Cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy
   
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:method2", li1)
print("After Cloning:method2", li2)

def Cloning(li1):
    li_copy = list(li1)
    return li_copy
   
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:method3", li1)
print("After Cloning:method3", li2)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Original List:method1 [4, 8, 2, 10, 15, 18]
After Cloning:method1 [4, 8, 2, 10, 15, 18]
Original List:method2 [4, 8, 2, 10, 15, 18]
After Cloning:method2 [4, 8, 2, 10, 15, 18]
Original List:method3 [4, 8, 2, 10, 15, 18]
After Cloning:method3 [4, 8, 2, 10, 15, 18]


#Program24
#Python | Count occurrences of an element in a list


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))

def countX(lst, x):
    return lst.count(x)

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
8 has occurred 5 times
8 has occurred 5 times

#Program25
#Python | Remove empty tuples from a list

def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
[('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', '')]


#Program26
#Python | Program to print duplicates from a list of integers

list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9] 
new = []  
for a in list: 
    n = list.count(a) 
    if n > 1:        
         if new.count(a) == 0:  # condition to check
             new.append(a)
print(new)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
[1, 2, 5, 9]

#Program27
#python program to find Cumulative sum of a list

li=[3,2,5,8,6,1,4]
l1=[]
a=0

for i in range(0,len(li)):
    a=a+li[i]
    l1.append(a)
print(li)
print(l1)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
[3, 2, 5, 8, 6, 1, 4]
[3, 5, 10, 18, 24, 25, 29]

#Program28
#Python | Sum of number digits in List

test_list = [12, 67, 98, 34]
print("The original list is : " ,str(test_list))
res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
print ("List Integer Summation : " , str(res))

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
The original list is :  [12, 67, 98, 34]
List Integer Summation :  [3, 13, 17, 7]


#Program29
#Break a list into chunks of size N in Python

l = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
n = 4
x = [l[i:i + n] for i in range(0, len(l), n)] 
print(x)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
[[1, 2, 3, 4], [5, 6, 7, 8], [9]]

#Program30
#Python | Ways to find length of list,if element exists in list,clear a list in Python

list1=[3,5,8,4,0,2,5,7]

a=len(list1)
print("length of list:",a)
print(list1.index(0))
list1.clear()
print(list1)

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
length of list: 8
4
[]
