# Build a Student record management system (using csv file)
# Features :
#     Store student data in a csv file
#     Add new stduent record 
#     Search by roll
#     View all students
#     delete any student by roll


# Student record file (.csv) structure

# Roll no | First Name | Last Name | Class | Full Name | Bengali | English | Math | COMS | Physics | Chemistry | Total Marks



import os
import csv

def allStudents(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            if reader:
                for row in reader:
                    print(f"{row[0]} | {row[4]} | {row[3]} | {row[11]}")
            else:
                print("There is no student record in the file")
    except Exception as e:
        print(f"Error while fetching data from the file : {e}")

def addNewStudent(path):
    try:
        with open(path,mode="a",newline="") as file:
            writer=csv.writer(file)
            roll=int(input("Enter the new student roll : "))
            fname=str(input("Enter the First name : "))
            lname=str(input("Enter the Last name : "))
            fullname=fname+" "+lname
            cls=int(input("Enter the class : "))
            ben=int(input("Enter the marks of Bengali : "))
            eng=int(input("Enter the marks of English : "))
            math=int(input("Enter the marks of Mathematics : "))
            coms=int(input("Enter the marks of Computer Science : "))
            phy=int(input("Enter the marks of Physics : "))
            chem=int(input("Enter the marks of Chemistry : "))
            total=ben+eng+math+coms+phy+chem
            writer.writerow([roll,fname,lname,cls,fullname,ben,eng,math,coms,phy,chem,total])
            print("New student record added successfully")

    except Exception as e:
        print(f"Error occured while adding new student record : {e}")


def deleteStudent(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            temp=[]
            found=False
            roll=int(input("Enter the roll of the student : "))
            for row in reader:
                if int(row[0])==roll:
                    found=True
                else:
                    temp.append(row)
            if found:
                with open(path,mode="w",newline="") as f:
                    writer=csv.writer(f)
                    writer.writerows(temp)
                    print(f"Roll no : {roll} is deleted successfully")
            else:
                print(f"There is no record for roll : {roll}")
    except Exception as e:
        print(f"Error occured while removing student record : {e}")


def findStudent(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            found=False
            roll=int(input("Enter the roll of the student : "))
            for row in reader:
                if int(row[0])==roll:
                    found=True
                    print(f"The student found :\nRoll :{row[0]}\nName : {row[4]}\nClass : {row[3]}\nBengali : {row[5]}\nEnglish : {row[6]}\nMaths : {row[7]}\nComputer Science : {row[8]}\nPhysics : {row[9]}\nChemistry : {row[10]}\nTotal Marks : {row[11]}")
                    return
            if not found:
                print(f"There is no record of student roll no : {roll}")
    except Exception as e:
        print(f"Error occcured while seraching the student ; {e}")

def main():
    path=os.path.join(os.path.dirname(__file__),"data.csv")
    trigger=True
    while trigger:
        try:
            print("--------------------------------------------------------")
            choice=int(input("What do you want to do ?\n1 for show all students record\n2 for add a new student record\n3 for search any student record\n4 for delete any student record\n5 for exit\n"))
            print("--------------------------------------------------------")
            if choice==1:
                allStudents(path)
            elif choice==2:
                addNewStudent(path)
            elif choice==3:
                findStudent(path)
            elif choice==4:
                deleteStudent(path)
            elif choice==5:
                trigger=False
            else:
                print("Invalid input ! You entered wrong input")
        except Exception as e:
            print(f"you have entered something wrong : {e}")


if __name__=="__main__":
    main()