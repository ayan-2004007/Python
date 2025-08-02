# build a To-Do list application using file handling
# Features :
#     add , delete and view tasks
#     save and load tasks using file handling
#     Mark tasks as completed
#     show pending and completed tasks



import os

def addNewTask(path):
    try:
        with open(path,"a") as file:
            task=str(input("Enter your new task : ")).strip().lower()
            file.write("[x] "+task+"\n")
            print("New task added successfully")
    except Exception:
        print(f"Something went wrong while adding new task !")

def allTask(path):
    try:
        with open(path,"r") as file:
            data=file.read()
            print("Your tasks are : ")
            print(data)
    except Exception:
        print("Something went wrong while fetching data !")        

def removeTask(path):
    try:
        with open(path,"r") as file:
            data=file.readlines()
        deleteTask="[x] "+str(input("Enter the task you want to delete : "))
        found=False
        newdata=[]
        for task in data:
            if task.strip().lower()==deleteTask:
                found=True
            else:
                newdata.append(task)
        
        if found:
            with open(path,'w') as f:
                f.writelines(newdata)
            print(f"{deleteTask} deleted successfully ")
        else:
            print(f"{deleteTask} is not found in the file")
    except Exception as e:
        print(f"Something went wrong while removing task : {e}")


def showPending(path):
    try:
        with open(path,"r") as file:
            data=file.readlines()
        newdata=[]
        for line in data:
            if line.find("[x]")!=-1:
                newdata.append(line)
        if len(newdata)>0:
            print("The pending tasks are : ")
            for line in newdata:
                print(line)
        else:
            print("You dont have any pending task")
    except Exception as e:
        print(f"Something went wrong while fetching data : {e}")

def main():
    path=os.path.join(os.path.dirname(__file__),"data.txt")
    trigger=True
    while trigger:
        try:
            print("--------------------------------------------------------")
            choice=int(input("What do you want to do ?\n1 for show all tasks\n2 for add new tasks\n3 for remove tasks\n4 for show pending tasks\n"))
            print("--------------------------------------------------------")
            if choice==1:
                allTask(path)
            elif choice==2:
                addNewTask(path)
            elif choice==3:
                removeTask(path)
            elif choice==4:
                showPending(path)
            else:
                print("Invalid input ! You entered wrong input")
        except Exception as e:
            print(f"You entered something wrong \nYou must enter integer : {e}")

if __name__=="__main__":
    main()