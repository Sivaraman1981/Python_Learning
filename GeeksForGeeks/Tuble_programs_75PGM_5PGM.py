#tubles
#Program1
#Python program to Find the size of a Tuple

tup=(22,54,3,18,64,19,21)
print("To find out size of the tuple is:",len(tup))

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
To find out size of the tuple is: 7



#Program2
#Python – Maximum and Minimum K elements in Tuple

tup=(22,54,3,18,64,19,21)
print("minimum element of tuple :",min(tup))
print("maximum element of tuple :",max(tup))

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
minimum element of tuple : 3
maximum element of tuple : 64

#Program3
#Python – Adding Tuple to List and vice – versa

tup1=(25,40,17)
li=[16,33]
li+=tup1
print(li)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
[16, 33, 25, 40, 17]

#Program4
#Python – Convert Nested Tuple to Custom Key Dictionary

Li1 = (3,4,5,6,9)
Li2 = ("python","c","java","sql","aws")

print(dict(zip(Li1,Li2)))

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
{3: 'python', 4: 'c', 5: 'java', 6: 'sql', 9: 'aws'}


#Program5
#Python – Flatten tuple of List to tuple

Li1 = (3,4,5,6,9,10)
Li2 = ("Hello","All","welcome","to","aws","Python")

print(list(zip(Li1,Li2)))


output:


========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
[(3, 'Hello'), (4, 'All'), (5, 'welcome'), (6, 'to'), (9, 'aws'), (10, 'Python')]
