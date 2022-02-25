
print("Welcome to Data structure calculator!!!")

user_select =int(input("Please select any one Data structure::: 1.List 2.Tuple 3.Set 4.Dictionary::: "))

if user_select == 1:
    print("You have selected the List data structure and welcome to the List!!")
    list1 = []

    noofelements = int(input("Enter number of elements : "))
    
    for i in range(0, noofelements):
        ele = int(input())
        list1.append(ele) 
     
    print(list1)
    
    print("1.Append","\n2.Pop","\n3.Update","\n4.Concatenation","\n5.Sum","\n6.Min","\n7.Max","\n8.Length","\n9.Mean","\n10.Median","\n11.Find","\n12.Frequency","\n13.Insertion","\n14.Remove","\n15.Count")

    list_operation=int(input("Please select any of the above operations to peform further List process::" ))

    if list_operation == 1:
        print("You have selected the Append operation in List::")
        append_elements = int(input("Enter the elements to add in List: "))
        list1.append(append_elements)
        print("After append operation, current List::",list1)
        
    elif list_operation == 2:
        print("You have selected the Pop operation in List::")
        pop_elements = int(input("Enter the elements to Pop in List: "))
        list1.pop(pop_elements)
        print("After Pop operation, current List::",list1)
        
    elif list_operation == 3:
        print("You have selected the Update operation in List::")
        update_position = int(input("Enter the position to update in List: "))
        update_elements = int(input("Enter the elements to update in List: "))
        
        list1[update_position]=update_elements
        print("After Update operation, current List::",list1)
        
    elif list_operation == 4:
        print("You have selected the Concatenation operation in List::")
        Concat_elements = int(input("Enter the No of elements to Concatenation in List: "))
        for i in range(0,Concat_elements):
            ele = int(input())
            list1.append(ele)       
        print("After Concatenation operation, current List::",list1)  

elif user_select == 2:
    print("You have selected the Tuple data structure and welcome to the Tuble!!")


elif user_select == 3:
    print("You have selected the Set data structure and welcome to the Set!!")


elif user_select == 4:
    print("You have selected the Dictionary data structure and welcome to the Dictionary!!")

else:
    print("You have selected Invalid Operation!!")

print("End of Data structure calculator!!!")
