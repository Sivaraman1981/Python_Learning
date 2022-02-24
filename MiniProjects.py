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
    print(i)
    

    User_In = input("Enter the values of rock paper scissor:::")
    print("User_In::",User_In)
    sys_ran = random.choice(Li1)
    print(sys_ran)
    
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
        print("User_In::User won the game")
    elif sys_ran =='rock' and User_In =='scissor':
        v_sys=v_sys+1
        print("sys_ran::System won the game")
    elif User_In =='paper' and sys_ran =='scissor':
        v_sys=v_sys+1
        print("User_In::System won the game")
    elif sys_ran =='paper' and User_In =='scissor':
        v_user=v_user+1
        print("User_In::User won the game")
    elif User_In =='rock' and sys_ran =='paper':
        v_sys=v_sys+1
        print("sys_ran::System won the game")
    elif sys_ran =='rock' and User_In =='paper':
        v_user=v_user+1
        print("User_In::User won the game")

print("\nTotal No of Games::",NoofGames)
print("System points::",v_sys)
print("User points::",v_user)
print("Total tie points::",v_tie)

if v_user > v_sys:
    print("\nUSER wins the game !!! Congrats !!!!")
elif v_sys > v_user:
    print("\nSYSTEM wins the game !!! Congrats !!!!")



Output:
========================================== RESTART: C:\Users\sivar\AppData\Local\Programs\Python\Python310\1.py =========================================
Enter the number of games do you want to play::3
0
Enter the values of rock paper scissor:::rock
User_In:: rock
rock
The game is tie
1
Enter the values of rock paper scissor:::paper
User_In:: paper
scissor
User_In::System won the game
2
Enter the values of rock paper scissor:::scissor
User_In:: scissor
rock
sys_ran::System won the game

Total No of Games:: 3
System points:: 2
User points:: 0
Total tie points::
 1

SYSTEM wins the game !!! Congrats !!!!

======================================== RESTART: C:/Siva_OldLaptop/Laptop_E_prompt/NOTES/Python/MiniProjects.py ========================================
Enter the number of games do you want to play::3
0
Enter the values of rock paper scissor:::paper
User_In:: paper
paper
The game is tie
1
Enter the values of rock paper scissor:::rock
User_In:: rock
scissor
User_In::User won the game
2
Enter the values of rock paper scissor:::scissor
User_In:: scissor
paper
User_In::User won the game

Total No of Games:: 3
System points:: 0
User points:: 2
Total tie points:: 1

USER wins the game !!! Congrats !!!!
