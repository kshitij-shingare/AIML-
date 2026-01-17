#  Topics - Conditional statements
    #loops 
    #Funcions

#Conditional Statements
    # if, elif, else

    #if - used to check condition is true then execute
    #elif - used when if stement is not true then we want to give another condition
    #else - used after the if when if is not true to execute any thing.


ip = input("Enter the color : ")

if(ip == "red"):
    print("Stopp ree !")
elif(ip == "yellow"):
    print("watch is someone coming !")
elif(ip == "Green" or ip == "green"):
    print("Gooooooooooooooo !")
else:
    print("Incorrect Input")
# --------------------------------------- #

# Ex -2 
age = int(input("Enter The Age : "))

if(age < 13 ):
    print("You are Child Unable To Vote")
elif(age < 18 ):
    print("You are Tennager Cant vote")
elif(age >=18):
    print("You are Eligible Brother")
else:
    print("Incorrect Input")

# --------------------------------------- #

# Ex-3

username = "admin"
password= "pass"

name = input("Enter the username")
pas = input("Enter the password")

if(name == username and pas == password):
    print("Login Successfully")
elif(name != username):
    print("Incorrect username")
else:
    print("Incorrect Password")
    