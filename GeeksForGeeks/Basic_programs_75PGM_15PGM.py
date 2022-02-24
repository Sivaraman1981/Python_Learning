
#Program 1
# Add two numbers
number1 = input("First number: ")
number2 = input("\nSecond number: ")
sum = float(number1) + float(number2)
  
print("The sum of {0} and {1} is {2}" .format(number1, number2, sum))

output:
First number: 12

Second number: 22
The sum of 12 and 22 is 34.0

#Program 2
#Program to find max of 2 numbers
int1 = int(input("Enter number 1: "))
int2 = int(input("Enter number 2: "))

print("Max number is:", max(int1,int2))

Output:
Enter number 1: 22
Enter number 2: 44
Max number is: 44

#Program 3 
# Program for factorial of a number

number1 = int(input("Enter the number::"))
factorial = 1

if number1 < 0 and (number1 == 0 or number1==1):
   print("The factorial of 0&1 is 1")
else:
   for i in range(1,number1 + 1):
       factorial = factorial*i
   print("The factorial of",number1,"is",factorial)
 
output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter the number::3
The factorial of 3 is 6

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter the number::7
The factorial of 7 is 5040

#Program 4
#Simple Interest Program
def simple_interest(principle,time,rate):
    si = (principle*time*rate)/100
    print('The Simple Interest is', si)
    return si

principle = float(input("Enter the priciple amount: "))
time = float(input("Enter the units of time: "))
rate = float(input("Enter the rate of interest: "))

simple_interest(principle,time,rate)

output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter the priciple amount: 4000
Enter the units of time: 2
Enter the rate of interest: 3
The Simple Interest is 240.0

#Program 5
#Compound Interest

def compound_interest(principle, rate, time):
 
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)
 
principle = float(input("Enter the priciple amount: "))
time = float(input("Enter the units of time: "))
rate = float(input("Enter the rate of interest: "))

compound_interest(principle, time, rate)

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter the priciple amount: 10000
Enter the units of time: 10.25
Enter the rate of interest: 5
Compound interest is 6289



#Program 6
#whether the number is armstrong or not

def armstrong(num1):
    tlength = len(num1)
    sumval = 0
    for i in num1:
        sumval = sumval + int(i)**tlength
    
    if(str(sumval) == num1):
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")
    
num1 = input("Enter a number to check if the number is armstrong or not: ")
armstrong(num1)

#Program 7
#Program to find area of a circle

def area_circle(radius):
    pi = 3.14
    return pi*radius**2

radius = float(input("Enter the radius of circle: "))

print(area_circle(radius))

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter the radius of circle: 22
1519.76

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter the radius of circle: 2
12.56

#Program 8
#print all Prime numbers in an Interval

lower = int(input("Enter a lower: "))
upper = int(input("Enter a upper: "))
prime_list = []
for num in range(lower, upper):
    if num>1:    
        for i in range(2,num):
              if(num % i == 0):
                  break
        else:
            prime_list.append(num)
            
print(prime_list)  

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter a lower: 2
Enter a upper: 7
[2, 3, 5]

#Program 9
#program to check whether a number is Prime or not

def prime_number(num1):
    if(num1 == 0 or num1 ==1):
        print(num1,"Is not a prime number")
    else:
        for n in range(2,num1):
            if num1%n==0:
                print(num1,"Is not a Prime Number")
                break
        else:
            print(num1,"Is Prime number")
        
number1 = int(input("Enter a number to check if its a prime number or not:"))
prime_number(number1)

#Program 10
#Program for n-th Fibonacci number

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
number1=int(input("Enter the number::")
print(fibonacci(number1))

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter the number::7
8

#Program 11
#Program for How to check if a given number is Fibonacci number?

import math

def tocheckperfectsquare(n):
    sqrt = int(math.sqrt(n))
    if pow(sqrt, 2) == n:
        return True
    else:
        return False

def toverifyfibonaccinumber(n):
    res1 = 5 * n * n + 4
    res2 = 5 * n * n - 4
    if tocheckperfectsquare(res1) or tocheckperfectsquare(res2):
        return True
    else:
        return False

number1 = int(input("Enter an integer number: "))

if toverifyfibonaccinumber(number1):
    print ("Yes,", number1, "is a Fibonacci number")
else:
    print ("No,", number1, "is not a Fibonacci number")

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter an integer number: 7
No, 7 is not a Fibonacci number

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter an integer number: 8
Yes, 8 is a Fibonacci number

#Program 12
#Program for n\’th multiple of a number in Fibonacci Series

def findPosition(k, n):
    f1 = 0
    f2 = 1
    i =2;
    while i!=0:
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
        #print("f3::",f3)
        #print("f1::",f1)
        #print("f2::",f2,"\n")
        if f2%k == 0:
            #print("inside if::",f2,k,n,i)
            return n*i
 
        i = i + 1
    #print("before main return::")     
    return
 
 
# Multiple no.
n = 5;
# Number of whose multiple we are finding
k = 4;
 
print(f"Position of {n}\'th multiple of {k} in" "Fibonacci Series is", findPosition(k,n));

output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Position of 5'th multiple of 4 inFibonacci Series is 30


#Program 13
#Program to find ASCII value of a char
char1 = input("Enter a character to find the ASCII value: ")
print(ord(char1))

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter a character to find the ASCII value: r
114



#Program 14
#Sum of square of n numbers

def square_sum(num):
    sum1 = 0
    for n in range(1,num+1):
        #print(n)
        #print("sum1,n**2",sum1,n**2)
        sum1 = sum1 + (n**2)
        #print("after add sum1 + (n**2):",sum1)
    return sum1

num = int(input("Enter a number to find the sum of squares of n numbers: "))
print(square_sum(num))

Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter a number to find the sum of squares of n numbers: 4
30


#Program 15
#Sum of cube of n numbers

def cube_sum(num):
    sum1 = 0
    for n in range(1,num+1):
        #print(n)
        #print(sum1,n**3)
        sum1 = sum1 + (n**3)
        #print("after add sum1 + (n**3):::",sum1)
    return sum1

num = int(input("Enter a number to find the sum of squares of n numbers: "))
print(cube_sum(num))


Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter a number to find the sum of squares of n numbers: 5
225

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter a number to find the sum of squares of n numbers: 4
100


