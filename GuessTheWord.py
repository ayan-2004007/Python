# Build a Guess the word game 
# Jumble a word (e.g., elephant → tnpahlee)
# Ask user to guess the original word.

import random
wordData={
    1:"elephant",
    2:"apple",
    3:"tiger",
    4:"house",
    5:"chair",
    6:"water",
    7:"green",
    8:"light",
    9:"smile",
    10:"phone",
    11:"bread",
    12:"planet",
    13:"garden",
    14:"window",
    15:"bottle",
    16:"pencil",
    17:"laptop",
    18:"mirror",
    19:"bucket",
    20:"jungle",
    21:"rocket",
    22:"triangle",
    23:"umbrella",
    24:"keyboard",
    25:"mountain",
    26:"airplane",
    27:"football",
    28:"sandwich",
    29:"building",
    30:"calendar"
}


def generateNumber():
    return random.randrange(1,31)

def jumble(original):
    wordList=list(original)
    random.shuffle(wordList)
    return "".join(wordList)


name=str(input("Enter your name player : "))
print("GUESS THE WORD")
print("-----------------------------------------")
originalWord = wordData[generateNumber()]
jumbledWord=jumble(originalWord)
print(f"You challenge is : {jumbledWord}")
playerWord=str(input(f"Enter what you are thinking : "))
if playerWord==originalWord:
    print(f"Yeah {name} , you arranged it right")
else:
    print(f"Shit {name} , you coudn't arrange it right")
