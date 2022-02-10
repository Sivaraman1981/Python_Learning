print("This is for example of indexing and slicing in python")
a = "python" #indexing
print(a)
print(a[0]) #p
print(a[3]) #h
print(a[-1]) #n
print(a[-4]) #t

s="Python"
print (s[1:3])
#Output:yt
s="Python"
print (s[0:3])
#Output:Pyt
s="Python"
print (s[:4])
#Output:Pyth
s="Python"
print (s[2:])
#Output:thon
s="Python"
print (s[-2:])
#Output:on
s="Python"
print (s[1:5:2])
#Output:yh

n=[0,1,2,3,4,5]
print(n[:])
#Output:[0, 1, 2, 3, 4, 5]
n=[0,1,2,3,4,5]
print(n[1:3])
#Output:[1, 2]
n=[0,1,2,3,4,5]
print(n[1:])
#Output:[1, 2, 3, 4, 5]
n=[0,1,2,3,4,5]
print(n[:4])
#Output:[0, 1, 2, 3]
n=[0,1,2,3,4,5]
print(n[1:2])
#Output:[1]
print (n[1])
#Output:1
n=[0,1,2,3,4,5]
print(n[1:5:2])
#Output:[1,3]