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
#Python program Different ways to clear a list in Python


lst = [10, 11, 12, 13, 14, 15]

