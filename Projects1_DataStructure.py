
###List operation functions

def create_list():
    list1 = []
    noofelements = int(input("Enter number of elements : "))
    
    for i in range(0, noofelements):
        ele = int(input(f"Enter the {i} Elements to add into list::"))
        list1.append(ele) 
     
    print("Created list::",list1)
    return list1

def list_append(list2):
    append_elements = int(input("Enter the elements to add in List: "))
    list2.append(append_elements)
    return list2

def list_pop(list2):
    pop_elements = int(input("Enter the elements to Pop in List: "))
    list2.pop(pop_elements)
    return list2

def list_update(list2):
    update_position = int(input("Enter the position to update in List: "))
    update_elements = int(input("Enter the elements to update in List: "))            
    list2[update_position]=update_elements
    return(list2)

def list_concat(list2):
    Concat_elements = int(input("Enter the No of elements to Concatenation in List: "))
    for i in range(0,Concat_elements):
        ele = int(input(f"Enter the {i} Elements to concat into list::"))
        list2.append(ele)
    return list2

###Set operation functions

def set_create():
    set1=set()
    no_of_ele=int(input("Enter number of elements to create Set:"))
    for i in range(0,no_of_ele):
        ele=int(input(f"Enter the {i} Elements to create into set ::"))
        set1.add(ele)
    print("Created set is::",set1)
    return set1

def set_add():
    add_elements=int(input("Enter the elements to add into set::"))
    set1.add(add_elements)
    return set1

def set_pop():
    pop_elements=int(input("Enter elements to Pop from set::"))
    set1.pop()
    return set1

def set_sum():
    sumset=sum(set1) 
    return sumset

def set_max():
    maxset=max(set1)    
    return maxset

def set_min():
    minset=min(set1)    
    return minset

def set_intersection():
    intset=set1.intersection(set2)    
    return intset

def set_union():
    uniset=set1.union(set2)    
    return uniset

###Dictionary Fucntions

def dict_create():
    dict1={}
    noofelements=input("Enter the number of elements to add into Dict::")
    for i in range(int(noofelements)):
        keys=int(input("Enter the key value of Dict::"))
        value=(input("Enter the value of Dict in Keys::"))
        dict1[keys]=value        
    print("After Create dictionary is::",dict1)
    return dict1

def dict_add():
    keysadd=int(input("Enter the key value of Dict::"))
    addvalue=(input("Enter the value of Dict in Keys::"))
    dict1[keysadd]=addvalue    
    return dict1

def dict_pop():
    keyspop=int(input("Enter the key value of poping:"))
    dict1.pop(keyspop)
    return dict1

def dict_update():
    keys=int(input("Enter the key value to be updated in Dict::"))
    value=(input("Enter the updated value of Dict in Keys::"))
    dict1[keys]=value
    dict1.update(create2_dict)    
    return dict1

def dict_max():
    dict1max=max(dict1)    
    return dict1max

def dict_min():
    dict1min=min(dict1)    
    return dict1min


print("Welcome to Data structure calculator!!!")

while True:
    
    user_select =int(input("Please select any one Data structure::: 1.List 2.Tuple 3.Set 4.Dictionary 5.Exit::: "))

    if user_select == 1:
        print("You have selected the List data structure and welcome to the List!!")

        list1=create_list()
    
        while True:
            print("1.Append","\n2.Pop","\n3.Update","\n4.Concatenation","\n5.Sum","\n6.Min","\n7.Max","\n8.Length",
              "\n9.Mean","\n10.Median","\n11.Find/Index","\n12.Count/Frequency","\n13.Remove","\n14.Copy","\n15.Reverse","\n16.Exit")

            list_operation=int(input("Please select any of the above operations to peform further List process::" ))

            if list_operation == 1:
                print("You have selected the Append operation in List::")
                list1=list_append(list1)
                print("After append operation, current List::",list1)
            
            elif list_operation == 2:
                print("You have selected the Pop operation in List::")
                list1=list_pop(list1)
                print("After Pop operation, current List::",list1)
            
            elif list_operation == 3:
                print("You have selected the Update operation in List::")
                list1=list_update(list1)
                print("After Update operation, current List::",list1)
            
            elif list_operation == 4:
                print("You have selected the Concatenation operation in List::")
                list1=list_concat(list1)
                print("After Concatenation operation, current List::",list1)
            
            elif list_operation == 5:
                print("You have selected the Sum operation in List::",list1)
                sumoflist=sum(list1)
                print("After Sum of operation::",sumoflist)
            
            elif list_operation == 6:
                print("You have selected the Min operation in List::",list1)
                minoflist=min(list1)
                print("After Min of operation::",minoflist)

            elif list_operation == 7:
                print("You have selected the Max operation in List::",list1)
                maxoflist=max(list1)
                print("After Max of operation::",maxoflist)

            elif list_operation == 8:
                print("You have selected the Length operation in List::",list1)
                lenoflist=len(list1)
                print("After Length of operation::",lenoflist)
            
            elif list_operation == 9:
                print("You have selected the Mean operation in List::",list1)
                moflist=sum(list1)/len(list1)
                print("After Mean of operation::",moflist)
            
            elif list_operation == 10:
                print("You have selected the Median operation in List::",list1)
                mdoflist=list1[(len(list1)-1)//2:(len(list1)+2)//2]
                print("After Median of operation::",mdoflist)

            elif list_operation == 11:
                print("You have selected the Find/Index operation in List::",list1)
                try:
                    find_list=int(input("Enter the Find/Index element from list::"))
                    findoflist=list1.index(find_list)
                    print("After Find/Index of operation::",findoflist)
                except Exception as error:
                    print(error)   
                    print("Find/Index elements is not available in the list::","User Input::",find_list,"Actual List::",list1)    
            
            elif list_operation == 12:
                print("You have selected the Count/Frequency operation in List::Current_list",list1)
                try:
                    cnt_list=int(input("Enter the element to find Count/Frequency from list::"))
                    cntoflist=list1.count(cnt_list)
                    print(f"After Count/Frequency of operation::",cntoflist,"User Input::",cnt_list)
                except Exception as error:
                    print(error)   
                    print("Count/Frequency elements is not available in the list::","User Input::",cnt_list,"Actual List::",list1)
                
            
            elif list_operation == 13:
                print("You have selected the Remove operation in List::",list1)
                try:
                    rm_list=int(input("Enter the Remove element from list::"))
                    rmoflist=list1.remove(rm_list)
                    print("After Remove of operation::",rmoflist)
                except Exception as error:
                    print(error)   
                    print("Remove elements is not available in the list::","User Input::",rm_list,"Actual List::",list1)    
  
            elif list_operation == 14:
                print("You have selected the Copy operation in List::")
                cpoflist=list1
                print("After Find of Copy::",cntoflist)

            elif list_operation == 15:
                print("You have selected the Reverse operation in List::",list1)
                reoflist=list1[::-1]
                print("After completes of Reverse Operation::",reoflist)       

            elif list_operation == 16:
                break
        
            else:
                print("You have selected Invalid Operation in List!!")

    elif user_select == 2:
        print("You have selected the Tuple data structure and welcome to the Tuble!!")


    elif user_select == 3:

        print("You have selected the Set data structure and welcome to the Set!!")
    
        set1=set_create()
        
        while True:
            print("1.Add","\n2.Pop","\n3.Sum","\n4.Max","\n5.Min","\n6.Length","\n7.Intersection","\n8.Union",
                  "\n9.Count","\n16.Exit")

            set_operation=int(input("Please select any of the above operations to peform further Set process::" ))
            
            if set_operation == 1:
                print("You have selected the Add operation in Set::Current Set",set1)
                set1add=set_add()
                print("After add operation in the elements::Current Set is::",set1add)
                
            elif set_operation == 2:
                print("You have selected the Pop operation in Set::Current Set",set1)
                set1pop=set_pop()
                print("After poping element in the Set::",set1pop)
                
            elif set_operation == 3:
                print("You have selected the Sum operation in Set::Current Set",set1)
                set1sum=set_sum()
                print("After Sum element in the Set::",set1sum)
                
            elif set_operation == 4:
                print("You have selected the Max operation in Set::Current Set",set1)
                set1max=set_max()
                print("After Max element in the Set::",set1max)
                
            elif set_operation == 5:
                print("You have selected the Min operation in Set::Current Set",set1)
                set1min=set_min()
                print("After Min element in the Set::",set1min)

            elif set_operation == 6:
                print("You have selected the Length operation in Set::Current Set",set1)
                set1len=len(set1)
                print("After Length element in the Set::",set1len)
                
            elif set_operation == 7:
                print("You have selected the Intersection operation in Set::Current Set",set1)
                set2=set_create()
                set1int=set_intersection()
                print("After Intersection of Two element in the Set::",set1int)
                
            elif set_operation == 8:
                print("You have selected the Union operation in Set::Current Set",set1)
                set2=set_create()
                set1uni=set_union()
                print("After Union of Two element in the Set::",set1uni)
                
            elif set_operation == 16:
                break


    elif user_select == 4:
        print("You have selected the Dictionary data structure and welcome to the Dictionary!!")

        dict1=dict_create()
      
        while True:

            print("1.Add","\n2.Pop","\n3.Update","\n4.Max","\n5.Min","\n6.Exit")

            dict_operation=int(input("Please select any of the above operations to peform further Dictionary process::" ))
            
            if dict_operation == 1:
                print("You have selected the Add operation in Dict::Current Dict",dict1)
                dict1add=dict_add()
                print("After add operation in the elements::Current Dict is::",dict1add)
                
            elif dict_operation == 2:
                print("You have selected the Pop operation in Dict::Current Dict",dict1)
                dict1pop=dict_pop()
                print("After poping element in the Dict::",dict1pop)
                
            elif dict_operation == 3:
                print("You have selected the Update operation in Dict::Current Dict",dict1)
                dict1update=dict_update()
                print("After poping element in the Dict::",dict1update)
                
            elif dict_operation == 4:
                print("You have selected the Max operation in Dict::Current Dict",dict1)
                dict1max=dict_max()
                print("After poping element in the Dict::",dict1max)
                
            elif dict_operation == 5:
                print("You have selected the Min operation in Dict::Current Dict",dict1)
                dict1min=dict_min()
                print("After poping element in the Dict::",dict1min)
                
            elif dict_operation == 6:                
                break
    elif user_select == 5:
        break

    else:
        print("You have selected Invalid Operation!!")

print("End of Data structure calculator!!!")
