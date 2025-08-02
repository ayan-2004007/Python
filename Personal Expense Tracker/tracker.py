# Build a personal expense tracker (using .csv)

# Features :
# Add new expense
# view expenses by category and date
# total expenses 

# Expense record structure
# note | amount | category | date


import os
import csv

def addNewExpense(path):
    try:
        with open(path,mode="a",newline="") as file:
            writer=csv.writer(file)
            note=str(input("Enter the  note for new expense : ")).lower()
            amount=int(input("Enter the amount for the new expense : "))
            category=str(input("Enter the category of the new expense : " )).lower()
            date=str(input("Enter the date of the new expense (yyyy-mm-dd) : ")).strip().lower()
            writer.writerow([note,amount,category,date])
            print("New expenses added successfully")
    except Exception as e:
        print(f"Error occured while adding new expense : {e}")

def findByCategory(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            cat=str(input("Enter the category you are looking for : ")).strip().lower()
            foundData=[]
            total=0
            for row in reader:
                if row[2]==cat:
                    foundData.append(row)
                    total+=int(row[1])
            if len(foundData)>0:
                print(f"Found data according {cat}")
                for row in foundData:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
                print(f"The total amount expend on {cat} : {total}")
            else:
                print(f"There is no data for category : {cat}")
    except Exception as e:
        print(f"Error occured while fetching data : {e}")


def findByDate(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            foundData=[]
            date=str(input("Enter the date you are looking for (yyyy-mm-dd) : ")).strip().lower()
            for row in reader:
                if row[3]==date:
                    foundData.append(row)
            if len(foundData)>0:
                for row in foundData:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
            else:
                print(f"There is no data for date {date}")
    except Exception as e:
        print(f"Error occured while fetching the data : {e}")


def totalExpense(path):
    try:
        with open(path,mode='r',newline='') as file:
            reader=csv.reader(file)
            next(reader)
            total=0
            for row in reader:
                total+=int(row[1])
            print(f"The total expense amount is : {total}")
    except Exception as e:
        print(f"Error occured while calculating the expenses : {total}")
                


def main():
    path=os.path.join(os.path.dirname(__file__),"expense.csv")
    trigger=True
    while trigger:
        try:
            print("--------------------------------------------------------")
            choice=int(input("What do you want to do ?\n1 for add a new expense\n2 for view expenses by category\n3 for view expenses by date\n4 for finding total expense\n5 for exit\n"))
            print("--------------------------------------------------------")
            if choice==1:
                addNewExpense(path)
            elif choice==2:
                findByCategory(path)
            elif choice==3:
                findByDate(path)
            elif choice==4:
                totalExpense(path)
            elif choice==5:
                trigger=False
            else:
                print("Invalid input ! you entered wrong input")
        except Exception as e:
            print(f"you have entered something wrong : {e}")

if __name__=="__main__":
    main()