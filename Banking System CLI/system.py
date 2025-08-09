# Make a Banking System CLI
# Features :
#     Make Customers, Account and transactions
#     Store data in a .json file
#     Add password protected login
#     The user can perform operations like check balance, Deposit , Withdrawl
#     An user can only perform operations if he or she is logged in (controll the login data using a runtime variable)


import os
import json
import random
from datetime import datetime
isLogin=False
customerData={}

def generateRandom(start,end):
    return random.randrange(start,end)

def login(custPath):
    try:
        with open(custPath,"r") as file:
            id=str(input("Enter your customer id : ")).upper().strip()
            password=str(input("Enter your password : ")).strip()
            data=json.load(file)
            found=False
            for cust in data:
                if cust["customerId"]==id and password==cust["password"]:
                    found=True
                    global isLogin,customerData
                    isLogin=True
                    customerData=cust
                    break
            if found:
                print(f"Hello {customerData['name']} , youe are logged in successfully ")
            else:
                print(f"Invalid Credentials !")
    except Exception as e:
        print(f"Something went wrong while login : {e}")

def updateCustomerData(custPath):
    try:
        with open(custPath,"r") as fr:
            custData=json.load(fr)
            global customerData
            done=False
            for cust in custData:
                if cust["customerId"]==customerData["customerId"]:
                    cust["balance"]=customerData["balance"]
                    done=True
            if done:
                with open(custPath,"w") as fw:
                    json.dump(custData,fw,indent=4)
            else:
                print("Cannot update customer data")
    except Exception as e:
        print(f"Something went wrong while updating the customer data : {e}")

def checkBalance(custPath):
    global isLogin,customerData
    if not isLogin:
        print("You have to login first to check balance !")
        login(custPath)
    if customerData:
        print(f"Hello {customerData['name']} , your current balance is : {customerData['balance']}")

def deposit(custPath,transactionPath):
    global isLogin,customerData
    if not isLogin:
        print("You have to login first to deposit amount !")
        login(custPath)
    try:
        with open(transactionPath,"r") as tran:
            transactionData=json.load(tran)
            depAmount=int(input("Enter the deposit amount : "))
            customerData["balance"]+=depAmount
            newTransaction={
                "transactionId": "T"+str(generateRandom(1,10000)),
                "customerId":customerData["customerId"],
                "type": "deposit",
                "amount":depAmount,
                "date":str(datetime.today().date()),
                "time":str(datetime.today().time())
            }
            transactionData.append(newTransaction)
            with open(transactionPath,"w") as t:
                json.dump(transactionData,t,indent=4)
                updateCustomerData(custPath)
            print(f"Deposit Amount : {depAmount} successfull")
    except Exception as e:
        print(f"Something went wrong while deposit : {e}")

def withdrawl(custPath,transactionPath):
    global isLogin,customerData
    if not isLogin:
        print("You have to login first to withdrawl amount !")
        login(custPath)
    try:
        with open(transactionPath,"r") as tran:
            transactionData=json.load(tran)
            withAmount=int(input("Enter the withdrawl amount : "))
            customerData["balance"]-=withAmount
            newTransaction={
                "transactionId": "T"+str(generateRandom(1,10000)),
                "customerId":customerData["customerId"],
                "type": "withdrawl",
                "amount":withAmount,
                "date":str(datetime.today().date()),
                "time":str(datetime.today().time())
            }
            transactionData.append(newTransaction)
            with open(transactionPath,"w") as t:
                json.dump(transactionData,t,indent=4)
                updateCustomerData(custPath)
            print(f"Withdrawl Amount : {withAmount} Successfull")
    except Exception as e:
        print(f"Something went wrong while withdrawl : {e}")

def main():
    custPath=os.path.join(os.path.dirname(__file__),"customers.json")
    transactionPath=os.path.join(os.path.dirname(__file__),"transactions.json")
    trigger=True
    try:
        while trigger:
            print("="*100)
            ch=int(input("What do you want to do ?\npress 1 for login\nPress 2 for check balance\nPress 3 for deposit\nPress 4 for withdrawl\nPress 5 for exit\n"))
            print("="*100)
            match ch:
                case 1:
                    login(custPath)
                case 2:
                    checkBalance(custPath)
                case 3:
                    deposit(custPath,transactionPath)
                case 4:
                    withdrawl(custPath,transactionPath)
                case 5:
                    trigger=False
                case _:
                    print("Invalid input !")
    except Exception as e:
        print(f"You entered something wrong : {e}")

if __name__=="__main__":
    main()