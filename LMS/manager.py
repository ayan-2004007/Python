# Build a Library book management system
# Features :
#     Add new book
#     search any book
#     Borrow or rerturn books
#     Store inventory in a file


# Book data structure
# Book Id | Book Title | Author | Availability

import os
import csv

def allBooks(path):
    try:
        with open(path,mode="r",newline="")as file:
            reader=csv.reader(file)
            next(reader)
            print(f"{'ID':<10} {'TITLE':<40} {'AUTHOR':<30} {'AVAILABILITY':<10}")
            print("-"*100)
            for row in reader:
                print(f"{row[0]:<10} {row[1]:<40} {row[2]:<30} {row[3]:<10}")
    except Exception as e:
        print(f"Something went wrong while fetching data : {e}")

def addNewBook(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            found=False
            id=str(input("Enter the ID of the new book : ")).lower().strip()
            title=str(input("Enter the name of the new book : ")).lower().strip()
            author=str(input("Enter the name of the Author : ")).lower().strip()
            availability=str(input("Enter the availability : ")).lower().strip()
            next(reader)
            for row in reader:
                if str(row[0])==id:
                    found=True
                    break
            if found:
                print(f"There is already a record for book ID : {id}")
            else:
                with open(path,mode="a",newline="") as f:
                    writer=csv.writer(f)
                    writer.writerow([id,title,author,availability])
                    print("New book added successfully")
    except Exception as e:
        print(f"Something went wrong while adding a new book : {e}")

def search(path,criteria,choice):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            searchData=[]
            print(f"{'ID':<10} {'TITLE':<40} {'AUTHOR':<30} {'AVAILABILITY':<10}")
            print("-"*100)
            for row in reader:
                if str(row[choice])==criteria:
                    searchData.append(row)
            if len(searchData)>0:
                for data in searchData:
                    print(f"{data[0]:<10} {data[1]:<40} {data[2]:<30} {data[3]:<10}")
            else:
                print(f"There is no book record for {criteria} ")
    except Exception as e:
        print(f"Something went wrong while searching : {e}")

def searchSupport(path):
    choice=int(input("1 for search by ID\n2 for search by Book name\n3 for search by Author name\n"))
    if choice==1:
        id=str(input("Enter the ID to search : ")).lower().strip()
        search(path,id,choice-1)
    elif choice==2:
        title=str(input("Enter the Name to search : ")).lower().strip()
        search(path,title,choice-1)
    elif choice==3:
        name=str(input("Enter the Author name to search : ")).lower().strip()
        search(path,name,choice-1)
    else:
        print("Invalid input ! Choose a valid option")

def borrowBook(path):
    try:
        with open(path,mode="r",newline="") as file:
            reader=csv.reader(file)
            title=str(input("Enter the title of the book : "))
            header=next(reader)
            wholeData=[]
            bookData=[]
            found=False
            for row in reader:
                if str(row[1])==title:
                    bookData=row
                    found=True
                else:
                    wholeData.append(row)
            if found and bookData[3]=="yes":
                with open(path,mode="w",newline="") as f:
                    writer=csv.writer(f)
                    bookData[3]="no"
                    wholeData.append(bookData)
                    writer.writerow(header)
                    writer.writerows(wholeData)
                    print(f"{bookData[1]} Book borrowed successfully")
            else:
                print(f"Sorry ! either the book is not found or the book is already borrowed")
    except Exception as e:
        print(f"Something went wrong while borrowing book : {e}")

def returnBook(path):
    try:
        with open(path,mode="r",newline="")as file:
            reader=csv.reader(file)
            title=str(input("Enter the title of the book : "))
            header=next(reader)
            wholeData=[]
            bookData=[]
            found=False
            for row in reader:
                if str(row[1])==title:
                    bookData=row
                    found=True
                else:
                    wholeData.append(row)
            if found and bookData[3]=="no":
                with open(path,mode="w",newline="")as f:
                    writer=csv.writer(f)
                    bookData[3]="yes"
                    wholeData.append(bookData)
                    writer.writerow(header)
                    writer.writerows(wholeData)
                    print(f"{bookData[1]} Book returned successfully")
            else:
                print(f"Sorry ! either the book is not found or the book is already returned")
    except Exception as e:
        print(f"Something went wrong while returning book : {e}")


def main():
    path=os.path.join(os.path.dirname(__file__),"books.csv")
    trigger=True
    while trigger:
        try:
            print("="*100)
            ch=int(input("What do you want to do?\npress 1 for see all books\npress 2 for add new book\npress 3 for search book\npress 4 for borrow book\npress 5 for return book\npress 6 for exit\n"))
            print("="*100)
            if ch==1:
                allBooks(path)
            elif ch==2:
                addNewBook(path)
            elif ch==3:
                searchSupport(path)
            elif ch==4:
                borrowBook(path)
            elif ch==5:
                returnBook(path)
            elif ch==6:
                trigger=False
            else:
                print("Invalid input ! Choose a valid option")
        except Exception as e:
            print(f"You entered something wrong : {e}")

if __name__=="__main__":
    main()