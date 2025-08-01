# Build a Quiz app which can :

# Randomly chooses multiple choice questions then 
# Ask 5 multiple-choice questions.
# Track score and display result at the end.

import random
questionData=[
    {
        "question":"What is the output of print(2 ** 3)?",
        "options":{
            "A":"6",
            "B":"8",
            "C":"9",
            "D":"5"
        },
        "answer":"B"
    },
    {
        "question":"Which datatype is immutable in python ?",
        "options":{
            "A":"List",
            "B":"Dictionary",
            "C":"Set",
            "D":"Tuple"
        },
        "answer":"D"
    },
    {
        "question":"What does 'len()' function do?",
        "options":{
            "A":"Prints list",
            "B":"Deletes elements",
            "C":"Returns length",
            "D":"Sorts list"
        },
        "answer":"C"
    },
    {
        
        "question":"Which keyword is used for function in Python?",
        "options":{
            "A":"function",
            "B":"func",
            "C":"define",
            "D":"def"
        },
        "answer":"D"
    },
    {
        
        "question":"Which of the following is a loop in Python?",
        "options":{
            "A":"while",
            "B":"loop",
            "C":"repeat",
            "D":"do while"
        },
        "answer":"A"
    },
    { 
        "question":"What is the correct file extension for Python files?",
        "options":{
            "A":".pt",
            "B":".py",
            "C":".python",
            "D":".p"
        },
        "answer":"B"
    },
    {
        "question":"Which operator is used for checking equality?",
        "options":{
            "A":"=",
            "B":"==",
            "C":"===",
            "D":"!="
        },
        "answer":"B"
    },
    {
        "question":"What will be the output of print('Hello' + 'World')?",
        "options":{
            "A":"Hello World",
            "B":"Hello + World",
            "C":"HelloWorld",
            "D":"Hello+World"
        },
        "answer":"C"
    },
    {
        "question":"Which of the following is not a keyword in Python?",
        "options":{
            "A":"if",
            "B":"then",
            "C":"self",
            "D":"elif"
        },
        "answer":"B"
    },
    {
        "question":"What does 'append()' method do?",
        "options":{
            "A":"Deletes last item",
            "B":"Adds item at end",
            "C":"Clears list",
            "D":"Sorts list"
        },
        "answer":"B"
    }
]


def generateNumber():
    return random.randrange(0,10)

def askQuestion(questionList):
    for i in questionList:
        print(f"\nQ> {questionData[i].get('question')}")
        options=questionData[i].get("options")
        for opt in options:
            print(f"\t{opt}. {options.get(opt)}")
        
        answer=str(input("Choose and enter the option : ")).upper()
        if answer==questionData[i].get("answer"):
            global score
            score +=1
            print(f"Yeah {name} , Correct answer")
        else:
            print(f"Shit {name} , Wrong answer")
    print("++++++++++++++++++++++++++++++++++++++")
    print(f"{name} , You have completed the quiz\nYour score is {score}")




name=str(input("Enter your name player : "))
print(f"\nDear {name} , Welcome to the QUIZ\nyou have to give answers of five quiz questions\nselect A,B,C or D options according to the questions\n")
print("-----------------------------------------------")
score=0
questionList=[]
while len(questionList)<5:
    num=generateNumber()
    if num not in questionList:
        questionList.append(num)
# print(questionList)
askQuestion(questionList)