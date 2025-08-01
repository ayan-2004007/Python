# Make a password length checker 
# check if password has :
# Minimum 8 characters and 
# one uppercase, one lowercase and one special character

password=str(input("Enter your password : "))
lowerlist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upperlist=[]
speciallist=["!","@","#","$","%","&","-","_","^","?"]
for char in lowerlist:
    upperlist.append(char.upper())
ltrigger,utrigger,strigger=False,False,False

if len(password)>=8:
    for i in lowerlist:
        for j in password:
            if i==j:
                ltrigger=True
                break

    for i in upperlist:
        for j in password:
            if i==j:
                utrigger=True
                break
    
    for i in speciallist:
        for j in password:
            if i==j:
                strigger=True
                break

else:
    print("Ops ! Your password must be length of 8")

if ltrigger and utrigger and strigger:
    print("Very good , your password is very strong")
else:
    print("Sorry , Your password is not strong enough ! Password must contain uppercase, lowercase and special characters")