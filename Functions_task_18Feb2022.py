#User Def functions (4)
#Write function to concatenate three strings

def concatenatestring(str1, str2, str3):
    return str1 + str2 + str3
  
string1 = input("Enter string 1: ") 
string2 = input("Enter string 2: ")
string3 = input("Enter string 3: ")

print(concatenatestring(string1, string2, string3))

#Write a function multiply three different integers and return a int

def concatenatestring(int1, int2, int3):
    return int(int1 * int2 * int3)
  
integer1 = int(input("Enter Value 1: "))
integer2 = int(input("Enter Value 2: "))
integer3 = int(input("Enter Value 3: ")) 

print(concatenatestring(integer1, integer2, integer3))

#Write a function to return middle char of the string
def middle_string(str1):
    middle_len=len(str1)
    middle_len_pos= middle_len//2
    return(str1[middle_len_pos])

string1= input("enter the string to find out middle string::")
print(middle_string(string1))
      
#write a function to return whether middle character is vowel or not 
def middle_string_vowel(str1):
    middle_len_pos= len(str1)//2
    middle_value=str1[middle_len_pos]
    print("middle value is::",middle_value)
    
    if ( middle_value in ['a','e','i','o','u','A','E','I','O','U']):
    	return "The string middle is Vowel" 
    else:
    	return "The string middle is not Vowel"

string1= input("enter the string to find out middle string is vowel or not::")
print(middle_string_vowel(string1))
