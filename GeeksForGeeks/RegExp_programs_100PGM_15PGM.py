#RegEXP

#1.Python – Check if String Contain Only Defined Characters using Regex

import re  
  
def check(str, pattern):
    if re.search(pattern, str):
        print("Valid String")
    else:
        print("Invalid String")
  
# _driver code
pattern = re.compile('^[1234]+$')
check('2134', pattern)
check('349', pattern)

#2.Python program to Count Uppercase, Lowercase, special character and numeric values using Regex

import re
 
 
string = "ThisIsGeeksforGeeks !, 123"
 
# Creating separate lists using
# the re.findall() method.
uppercase_characters = re.findall(r"[A-Z]", string)
lowercase_characters = re.findall(r"[a-z]", string)
numerical_characters = re.findall(r"[0-9]", string)
special_characters = re.findall(r"[, .!?]", string)
 
print("The no. of uppercase characters is", len(uppercase_characters))
print("The no. of lowercase characters is", len(lowercase_characters))
print("The no. of numerical characters is", len(numerical_characters))
print("The no. of special characters is", len(special_characters))

#3.The most occurring number in a string using Regex in python

import re 
from collections import Counter 
  
def most_occr_element(word):
      
    # re.findall will extract all the elements 
    # from the string and make a list
    arr = re.findall(r'[0-9]+', word)    
      
    # to store maxm frequency
    maxm = 0  
  
    # to store maxm element of most frequency
    max_elem = 0
      
    # counter will store all the number with 
    # their frequencies
    # c = counter((55, 2), (2, 1), (3, 1), (4, 1))    
    c = Counter(arr)
    
    # Store all the keys of counter in a list in
    # which first would we our required element    
    for x in list(c.keys()):
  
        if c[x]>= maxm:
            maxm = c[x]
            max_elem = int(x)
                  
    return max_elem
  
# Driver program 
if __name__ == "__main__": 
    word = 'geek55of55gee4ksabc3dr2x'
    print(most_occr_element(word))

#4.Python Regex to extract maximum numeric value from a string

import re
  
def extractMax(input):
    numbers = re.findall('\d+',input)
    numbers = map(int,numbers)
  
    print (max(numbers))
  
# Driver program
if __name__ == "__main__":
    input = '100klh564abc365bg'
    extractMax(input)

#5.Regex in Python to put spaces between words starting with capital letters

import re
   
def putSpace(input):
   
    # regex [A-Z][a-z]* means any string starting 
    # with capital character followed by many 
    # lowercase letters 
    words = re.findall('[A-Z][a-z]*', input)
   
    # Change first letter of each word into lower
    # case
    for i in range(0,len(words)):
        words[i]=words[i][0].lower()+words[i][1:]
    print(' '.join(words))
     
   
# Driver program
if __name__ == "__main__":
    input = 'BruceWayneIsBatman'
    putSpace(input)
