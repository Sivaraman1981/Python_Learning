#Task1
#whether the string is palindrome or not

def palindrome_string(str1):
   reversestr=str1[::-1]
   if str1 == reversestr:
       return "Enter string is palindrome"
   else:
       return "Enter string is not palindrome"

string1= input("enter the string to find out palindrome or not::")
print(palindrome_string(string1))

#Task2
#whether the number is armstrong or not
def armstrong(num1):
    leng = len(num1)
    sumval = 0
    for i in num1:
        sumval = sumval + int(i)**leng
    
    if(str(sumval) == num1):
        print("It is an armstrong number")
    else:
        print("It is not an armstrong number")
    
num1 = input("Enter a number to check if the number is armstrong or not: ")
armstrong(num1)

#Task 3
#whether the number is prime or not

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

#Task4. Find factorial of a number using function

def factorial(num1):
 
    # single line to find factorial
    return 1 if (num1==1 or num1==0) else num1 * factorial(num1 - 1)
 
number1=int(input("Enter the number::"))
print ("Factorial of",number1,"is",factorial(number1))


#Task5. Find factorial of a number using recursive function
def factorial(num1):
    if(num1>1):
        fact2=num1*factorial(num1-1)
        return fact2
    else:
        return 1    

number1=int(input("Enter a number::"))
fact1=factorial(number1)
print("Factorial of a number is=",fact1)

#Task6. Find factorial of a number without using function
number1 = int(input("Enter the number::"))
factorial = 1

if number1 < 0 and (number1 == 0 or number1==1):
   print("The factorial of 0&1 is 1")
else:
   for i in range(1,number1 + 1):
       factorial = factorial*i
   print("The factorial of",number1,"is",factorial)

#Task7. Fibonacci series

