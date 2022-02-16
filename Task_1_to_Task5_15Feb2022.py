#Task1
#hackerrank Write a function
print("The Task 1 Started:")
def is_leap(year):
    leap = False
    
    if year%4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
    else:
        leap = False
    
        return leap

year = int(input("Enter the Year:"))
print(is_leap(year)) 

print("The Task 1 Ended:")

#Task 2
#hackerrank Python If-Else
print("The Task 2 Started:")

n = int(input("Enter the Value:"))

if(n%2 != 0):
        print("Weird")
else:
    if(n in range(2,6)):
        print("Not Weird")
    elif(n in range(6,21)):
        print("Weird")
    elif(n>20):
        print("Not Weird")       

print("The Task 2 ended:")
#Task 3
#Fizz buzz
#Get one number from user
#Multiple of 3 ==> Fizz
#Multiple of 5 ===> buzz
#Multiple of 3 and 5 ===> Fizzbuzz
#None ==> Invalid number

print("The Task 3 Started:")

a= int(input("Enter the Value:"))

if a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0 and a % 5 == 0:
    print("Fizzbuzz")
else:
   print("Invalid number")

print("The Task 3 ended:")

#Task 4
#Get one mark from student
#mark 0 to 100 Valid otherwise invalid mark

#50 + PASS otherwise FAIL
#90 to 100 ===> A 
#80 to 89 ===> B
#70 to 79 ===> C
#60 to 69 ===> D
#50 to 59 ===> E
#0 to 49 ===> FAIL

#if it is 93 ===> A
#if it is 99 ===> A
#if it is 88 ====> B

# if it is 78
#VALID MARK (between 0 to 100)
#PASS MARK (50 +)
#C
#if it is 65

print("The Task 4 Started:")

mark1= int(input("Enter the marks:"))

if(mark1>0 and mark1<100):
    print("Valid marks")
    if(mark1>=50):
        print("PASS")
        if(mark1>90 and mark1<100):
            print("Grade A")
        elif(mark1>80 and mark1<89):
            print("Grade B")
        elif(mark1>70 and mark1<79):
            print("Grade C")
        elif(mark1>60 and mark1<69):
            print("Grade D")
        elif(mark1>=50 and mark1<59):
                print("Grade E")
    else:
        print("FAIL")
    
else:
    print("Invalid marks")

print("The Task 4 ended:")

#Task 5
#collect three marks from user
#calculate mark1 + mark2 + mark3 / 100

#if calculate > 90 ===> Grade A
#if calculate > 75 ==> Grade B
#calculate > 50  ==> grade C
#Other wise ===> Grade D

print("The Task 5 Started:")
a= int(input("Enter the Tamil mark:"))
b= int(input("Enter the English mark:"))
c= int(input("Enter the Maths mark:"))
d=(a+b+c)/3
print(d)
if d>90:
    print("Grade A")
elif d>75:
    print("Grade B")
elif d>50:
    print("Grade C")
else:
    print("Grade D")

print("The Task 5 ended:")

