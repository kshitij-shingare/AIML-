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

name = input("Enter the username : ")
pas = input("Enter the password : ")

if(name == username and pas == password):
    print("Login Successfully !")
elif(name != username):
    print("Incorrect username")
else:
    print("Incorrect Password")

# --------------------------------------- #

# EX -3

# n is multiple of m
n  = int(input("enter the n value : "))
m = int(input("enter the m value : "))

if(n % m == 0):
    print(n,"Is multiple Of ",m )
else:
    print(n,"is not multiple of ",m)

# --------------------------------------- #

# EX -4

# Print if Any Number is Odd or Even

oe = int(input("enter the m value : "))

if(oe % 2 == 0):
    print(oe,"is even" )
else:
    print(oe,"is odd")



# ----------------------------------------------------------------------------- #

# Nesting
username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("success")
else:
    if (username != "admin"):
        print("wrong username")
    else:
        print("wrong password") 


# -----------------------------------------------------------------------------


#Match Case - Alternative for if , elif , else

color = input("Enter color 1)red 2)yellow 3)Green")

match color:
    case "green":
        print("Go")
    case "red":
        print("stop bhaiya")
    case "yellow":
       print("stop") 
    case _:
        print("Wrong color")
# -----------------------------------------------------------------------------#

#Loops - used when we want to repeat or redundant the task

# 1)While Loops - while is basically is keyword repeat the work until condition is true
# counter - is used to count this name given by us (counter)

# Printing hi 5 times using loops
i = 1 #iterator 
while i<=5:
    i +=1
    print(i,"hi")
print("After loop count is : ",i)

# -------------------------#

#printing numbers 1 -5 

i =0 
while i<=4:
    i +=1
    print(i)

#  print 1 -5 in reverse

i =5
while i>=2:
     print(i)
     i -=1

# multiplication table of 6

i = 1

while i<=10:
    print(i*6)
    i+=1

# -----------------------------------------------------------------------------#

# Break & Continue
# break - terminate loop - end a loop
i = 1

while i<=10:
    print(i)
    i+=1
    if(i % 6 ==0):
        break

# continue - skip current iteration

i = 1

while i<=10:
    
    if(i % 3 == 0):
        i+=1
        continue
    print(i)
    i+=1

# -----------------------------------------------------------------------------#

# For Loops - use For Sequential Traversal
# sysntax - for _ in ___ (start,stop,step)
# counting numbers pf i's

# counting i's
word = "artificial intelligence"
count = 0
for ch in word:
    if(ch == 'i'):
        count +=1
print("count of i = ", count)

# counting vowels 

word = 'artificial'
count = 0
for vw in word:
    if(vw == 'a' or vw == 'e' or vw == 'i' or vw == 'o' ):
        count +=1

print("vowels are", count)


# Range Function - sequence generate

#sum of n natural numbers 

n = int(input("enter the vlaie"))
sum = 0
for i in range(1,n+1):
    sum+=i
print(sum)


# ---------------------------------------------------------------#

# Functions - block of codes used to perform specific task
# specific task - 1)func definision - where logic written 
                # func call - invoke (to call the func)
# non-default
def sumg(a,b):
    sum = a+b
    print(sum)

sumg(5,10)

# non default

def sumg(a,b=5):
    sum = a+b
    print(sum)

sumg(5)


# fucntion examples -
def avg():
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    c=int(input("enter the third number"))
    av = a+b+c/3
    return av

print(avg())


# Types of Functions - 1)builtin func 2)userdefined func
# 1)builtin - ex - print(),input(),etc...
# 2)userdefined - created by user like sum(),avg(),etc...

# ---------------------------------------------------------------#

# lambda functions
# not used for complex works used for simple works
# used in high order functions - func whoch are take parameter function values or
# return values that are func

sum = lambda a,b: (a+b)/2
print(sum(4,5))


# WAF to print factorial of 'n'

