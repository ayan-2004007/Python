# Build a simple billing system 
# Features :
#     User selects items from a product list (with price)
#     all the product data must be fetched from a file txt or csv
#     Calculates total bill and generates receipt
#     show the receipt in the terminal 
#     Save bill in file
#     Discounts and taxes


# product data structure 
# serial no | Product name | company | category | price |  warranty

# Billing data structure
# Bill no | Customer name | date | product name | price
import csv
import os
import datetime 
import random
customer={
        "name":"",
        "billno":"",
        "products":[],
        "date":"",
        "total":0
    }

def generateRandomBillno():
    return "b2025-"+str(random.randrange(100,1000))

def allProducts(productPath):
    try:
        with open(productPath,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            print(f"{'Serial No':<15} {'Product Name':<30} {'Company':<15} {'Category':<15} {'Price Rs':<12} {'Warranty':<8}")
            print("=======================================================================================================")
            for row in reader:
                print(f"{row[0]:<15} {row[1]:<30} {row[2]:<15} {row[3]:<15} Rs.{row[4]:<11} {row[5]:<6}")
    except Exception as e:
        print(f"Something went wrong while fetching the product data : {e}")

def search(productPath,category):
    try:
        with open(productPath,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            newData=[]
            for row in reader:
                if str(row[3])==category:
                    newData.append(row)
            if len(newData)>0:
                print(f"{'Serial No':<15} {'Product Name':<30} {'Company':<15} {'Category':<15} {'Price Rs':<12} {'Warranty':<8}")
                print("=======================================================================================================")
                for row in newData:
                    print(f"{row[0]:<15} {row[1]:<30} {row[2]:<15} {row[3]:<15} Rs.{row[4]:<11} {row[5]:<6}")
                return
            else:
                print(f"There is no products available of {category}")
                return
    except Exception as e:
        print(f"Somethign went wrong while searching the data : {e}")

def showAllCategories(productPath):
    try:
        with open(productPath,mode="r",newline="") as file:
            reader=csv.reader(file)
            next(reader)
            allcat=[]
            for row in reader:
                allcat.append(str(row[3]).upper())
            cats=set(allcat)
            print("All the categories : ")
            for cat in cats:
                print(cat)
    except Exception as e:
        print(f"Something went wrong while fetching the categories : {e}")


def buyProducts(productPath,billPath):
    try:
        with open(productPath,mode="r",newline="") as file:
            reader=csv.reader(file)
            trigger=True
            next(reader)
            while trigger:
                product=str(input("Enter the product name ( if you dont remember the product name then enter 1 to show the products name by categories and press 0 to finish purchesing): ")).lower()
                if product=="1":
                    cat=str(input("Enter the product category : ")).lower()
                    search(productPath,cat)
                    continue
                if product=="0":
                    trigger=False
                    print("Thanks for choosing our store ")
                    generateBill()
                    saveBill(billPath)
                else:
                    found=False
                    file.seek(0)
                    reader=csv.reader(file)
                    next(reader)
                    for row in reader:
                        if str(row[1])==product:
                            customer["products"].append(row)
                            print("Product purchesed succesfully")
                            customer["total"]+=int(row[4])
                            found=True
                            break
                    if not found:
                        print(f"There is no product named {product}")
    except Exception as e:
        print(f"Something went wrong while purchesing the products : {e}")


def generateBill():
    os.system("cls" if os.name=='nt' else "clear")
    print("=================================================================================")
    print("\t\tAYAN PC BUILDER")
    print("\t\tContact : 7439537213")
    print("=================================================================================")
    print(f"Customer name : {customer['name']}")
    customer["date"]=datetime.date.today()
    customer["billno"]=generateRandomBillno()
    print(f"Date : {customer['date']}")
    print(f"Bill no : {customer['billno']}")
    print("---------------------------------------------------------------------------------")
    print(f"{'Serial no : ':<15} {'Product Name : ':<30} {'Company : ':<15} {'Price(rs) : ':<12}")
    print("---------------------------------------------------------------------------------")
    for product in customer["products"]:
        print(f"{product[0]:<15} {product[1]:<30} {product[2]:<12} {product[4]:<12}")
    print("---------------------------------------------------------------------------------")
    print(f"{'Total Price : ':<30} {'₹'}{customer['total']}")
    discount=(customer['total']*10)//100
    print(f"{'Discount (10%) : ':<30} {'-₹'}{discount}")
    print("---------------------------------------------------------------------------------")
    print(f"{'Grand Total : ':<30} {'₹'}{customer['total']-discount}")
    print("=================================================================================")
    print("\t\tThank You For Shopping With Us !")
    print("=================================================================================")


def saveBill(billPath):
    try:
        with open(billPath,mode="a",newline="") as file:
            writer=csv.writer(file)
            if len(customer["products"])>0:
                for i in range(len(customer["products"])):
                    writer.writerow([customer["billno"],customer["name"],customer["date"],customer["products"][i][0],customer["products"][i][1],customer["products"][i][4]])
            
            exit(0)
    except Exception as e:
        print(f"Error occured while saving the bill : {e}")

def main():
    productPath=os.path.join(os.path.dirname(__file__),"products.csv")
    billPath=os.path.join(os.path.dirname(__file__),"bill.csv")
    name=str(input("Enter your name customer : ")).title()
    customer["name"]=name
    trigger=True 
    while trigger:
        try:
            print("--------------------------------------------------------")
            choice=int(input("What do you want to do ?\n1 for show all products\n2 for search products by categories\n3 for show all categories\n4 for buy products\n5 for exit\n"))
            if choice==1:
                allProducts(productPath)
            elif choice==2:
                category=str(input("Enter the category : "))
                search(productPath,category)
            elif choice==3:
                showAllCategories(productPath)
            elif choice==4:
                buyProducts(productPath,billPath)
            elif choice==5:
                trigger=False
            else:
                print("Invalid input !")
        except Exception as e:
            print(f"you have entered something wrong : {e}")


if __name__=="__main__":
    main()