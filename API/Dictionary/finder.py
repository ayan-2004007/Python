# Make a Dictionary / Word meaning finder using public API
# Features :
#     The system should take a word
#     Give the all possible definations of the words

import requests
import json

def displayMeanings(data,word):
    print("="*150)
    print(" "*50,"MY DICTIONARY")
    print("="*150)
    print(f"{'Your word : ':<30}{data[0]['word']}")
    print("="*150)
    if len(data[0]["meanings"])>0:
        for i in data[0]["meanings"]:
            print(f"{'Parts of Speech :':<30}{i['partOfSpeech'].upper()}")
            print(f"{'Definition : ':<30}{i['definitions'][0]['definition']}")
            print("-"*150)
    else:
        print(f"There is no data found for the word : {word}")

def main():
    trigger=True
    while trigger:
        word=str(input("Enter the word you want to know meaning (Press 1 for exit) : "))
        if word=="1":
            trigger=False
            exit(0)
        API=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        res=requests.get(API)
        data=res.json()
        if res.status_code!=200:
            print(f"{data['message']}")
            continue
        displayMeanings(data,word)

if __name__=="__main__":
    main()