#Task1
#Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]

#Output of these values 5 56 222 50000 put 5555 7777 666 89 on 333 3333
print("Task1 started:::\n")
Li1 = [2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]
print(Li1)
print(Li1[3])
print(Li1[4][1])
print(Li1[4][4][1])
print(Li1[4][4][3][2][1])
print(Li1[4][4][3][2][3][3:6])
print(Li1[4][4][3][0])
print(Li1[4][4][3][4])
print(Li1[4][4][6])
print(Li1[4][5])
print(Li1[4][4][3][2][2][-2:])
print(Li1[4][4][2])
print(Li1[4][4][3][1])

print("\nTask1 ended:::\n")

#Task2
#Extract the below from a = [1,2,3,4,[100,101,102,"Computer_science"],200,203]
#science
#Computer
print("Task2 started:::\n")
Li1 = [1,2,3,4,[100,101,102,"Computer_science"],200,203]
print(Li1)
print(Li1[4])
a=(Li1[4][3])
print(a[a.find("_")+1:])
print(a[0:a.find("_")])
print("\nTask2 ended:::\n")
#Task3
#Extract the below from a = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]
#666
#201
#102
#999
#777
print("Task3 started:::\n")
Li1 = [1,2,3,4,[101,102,103,[201,202,[999]], 666, 777]]
print(Li1)
print(Li1[4])
print(Li1[4][4])
print(Li1[4][3][0])
print(Li1[4][1])
print(Li1[4][3][2])
print(Li1[4][5])
print("\nTask3 ended:::\n")
#Task4
#Extract the blow from Li1 = [2,3,"python","hello",4,5,0]  
#ll
#thon
print("Task4 started:::\n")
Li1 = [2,3,"python","hello",4,5,0]  
print(Li1)
print(Li1[3][2:4])
print(Li1[2][2:])
print("\nTask4 ended:::\n")
#Task5
Li1 = [1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]

#Output Prediction 
print("Task5 started:::\n")
print(Li1[5][0])
print(Li1[5][6])
print(Li1[5][-2])
print(Li1[5][7])
print(Li1[6])
print(Li1[5][5][1])
print(Li1[-2][-1])
print(Li1[-2][2:4])
print("\nTask5 ended:::\n")
#Task6
#a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}
#output with below values alone from above set
#py
#ello
#en
#zoo
#Bot
print("Task6 started:::\n")
a = {1: [1,2,3,"python"], 2:{10:"hello",20:"welcome",40: "science"}, 99: {3,4,5,6}, 40:{1:"zoology", 2:"Botany"}}
print(a)
print(a[1][3][0:2])
print(a[2][10][1:])
print(a[2][40][3:5])
print(a[40][1][0:3])
print(a[40][2][0:3])
print("\nTask6 ended:::\n")
#Task7
#Covert below two lists in to a dictionary [1,2,3,4,5] ["python","cpp","c","java","php"]
print("Task7 started:::\n")
key_list = [1,2,3,4,5]
value_list = ["python","cpp","c","java","php"]

#Method1
print("Method1::\n",dict(zip(key_list,value_list)))


#Method2:
dict_from_list = {key_list[i]: value_list[i] for i in range(len(key_list))}
print("Method2::\n",dict_from_list)
print("\nTask7 ended:::\n")
#Task8
#Covert below set in to a list {5,4,3,6,2,7,1}
print("Task8 started:::\n")
sample_set = {5,4,3,6,2,7,1}
my_list = list(sample_set)
print(my_list)
print("\nTask8 ended:::\n")
#Task9
#Remove duplicates from below list  [5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
print("Task9 started:::\n")
list1 = [5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
print(list(set(list1)))
print("\nTask9 ended:::\n")
#Task 10
#Convert below one to tuple
#[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
print("Task10 started:::\n")
list1 = [5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
print(tuple(list1))
print("\nTask10 ended:::\n")


