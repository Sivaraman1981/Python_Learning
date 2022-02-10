#Task6
a = input("please enter a First string: ")
print(a[0])
print(a[-1])
print(len(a[1:-1]))
b=str(len(a[1:-1]))
print("The Final Output is:",a[0]+b+a[-1])
a = input("please enter a Second string: ")
print(a[0])
print(a[-1])
print(len(a[1:-1]))
b=str(len(a[1:-1]))
print("The Final Output is:",a[0]+b+a[-1])

"""#Task5
a = input("please enter a First string: ") #string default
b = input("please enter a Second string: ")
print(a)
print(b)
a1=a.find('p')
b1=b.find('c')
print(a1)
print(b1)
print("Find out the value of string1:",a[a1])
print("Find out the value of string2:",b[b1])

print("The ASCII value of '" + a[a1] + "' is", ord(a[a1]))
print("The ASCII value of '" + b[b1] + "' is", ord(b[b1]))
a2=ord(a[a1])
b2=ord(b[b1])

print(f"Based on the above ASCII value({ord(a[a1])}) of The original value is", chr(ord(a[a1])))
print(f"Based on the above ASCII value({ord(b[b1])}) of The original value is", chr(ord(b[b1])))
print("The Total value is:",int(a2+b2))

#Task4
a = input("please enter a First string: ") #string default
b = input("please enter a Second string: ")
#c = input("please enter a Third string: ")
#d = input("please enter a Fourth string: ")
print(a)
print(b)
a1=a[0]
b1=b[0]
a2=a[1:]
b2=b[1:]
print(a1)
print(b1)
print(a2)
print(b2)
a1_len=len(a)
b1_len=len(b)
print(a1_len)
print(b1_len)
a3=a1_len//2
b3=b1_len//2
print(a3)
print(b3)
a4=(a[a3])
b4=(b[b3])
print(a4)
print(b4)
a1_b1_len=str(str(a1_len)+str(b1_len))
print("The Final Output is:",str(b1+a2+a1+b2+a1_b1_len+a4+b4))
a = input("please enter a Third string: ")
b = input("please enter a Fourth string: ")
print(a)
print(b)
a1=a[0]
b1=b[0]
a2=a[1:]
b2=b[1:]
print(a1)
print(b1)
print(a2)
print(b2)
a1_len=len(a)
b1_len=len(b)
print(a1_len)
print(b1_len)
a3=a1_len//2
b3=b1_len//2
print(a3)
print(b3)
a4=(a[a3])
b4=(b[b3])
print(a4)
print(b4)
a1_b1_len=str(str(a1_len)+str(b1_len))
print("The Final Output is:",str(b1+a2+a1+b2+a1_b1_len+a4+b4))
#Task3
a = input("please enter a First string: ") #string default
b = input("please enter a Second string: ")
c = input("please enter a Third string: ")
print(a)
a1=a.split(' ')
print(a1)
a2=float(a1[1])
#a1=int(a.split(' ')[1])
print(a2)
print(b)
b1=b.split(' ')
print(b1)
b2=float(b1[1])
print(b2)
print(c)
c1=c.split(' ')
print(c1)
c2=float(c1[1])
print(c2)
tot_value=(a2+b2+c2)
print("The total value of above input value is:",tot_value)
##Task2
c = input("please enter a string of strip: ") 
print(c)
c1 = input("please enter a string of lstrip: ") 
print(c1)
c2 = input("please enter a string of rstrip: ") 
print(c2)
print("Using strip:",c.strip("*"))  
c3=(c1.lstrip("*"))
c4=(c3.rstrip("*"))
print("Using lstrip:",c4)
c5=(c2.rstrip("*"))
c6=(c5.lstrip("*"))
print("Using rstrip:",c6)
##Task1
c = input("please enter a string: ") #string default
print(c)
length=len(c)
print("Length of string is:",length)
length1=int(len(c)/2)
print("The middle string value is:",length1)
print(c[length1])




========================================== RESTART: C:/Users/sivar/AppData/Local/Programs/Python/Python310/3.py =========================================
please enter a string of strip: ***python***
***python***
please enter a string of lstrip: **python********
**python********
please enter a string of rstrip: ********python*******
********python*******
Using strip: python
Using lstrip: python
Using rstrip: python"""
