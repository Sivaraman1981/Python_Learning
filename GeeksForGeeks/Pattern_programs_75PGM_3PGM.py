#Pattern Search
#Program1
#Program to print the pattern ‘G’

def Pattern(line):
    pat=""
    for i in range(0,line):   
        for j in range(0,line):    
            if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
                i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2)
                and j > line-5 and j < line-1) or (j == line-2 and
                i != 0 and i != line-1 and i >=((line-1)/2))): 
                pat=pat+"*"  
            else:     
                pat=pat+" "  
        pat=pat+"\n"  
    return pat
  
# Driver Code
line = 7
print(Pattern(line))

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
  ***  
 *     
 *     
 * *** 
 *   * 
 *   * 
  ***  

#Program2
#Python | Print an Inverted Star Pattern

n=10
for i in range (n, 0, -1):
    print((n-i) * ' ' + i * '*')


Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
**********
 *********
  ********
   *******
    ******
     *****
      ****
       ***
        **
         *


#Program3
#Python 3 | Program to print double sided stair-case pattern


def pattern(n):
    for i in range(1,n+1):
        k =i + 1 if(i % 2 != 0) else i
        for g in range(k,n):
            if g>=k:
                print(end="  ")
        for j in range(0,k):
            if j == k - 1:
                print(" * ")
            else:
                print(" * ", end = " ")
n = 10
pattern(n)



========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
                 *   * 
                 *   * 
             *   *   *   * 
             *   *   *   * 
         *   *   *   *   *   * 
         *   *   *   *   *   * 
     *   *   *   *   *   *   *   * 
     *   *   *   *   *   *   *   * 
 *   *   *   *   *   *   *   *   *   * 
 *   *   *   *   *   *   *   *   *   * 
