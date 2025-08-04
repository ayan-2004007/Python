# Build a contact book management system
# Features :
#     Add new contacts
#     search any contact by name or number
#     update any contact details
#     delete any contact

# Contact data structure
# Name | Phone number | Email | Address

import csv
import os

def allContacts(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            print(f"{'Name':<30} {'Phone Number':<15} {'Email':<40} {'Address':<80}")
            print("----------------------------------------------------------------------------------------------------")
            for row in reader:
                print(f"{row[0]:<30} {row[1]:<15} {row[2]:<40} {row[3]:<80}")
    except Exception as e:
        print(f"Something went wrong while fetching the contact data : {e}")

def searchByName(path,name):
    try:
        with open(path,mode="r",newline="") as file:
                reader=csv.reader(file)
                found=False
                next(reader)
                print(f"{'Name':<30} {'Phone Number':<15} {'Email':<40} {'Address':<80}")
                print("----------------------------------------------------------------------------------------------------")
                for row in reader:
                    if str(row[0])==name:
                        print(f"{row[0]:<30} {row[1]:<15} {row[2]:<40} {row[3]:<80}")
                        found = True
                        break
                if not found:
                    print(f"There is no record for name : {name}")
    except Exception as e:
        print(f"Something went wrong while seraching by name : {e}")


def searchByNumber(path,number):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            found=False
            next(reader)
            print(f"{'Name':<30} {'Phone Number':<15} {'Email':<40} {'Address':<80}")
            print("----------------------------------------------------------------------------------------------------")
            for row in reader:
                if row[1]==number:
                     found=True
                     print(f"{row[0]:<30} {row[1]:<15} {row[2]:<40} {row[3]:<80}")
                     break
            if not found:
                 print(f"There is no record for phone number : {number}")
    except Exception as e:
         print(f"Something went wrong while seraching by number : {e}")


def searchByEmail(path,mail):
     try:
          with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            found=False
            next(reader)
            print(f"{'Name':<30} {'Phone Number':<15} {'Email':<40} {'Address':<80}")
            print("----------------------------------------------------------------------------------------------------")
            for row in reader:
                   if str(row[2])==mail:
                        found=True
                        print(f"{row[0]:<30} {row[1]:<15} {row[2]:<40} {row[3]:<80}")
                        break
            if not found:
               print(f"There is no record for email : {mail}")
     except Exception as e:
          print(f"Something went wrong while seraching by email : {e}")

def searchSupport(path):
        choice=int(input("press 1 for search by name\npress 2 for search by phone number\npress 3 for search by email\n"))
        if choice==1:
             name=str(input("Enter the name to search : ")).lower()
             searchByName(path,name)
        elif choice==2:
             number=input("Enter the phone number to search : ")
             searchByNumber(path,number)
        elif choice==3:
             mail=str(input("Enter the email to serach : ")).lower()
             searchByEmail(path,mail)

def addNewContact(path):
     try:
          with open(path,mode="a",newline="") as file:
               writer=csv.writer(file)
               name=str(input("Enter the name of the new contact : ")).lower()
               number=int(input("Enter the phone number of the new contact : "))
               mail=str(input("Enter the email of the new contact : ")).lower()
               add=str(input("Enter the full address of the new contact : ")).lower()
               writer.writerow([name,number,mail,add])
               print("Contact added successfully")
     except Exception as e:
          print(f"Something went wrong while adding a new contact : {e}")

def deleteContact(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            header=next(reader)
            found=False
            number=input("Enter the phone number you want to delete : ").strip()
            temp=[]
            for row in reader:
                if row[1]==number:
                    found=True
                else:
                    temp.append(row)
            if found:
                print("The record deleted sucessfully")
                with open(path,mode="w",newline="") as f:
                    writer=csv.writer(f)
                    writer.writerow(header)
                    writer.writerows(temp)
            else:
                print(f"There is no record found for number : {number}")
    except Exception as e:
        print(f"Something went wrong while deleting the contact : {e}")

def update(path,criteria,choice):
    try:
        with open(path,mode="r",newline="")as file:
            reader=csv.reader(file)
            header=next(reader)
            found=False
            data=[]
            temp=[]
            for row in reader:
                if row[choice]==criteria:
                    found=True
                    data=row
                else:
                    temp.append(row)
            if found:
                with open(path,mode="w",newline="") as f:
                    writer=csv.writer(f)
                    ch=int(input("What do you want to update?\n1 for update name\n2 for update number\n3 for update mail\n4 for update address\n"))
                    if ch==1:
                        newname=str(input("Enter the new name : ")).lower()
                        data[0]=newname
                        temp.append(data)
                        writer.writerow(header)
                        writer.writerows(temp)
                        print("Data updated sucessfully")
                    elif ch==2:
                        newnumber=input("Enter the new phone number : ").strip()
                        data[1]=newnumber
                        temp.append(data)
                        writer.writerow(header)
                        writer.writerows(temp)
                        print("Data updated sucessfully")
                    elif ch==3:
                        newmail=str(input("Enter the new email : ")).lower()
                        data[2]=newmail
                        temp.append(data)
                        writer.writerow(header)
                        writer.writerows(temp)
                        print("Data updated sucessfully")
                    elif ch==4:
                        newadd=str(input("Enter the new address : ")).lower()
                        data[3]=newadd
                        temp.append(data)
                        writer.writerow(header)
                        writer.writerows(temp)
                        print("Data updated sucessfully")
                    else:
                        print("Invalid Choice ! choose a valid option")
    except Exception as e:
        print(f"something went wrong while updating the data : {e}")

def updateSupport(path):
    try:
        choice=int(input("press 1 for search by name\npress 2 for search by phone number\npress 3 for search by email\n"))
        if choice==1:
            name=str(input("Enter the name of the contact : ")).lower()
            update(path,name,choice-1)
        elif choice==2:
            number=input("Enter the phone number of the contact : ").strip()
            update(path,number,choice-1)
        elif choice==3:
            mail=str(input("Enter the email of the contact : ")).lower()
            update(path,mail,choice-1)
        else:
            print("Invalid input ! Choose a valid option")
    except Exception as e:
        print(f"Something went wrong while updating the contact : {e}")

def main():
    path=os.path.join(os.path.dirname(__file__),"contacts.csv")
    trigger=True
    while trigger:
        try:
            print("====================================================================================================")
            choice=int(input("What do you want to do ?\n1 for see all contacts\n2 for search any contact\n3 for add a new contact\n4 for update any contact\n5 for delete any contact\n6 for exit"))
            print("====================================================================================================")
            if choice==1:
                allContacts(path)
            elif choice==2:
                searchSupport(path)
            elif choice==3:
                addNewContact(path)
            elif choice==4:
                updateSupport(path)
            elif choice==5:
                deleteContact(path)
            elif choice==6:
                trigger=False
            else:
                print("Invalid input ! Choose a valid option")
        except Exception as e:
            print(f"You entered something wrong : {e}")

if __name__=="__main__":
    main()
