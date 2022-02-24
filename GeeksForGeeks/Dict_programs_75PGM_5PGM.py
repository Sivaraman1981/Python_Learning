#Dict
#Program1
#Python – Extract Unique values dictionary values

a={'gfg': [5, 6, 7, 8], 'best': [6, 12, 10, 8], 'is': [10, 11, 7, 5], 'for': [1, 2, 5]}
print(a.values())
print(a.items())

output:


========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
dict_values([[5, 6, 7, 8], [6, 12, 10, 8], [10, 11, 7, 5], [1, 2, 5]])
dict_items([('gfg', [5, 6, 7, 8]), ('best', [6, 12, 10, 8]), ('is', [10, 11, 7, 5]), ('for', [1, 2, 5])])


#Program2
#Python program to find the sum of all items in a dictionary

d={'a': 100, 'b':300, 'c':500}
a=d.values()
n=0
for i in d.values():
    n=n+i
print(n)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
900

#Program3
#Python | Merging two Dictionaries

d={'a': 400, 'b':900, 'c':800}
a={'d':25, 'e':50}
d.update(a)
print(d)

output:


========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
{'a': 400, 'b': 900, 'c': 800, 'd': 25, 'e': 50}


#4)Python | Ways to remove a key from dictionary

a={1: 'hello', 2: 'hi', 3: 'welcome', 4: 'to', 5: 'python'}
print(a.keys())
a.pop(4)
print(a)

output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
dict_keys([1, 2, 3, 4, 5])
{1: 'hello', 2: 'hi', 3: 'welcome', 5: 'python'}

#Program5
#Python – Convert key-values list to flat dictionary

a = {'week' : [1, 2, 3,4],
             'weekname' : ['sunday', 'monday', 'tuesday','wednesday']}
res = dict(zip(a['week'], a['weekname']))
print(res)


output: 


========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
{1: 'sunday', 2: 'monday', 3: 'tuesday', 4: 'wednesday'}



