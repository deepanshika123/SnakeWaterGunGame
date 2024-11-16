import random

instruction_shown=False

def show_instruction():
 global instruction_shown
 if not instruction_shown:
  print('''Instruction!
    Choose snake water and gun and play with computer
    Enjoy your Game''' )
  instruction_shown=True

show_instruction()
while True:
 computer=random.choice([-1,0,1])
 yourstring=input("Enter your choice: ")
 yourdict={"snake": 1 , "water" : 0 , "gun" :-1}
 reversedict={1:"snake" , 0:"water" , -1:"gun"}

 you=yourdict[yourstring]

 print(f"You chose  {reversedict[you]} \n computer chose {reversedict[computer]}")


 if(computer==you):
    print("It's a Draw")

 else:
    if(computer==1 and you==0):
        print("Computer Win!")
    elif(computer==-1 and you==1):
        print("Computer Win!")
    elif(computer==0 and you==-1):
        print("Computer Win!")
    elif(computer==1 and you==-1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Win!")
    else:
        print("oops! Something went wrong")

 replay = input("Do you want to play again? (yes/no): ").lower()
 if replay != 'yes':
  print("Thanks for playing")
  break
 
   
