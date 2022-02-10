

dict1={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
print(dict1)
a=dict1[3]
print("a value is:",a)
b=a[0]
print("a value is:",b)
print("Extract 'bobtn' from above dictionary\n",b[0::2])
a1=a[2]
print("a1 value is:",a1)
print("Extract 'arbeg' from above dictionary\n",a1[-1:1:-1])
print("print all keys in dictionary and convert it into tuple::",tuple(dict1.keys()))
dict2_values=(dict1[2])
print(dict2_values)
dict2_values=sum(dict1[2])
print(dict2_values)
length=len(dict1[2])
print(length)
avg_val=dict2_values/length
print("Find the average of all numbers available under key 2::",int(avg_val))
