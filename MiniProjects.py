#rock + rock ==> Tie
#paper + paper ==> Tie
#scissor + scissor ==> Tie
#rock + scissor ==> rock
#paper + scissor ==> scissor 
#rock + paper  ===> paper
#Total of number games: 3
#System points ==> 0
#User point ==> 2
#Tie ===> 1
#USER wins the game !!! Congrats !!!!

import random

NoofGames = int(input("Enter the number of games do you want to play::"))

Li1 = ["rock","paper","scissor"]

v_tie=0
v_user=0
v_sys=0

for i in range(NoofGames):


    User_In = input("Enter the values of rock paper scissor:::")
    print("User Input::",User_In)
    sys_ran = random.choice(Li1)
    print("System Input::",sys_ran)
    
    if User_In =='rock' and (User_In==sys_ran):
        v_tie=v_tie+1
        print("The game is tie")
    elif User_In =='paper' and (User_In==sys_ran):
        v_tie=v_tie+1
        print("The game is tie")
    elif User_In =='scissor' and (User_In==sys_ran):
        v_tie=v_tie+1
        print("The game is tie")
    elif User_In =='rock' and sys_ran =='scissor':
        v_user=v_user+1
        print("User won the game")
    elif sys_ran =='rock' and User_In =='scissor':
        v_sys=v_sys+1
        print("System won the game")
    elif User_In =='paper' and sys_ran =='scissor':
        v_sys=v_sys+1
        print("System won the game")
    elif sys_ran =='paper' and User_In =='scissor':
        v_user=v_user+1
        print("User won the game")
    elif User_In =='rock' and sys_ran =='paper':
        v_sys=v_sys+1
        print("System won the game")
    elif sys_ran =='rock' and User_In =='paper':
        v_user=v_user+1
        print("User won the game")
    else:
        print("Invalid Input given by User")

print("\nTotal No of Games::",NoofGames)
print("System points::",v_sys)
print("User points::",v_user)
print("Total tie points::",v_tie)

if v_user > v_sys:
    print("\nUSER wins the game !!! Congrats !!!!")
elif v_sys > v_user:
    print("\nSYSTEM wins the game !!! Congrats !!!!")
elif v_user == v_sys and (v_user>0 and v_sys>0):
    print("\nUSER & SYSTEM both are wins the game !!! Congrats !!!!")
elif v_user == 0 and v_sys == 0:
    print("\nUSER & SYSTEM both are not wins the game !!! Congrats !!!!")

Output:

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Enter the number of games do you want to play::3
Enter the values of rock paper scissor:::rock
User Input:: rock
System Input:: paper
System won the game
Enter the values of rock paper scissor:::paper
User Input:: paper
System Input:: rock
User won the game
Enter the values of rock paper scissor:::scissor
User Input:: scissor
System Input:: scissor
The game is tie

Total No of Games:: 3
System points:: 1
User points:: 1
Total tie points:: 1

USER & SYSTEM both are wins the game !!! Congrats !!!!

========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\2.py =========================================
Enter the number of games do you want to play::2
Enter the values of rock paper scissor:::rrrr
User Input:: rrrr
System Input:: paper
Invalid Input given by User
Enter the values of rock paper scissor:::rock
User Input:: rock
System Input:: rock
The game is tie

Total No of Games:: 2
System points:: 0
User points:: 0
Total tie points:: 1

USER & SYSTEM both are not wins the game !!! Congrats !!!!
