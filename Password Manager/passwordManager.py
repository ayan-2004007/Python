# Build a Password generator and  managing system
# Features:
#     Generate strong passwords based on user choices (length)
#     Password must contain atleast one Uppercase, Lowercase, Number and symbol
#     Save passwords with website names
#     Retrieve passwords from the file

# Data file structure (.csv)
# Website Name | Website Link | Passwords

import os
import csv
import random
passData={
    "lowercase":["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
    "uppercase":["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
    "numbers":["0","1","2","3","4","5","6","7","8","9"],
    "symbols":["!","@","#","$","%","&","-","_",".","?","~"]
}

def generateRandomIndex(start,end):
    return random.randrange(start,end)
def generatePassword():
    length=int(input("Enter the length of our new password : "))
    if length<=4:
        print("Password length must be greater than 4 !")
        return ""
    newpass=""
    newpass+=passData["lowercase"][generateRandomIndex(0,26)]
    newpass+=passData["uppercase"][generateRandomIndex(0,26)]
    newpass+=passData["numbers"][generateRandomIndex(0,9)]
    newpass+=passData["symbols"][generateRandomIndex(0,11)]
    try:
        for i in range(length-4):
            op=generateRandomIndex(1,5)
            if op==1:
                index=generateRandomIndex(0,26)
                newpass+=passData["lowercase"][index]
            elif op==2:
                index=generateRandomIndex(0,26)
                newpass+=passData["uppercase"][index]
            elif op==3:
                index=generateRandomIndex(0,9)
                newpass+=passData["numbers"][index]
            elif op==4:
                index=generateRandomIndex(0,11)
                newpass+=passData["symbols"][index]
        newpasslist=list(newpass)
        random.shuffle(newpasslist)
        newpass="".join(newpasslist)
        return newpass
    except Exception as e:
        print(f"Something went wrong while generating the password : {e}")

def allData(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            print(f"{'Website Name':<20} {'Website Link':<50} {'Password':<15}")
            print("-"*100)
            for row in reader:
                print(f"{row[0]:<20} {row[1]:<50} {row[2]:<15}")
    except Exception as e:
        print(f"Something went wrong while fetching the data from the file: {e}")

def saveNewPassword(path):
    found=False
    name=str(input("Enter the website name : ")).lower().strip()
    link=str(input("Enter the link of the website : ")).lower().strip()
    password=str(input("Enter the password : "))
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if row[0]==name:
                    found=True
                    break
            if found:
                print(f"There is already a password exists for the site {name}")
            else:
                with open(path,mode="a",newline="") as f:
                    writer=csv.writer(f)
                    writer.writerow([name,link,password])
                    print("New password saved successfully")
    except Exception as e:
        print(f"Something went wrong while saving the new password ; {e}")

def search(path):
    try:
        with open(path,mode="r",newline="") as file:
            name=str(input("Enter the name of the website you want to search : ")).lower().strip()
            reader=csv.reader(file)
            found=False
            print(f"{'Website Name':<20} {'Website Link':<50} {'Password':<15}")
            print("-"*100)
            next(reader)
            for rows in reader:
                if rows[0]==name:
                    print(f"{rows[0]:<20} {rows[1]:<50} {rows[2]:<15}")
                    found=True
            if not found:
                print(f"There is no data for website named : {name}")
    except Exception as e:
        print(f"Something went wrong while seraching : {e}")

def main():
    path=os.path.join(os.path.dirname(__file__),"data.csv")
    trigger=True
    while trigger:
        print("="*100)
        choice=int(input("What do you want to do ?\n1 for create a strong password\n2 for see all data\n3 for save a new password\n4 for search any password\n5 for exit\n"))
        print("="*100)
        if choice==1:
            newpass=generatePassword()
            print(f"Your password is : {newpass}")
        elif choice==2:
            allData(path)
        elif choice==3:
            saveNewPassword(path)
        elif choice==4:
            search(path)
        elif choice==5:
            trigger=False
        else:
            print("Invalid input ! Choose a valid option")

if __name__=="__main__":
    main()