# Built a Rock, paper and scissors game where the player will play with the computer 

import random
choice={
    1:"rock",
    2:"paper",
    3:"scissor"
}

def generateNumber():
    return random.randrange(1,4)

name=str(input("Enter your name player : "))
print("ROCK - PAPER - SCISSOR")
print("-------------------------------------")
count=0
playerScore=0
computerScore=0
while count<3:
    computerChoice=generateNumber()
    print("-------------------------------------")
    playerChoice=int(input(f"{name}, What will you choose ?\n1 for Rock\n2 for Paper\n3 for Scissor\n"))
    if computerChoice==playerChoice:
        print(f"Draw match ! \nYou chose {choice.get(playerChoice)}\nComputer chose {choice.get(computerChoice)}")
        count+=1
    elif playerChoice==1 and computerChoice==2:
        print(f"Computer won ! \nYou chose {choice.get(playerChoice)}\nComputer chose {choice.get(computerChoice)}")
        computerScore+=1
        count+=1
    elif playerChoice==1 and computerChoice==3:
        print(f"You won ! \nYou chose {choice.get(playerChoice)}\nComputer chose {choice.get(computerChoice)}")
        playerScore+=1
        count+=1
    elif playerChoice==2 and computerChoice==1:
        print(f"You won ! \nYou chose {choice.get(playerChoice)}\nComputer chose {choice.get(computerChoice)}")
        playerScore+=1
        count+=1
    elif playerChoice==2 and computerChoice==3:
        print(f"Computer won ! \nYou chose {choice.get(playerChoice)}\nComputer chose {choice.get(computerChoice)}")
        computerScore+=1
        count+=1
    elif playerChoice==3 and computerChoice==1:
        print(f"Computer won ! \nYou chose {choice.get(playerChoice)}\nComputer chose {choice.get(computerChoice)}")
        computerScore+=1
        count+=1
    elif playerChoice==3 and computerChoice==2:
        print(f"You won ! \nYou chose {choice.get(playerChoice)}\nComputer chose {choice.get(computerChoice)}")
        playerScore+=1
        count+=1
    else:
        print("Invalid input!")

if playerScore>computerScore:
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Yeah {name} , You won the match\nYour score : {playerScore}")
else:
    print("+++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Shit {name}, You loose the match\nYour score : {playerScore}")