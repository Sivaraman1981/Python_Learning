
#Program 1
# Add two numbers
number1 = input("First number: ")
number2 = input("\nSecond number: ")
sum = float(number1) + float(number2)
  
print("The sum of {0} and {1} is {2}" .format(number1, number2, sum))

#Program 2
#Program to find max of 2 numbers
int1 = int(input("Enter number 1: "))
int2 = int(input("Enter number 2: "))

print("Max number is:", max(int1,int2))

Output:
Enter number 1: 4
Enter number 2: 100
Max number is: 100

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
 
#Program 4
#Simple Interest Program
def simple_interest(principle,time,rate):
    return (principle*time*rate)/100

principle = float(input("Enter the priciple amount: "))
time = float(input("Enter the units of time: "))
rate = float(input("Enter the rate of interest: "))

print(simple_interest(principle,time,rate))

#Program 5
#Compound Interest
def compound_interest(principle,time,rate):
    return principle*(1 + rate/100)**time

principle = float(input("Enter the priciple amount: "))
time = float(input("Enter the units of time: "))
rate = float(input("Enter the rate of interest: "))

print(compound_interest(principle,time,rate))

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
def area_circle(radius):
    pi = 3.14
    return pi*radius**2

radius = float(input("Enter the radius of circle: "))

print(area_circle(radius))


#Program 8
#Sum of square of n numbers
def square_sum(num):
    sum1 = 0
    for n in range(num+1):
        sum1 = sum1 + (n**2)
    return sum1

num = int(input("Enter a number to find the sum of squares of n numbers: "))
print(square_sum(num))


#Program 9
#Sum of cube of n numbers
def cube_sum(num):
    sum1 = 0
    for n in range(num+1):
        sum1 = sum1 + (n**3)
    return sum1

num = int(input("Enter a number to find the sum of squares of n numbers: "))
print(cube_sum(num))


#Program 10
#Program to find ASCII value of a char
char1 = input("Enter a character to find the ASCII value: ")[0]
print(ord(char1))

Output:
Enter a character to find the ASCII value: u
117

