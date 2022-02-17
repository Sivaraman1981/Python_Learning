#Task1
#Using Range function  print multiples of 5 from 0 to 75
#Using Range function  print multiples of 8 from 0 to 72

#Using Range function  print multiples of 5 from 75 to 0
#Using Range function  print multiples of 8 from 96 to 72

print("Task1 is started::")
for i in range(0,76):
        print(f"Using Range function  print multiples of 5 from 0 to 75 value is {i}::",i*5)
        
for i in range(0,73):
        print(f"Using Range function  print multiples of 8 from 0 to 72 value is {i}:::",i*8)

print("Task1 is ended::")

print("Task1 is started::")
for i in range(75,-1,-1):
        print(f"Using Range function  print multiples of 5 from 75 to 0 value is {i}::",i*5)
        
for i in range(96,71,-1):
        print(f"Using Range function  print multiples of 8 from 96 to 72 value is {i}:::",i*8)


print("Task1 is ended::")


#Task2
#Get a dynamic list from user
#clues Task2 and Task3
#1. get number of elements from user
#Loop through range
#append to list/dicti

print("\nTask2 is started::")
list1=[]
num=input("Enter the number of elements::")
for i in range(int(num)):
        ele = int(input("enter the input value:"))
        list1.append(ele)       
print(list1)
print("Task2 is ended::\n")

#Task3
#Get a dynamic dictionary from user
#clues Task2 and Task3
#1. get number of elements from user
#Loop through range
#append to list/dicti

print("\nTask3 is started::")
dict1={}
num=input("Enter the number of elements::")
for i in range(int(num)):
        keys=int(input("enter the key value:"))
        value=(input("enter the value:"))
        dict1[keys]=value
print(dict1)
print("Task3 is ended::\n")

#Task4
#Get two integers from user
#print multiples of 8 between them

#clues:
#Use range function in for loop
#Use if condition inside for loop
#add in to list

#input 10 100
#multiples of 8
#[16,24,32.....,96]

print("\nTask4 is started::")
input1=int(input("enter the first range value::"))
input2=int(input("enter the second range value::"))
list1=[]
for i in range(input1,input2):
	if i%8==0:
		print(f'{i}:mulptiples of 8')
for i in range(input1,input2):
        if i%8==0:
                list1.append(i)
print(list1)

print("\nTask4 is ended::")

#Task5
#Li1 = [3,4,5,2,7,8,9,10]

#Output:
#Li_odd = [3,5,7,9]
#Li_even = [4,2,8,10]

print("\nTask5 is started::")
Li1 = [3,4,5,2,7,8,9,10]
Li2 = []
Li3 = []

for i in Li1:
    if i% 2 == 0:
        Li2.append(i)
    else:
        Li3.append(i)
        
print("Even number is::",list(Li2))
print("Odd number is::",list(Li3))
print("\nTask5 is ended::")


#Task6
#Input: [-1, -7,8,10,20,21,17,28,-3,0,0,]    
#Output:
#neg_LI = [-1,-7,-3]
#pos_LI = []
#Zeros = []

#Numeber of postivie ele: 6
#Number nega: 3
#Number of zeros: 2

print("\nTask6 is started::")
list1=[-1, -7,8,10,20,21,17,28,-3,0,0,]
list2=[]
list3=[]
list4=[]
for i in list1:
        if i>0:
                list2.append(i)
        elif i<0:
                list3.append(i)
        elif i==0:
                list4.append(i)
print("The number of positive value is::",len(list2)," and the values are::",list2)
print("The number of positive value is::",len(list3)," and the values are::",list3)
print("The number of positive value is::",len(list4)," and the values are::",list4)
print("\nTask6 is ended::")

#Task7

print(list(range(5)))
print(list(range(1,5)))
print(list(range(5,20)))
print(list(range(-5,5)))
print(list(range(10,100,10)))
print(list(range(10,0,-1)))
print(list(range(-5,5,3)))
print(list(range(10,100,5)))
print(list(range(10,0,-2)))