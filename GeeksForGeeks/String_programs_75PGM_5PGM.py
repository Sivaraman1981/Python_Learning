#String
#Program1
#Python program to check if a string is palindrome or not

def string(a):
    if a[::]==a[::-1]:
        print(a," :is polindrome")
    else:
        print(a,":is not polindrome")
    return a
print(string("malayalam"))
print(string("python"))

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
malayalam  :is polindrome
malayalam
python :is not polindrome
python


#Program2
#Reverse words in a given String in Python

string="welcome to Java J2EE class"
l=string.split(" ")
print(l[::-1])

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
['class', 'J2EE', 'Java', 'to', 'welcome']


#Program3
#Python program to print even length words in a string

string="welcome to python class"
list1=string.split(" ")
for words in list1:
    if len(words)%2==0:
        print(words)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
to
python


#Program4
#Ways to remove i’th character from string in Python

str1="mathematics"
a=len(str1)
str2=""
for i in range(a):
    if i!=3:
        str2=str2+str1[i]
print(str1)
print(str2)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
mathematics
matematics


#Program5
#Find length of a string in python (2 ways)

def l_str(a):
    c=0
    for i in a:
        c=c+1
    return c
a="hello world"
print("Method1::",l_str(a))

s="maths"
n=len(s)
print("Method2::",n)



========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Method1:: 11
Method2:: 5