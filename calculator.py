# Build a simple calculator

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1//n2

trigger=1
while trigger==1:
    num1=int(input("\nEnter the first number : "))
    num2=int(input("Enter the second number : "))
    op=int(input("What do you want to do ??\n"
    "1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division\n5 for exit\n"))
    if op==1:
        print(f"Your result is : {add(num1,num2)}")
    elif op==2:
        print(f"Your result is : {sub(num1,num2)}")
    elif op==3:
        print(f"Your result is : {mult(num1,num2)}")
    elif op==4:
        print(f"Your result is : {div(num1,num2)}")
    elif op==5:
        trigger=0
    else:
        print("Invalid input")