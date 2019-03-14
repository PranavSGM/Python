state_capital = {
'Andhra Pradesh' : 'Hyderabad',
'Arunachal Pradesh' : 'Itanagar',
'Assam' : 'Dispur',
'Bihar' : 'Patna',
'Chhattisgarh' : 'Raipur',
'Goa' : 'Panaji',
'Gujarat' : 'Gandhinagar',
'Haryana' : 'Chandigarh',
'Himachal Pradesh' : 'Shimla',
'Jammu and Kashmir' : 'Srinagar',
#'Jammu and Kashmir' : 'Srinagar|Jammu',
'Jharkhand' : 'Ranchi', 
#'Karnataka' : 'Bangaluru|Bangalore',
'Karnataka' : 'Bangalore',
'Kerala' : 'Thiruvananthapuram',
'Madhya Pradesh' : 'Bhopal',
'Maharashtra' : 'Mumbai',
'Manipur' : 'Imphal',
'Meghalaya' : 'Shillong',
'Mizoram' : 'Aizawl',
'Nagaland' : 'Kohima',
'Odisha' : 'Bhubaneswar',
'Punjab' : 'Chandigarh',
'Rajasthan' : 'Jaipur',
'Sikkim' : 'Gangtok',
'Tamil Nadu' : 'Chennai',
'Telangana' : 'Hyderabad',
'Tripura' : 'Agartala',
'Uttar Pradesh' : 'Lucknow',
'Uttarakhand' : 'Dehradun',
'West Bengal' : 'Kolkata'
}

UnionTerritories_capital = {
'Andaman and Nicobar Islands' : 'Port blair',
'Chandigarh' : 'Chandigarh',
'Dadar and Nagar Haveli' : 'Silvassa',
'Daman and Diu' : 'Daman',
'Delhi' : 'Delhi',
'Lakshadweep' : 'Kavaratti',
'Pondicherry' : 'Pondicherry'
}

import random
import os
import time

clear = lambda: os.system('cls')
clear()
print("\n\n\nWelcome to The State-Capital Quiz !")
print("""\n\n\nGame Rules !
There will be 2 rounds.
Round-1 : Checking the Capital of States
Round-2 : Checking the Capital of Union Territories

Each Round is marked seperately as follow:
Round-1: Will have 5 Questions with each correct gives +3   and each wrong gives -1
Round-2: Will have 2 Questions with each correct gives +2.5 and each wrong gives -0

Winning Prizes in the Games:-
Each Game costs you => INR 50

Prizes are as per the Score bracket below ->
     Result = 20 ,  GIVES INR 100
20 < Result <= 15 , GIVES INR 50
15 < Result <= 10,  GIVES INR 40 
10 < Result <= 5,   GIVES INR 30
5  < Result <= 0,   GIVES INR 20
0  < Result <= -5,  GIVES INR 10

" ON ALL WRONG ATTEMPTS, YOU STILL GET INR 10, SO JUST ATTEMP EVERY QUESTION "
""")

gamestart = input("""\n\n\n
Enter '1' to Start the Game !
Enter '2' to Revise !
Enter '3' to Exit the Game !
""")
states = list(state_capital.keys())
unionterritories = list(UnionTerritories_capital.keys())
if(gamestart == "1"):
    clear()
    print("\n\n\nRound-1")
    countdown = 3
    for count in reversed(range(countdown,0,-1)):
        print("\n\n... "+str(count)+" ...")
        time.sleep(1)
    print('\n...... GO ! ......')
    time.sleep(2)
    score = 0
    for i in [1,2,3,4,5]:
        clear()
        print("\nQues-"+str(i))
        state = random.choice(states)
        capital = state_capital[state]
        capital_guess = input("What is the capital of " + state + "? ")
        
        if capital_guess.lower() == capital.lower():
            score += 3
            print("""Correct Answer ! 
            Nice Job !
            Current Score = """+str(score)+"/20")
            time.sleep(3)
        else:
            score -= 1
            print("""Wrong Answer ! 
            The Capital of """+ str(state) + " is " + str(capital)+ """ .
            Current Score = """+str(score)+"/20")
            time.sleep(5)
            
    # Round -2        
    clear()
    print("\n\n\nRound-2")
    countdown = 3
    for count in reversed(range(countdown,0,-1)):
        print("... "+str(count)+" ...")
        time.sleep(1)
    print('...... GO ! ......')
    time.sleep(3)
    for i in [1,2]:
        clear()
        print("\nQues-"+str(i))
        state = random.choice(unionterritories)
        capital = UnionTerritories_capital[state]
        capital_guess = input("What is the capital of " + state + "? ")
        
        if capital_guess.lower() == capital.lower():
            score += 2.5
            print("""Correct Answer ! 
            Nice Job !
            Current Score = """+str(score)+"/20")
            time.sleep(3)
        else:
            score -= 0
            print("""Wrong Answer ! 
            The Capital of """+ str(state) + " is " + str(capital)+ """ .
            Current Score = """+str(score)+"/20")
            time.sleep(3)
    if score == 20:
        winningamount = 100
    elif (score<20 and score>=15):
        winningamount = 50
    elif (score<15 and score>=10):
        winningamount = 40
    elif (score<10 and score>=5):
        winningamount = 30
    elif (score<5 and score>=0):
        winningamount = 20
    elif (score<0 and score>=-5):
        winningamount = 10
    print("""Test is Completed!
    Your Final Score = """+str(score)+"""
    Your winning amount = INR """+str(winningamount))
elif(gamestart=="3"):
    print("\n\n\nYou are now Exiting the Game !")
elif(gamestart=="2"):
    clear()
    print("\n\n\nRevise for State-Capital !")
    for k,v in state_capital.items():
        print("Capital of '"+k+"' is '"+v+"'")
        
    next = input("""\n\n\n\n\n
    When Done enter '1' to go to next revision screen
    OR enter '2' to finish Revision and start Again
    """)    
    if(next=="1"):
        clear()
        print("\n\n\nRevise for UT's-Capital !")
        for k,v in UnionTerritories_capital.items():
            print("Capital of '"+k+"' is '"+v+"'")
        next = input("\n\n\n\n\nWhen Done enter '2' to finish Revision and start again")
    else:
        print("Exit game!")
else:
    print("Invalid Input, Star again")