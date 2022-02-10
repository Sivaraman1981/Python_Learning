
#Create an empty list (two ways)
# Creating empty List using []
sample_list = []
print('Sample List: ', sample_list)
# Creating empty List using list constructor
sample_list = list()
print('Sample List: ', sample_list)
#Concatenate with [5,6,7,8]
sample_list2=[5,6,7,8]
print("List with elements:",sample_list2)
sample_list.extend(sample_list2)
print("After concatination empty list is:",sample_list)
#add 8,9,1,5,6,7,8,1 elements to that list
sample_list3= (8,9,1,5,6,7,8,1)
print("Before concatination sample_list3 is:",sample_list3)
sample_list.extend(sample_list3)
print(sample_list)
#Find frequency of 8 (count)
frequency=sample_list.count(8)
print("Frequency of the given value is",frequency)
#find the mean of the list
mean=sum(sample_list)/len(sample_list)
print("Mean of the list is:",mean)
#find sum (List) + min + Max 
print("sum of list is:",sum(sample_list))
print("Minimum element in the list is:",min(sample_list))
print("Maximum element in the list is:",max(sample_list))
#Find median of the list
median=sample_list[(len(sample_list)-1)//2:(len(sample_list)+2)//2]
print("Median of list is:",median)
sample_list1 = set(sample_list)
print("After removing duplicate values:",sample_list1)
print("Printing output in Tuple format",tuple(sample_list1))

#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Find the common elements between two tuples
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times

tup1 = (1,4,5,6,7,8)
tup2 = (5,6,7,8,9)

print(tup1)
print(tup2)
tuble3=(tup1 + tup2)
result = tuple(set(tup1) & set(tup2))
print("Find the common elements between two tuples::",result)
print("Concatenate both tuples :::",(tuble3))
print("Concatenate both tuples and remove duplicates from tuple:::",set(tuble3))
print("Find the index value of 9 (after concatenation):::",tuble3[9])
Output = [(x * 3) for x in tuble3]
print("Multiply by 3 times:::",Output)

#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2

set1=set()
set2=set()
print(set1)
print(type(set1))
print(type(set2))
print(set2)
set3={7,8,9,1,2,3,4,5,0}
set1.update(set3)
set2.update({4,5,6,0})
print(set1)
print(set2)
print("Is set1 is subset of set2:",set1.issubset(set2))
print("Common elements in two sets are",set1.intersection(set2))
set1.discard(8)
set2.discard(8)
set2.discard(0)
set1.discard(0)
print(set1.union(set2))


