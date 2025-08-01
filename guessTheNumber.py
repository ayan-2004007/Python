# Built a guess the number game which has limited guessing chance 

# Algorithm : 
# Generate a random number between 1 to 100
# The player has only 8 chances to guess the right number
# The game should display a message on the basis of situation after every guess of player
# Try something lower values -> if user guesses a high number
# Try somehting higher values -> if user guesses a low number
# If he cant guess the number within 8 guess chnaces then print user looses and if he guesses the right number then print user won

import random
def generateNumber():
    return random.randrange(1,101)

name=str(input("Enter your name player : "))
print("GUESS THE NUMBER (100)")
print("You have total 8 chances")
print("___________________________________")
computerNumber=generateNumber()
count=0
while count<8:
    print("___________________________________")
    playerGuess=int(input(f"Enter what you are thinking : "))
    if playerGuess>computerNumber:
        count+=1
        print(f"{name} , try to guess lower !\nYou have {8-count} chances left")
    elif playerGuess<computerNumber:
        count+=1
        print(f"{name} , Try to guess higher !\nYou have {8-count} chances left")
    elif playerGuess==computerNumber:
        print(f"yeah {name} , you guessed it right")
        print(f"Your point {8-count}")
        break
if count==8:
    print(f"Shit {name} ! You loose")