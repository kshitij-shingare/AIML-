# printing Hello World
print("Hello World")

#Variables - Are use to store the data in the memory
A = 10
B = 20
name = "KBS"
Age = 35 
_PI = 3.14

print("My name is ",name,Age) #printing variables (note that when we are printing variables we are not going to use doublecoat "")
# the name which we have given to the value or any name which is given is called "Identifiers" and they are casesensitive.

#Rules of IDentifiers - 1) eng letters 2) NOt with digit 3)start with "_"

#-----------------------------------------------------------------------#

#Data Types

# 1) Integer 2)String 3)Float 4)Boolean 5)None

A = 10
Name = "Ram"
PI = 3.14

num = 2
isPrime = True


isWhole = None #used to not give any datatype
print(type(Name)) #use to print type of a variable
print(type(isPrime)) #printing the type of a varible (boolean)


#-----------------------------------------------------------------------#

#Keywords

#In python there are multiple reserved words which are not going to used to store or any operation Ex. False.....

#-----------------------------------------------------------------------#

#Comments - To Write Comments in Python We use "#" For single line, ''' this are the multiline comments '''

#-----------------------------------------------------------------------#

#Style_Guide - 
                # Snake_Case - tot_Price = 100 - in this we use the UnderScore And It is Recommend That to use the Snake_case
                # CamelCase - totPrice = 100 - First word of First Letter is Small and Others words first case is Capital
                # PascalCase - TotPrice = 100 - All words First Words Are Capital

                #Always prefer Snake Case Because in Existing Fuctions and other Features Snake_Case Are Used.
                #There is Googles Python Style GUide Do Checkout.

#-----------------------------------------------------------------------#

# Now Using OUr this Knowledge We Are going to Write 
    # WAP(Write A Program) to Calculate SUm of 2 Numbers

A = 10
B = 20
sum_AB = A + B
print(sum_AB)


#-----------------------------------------------------------------------#

#Operators 

    # Arithmetic - +, -, *, /, %, **
    # Relational / Comparison - >, >=, <, <=, ==, !=
    # Assignment - = , +=
    # Logical - not, and, or

# We Have Seen That sum = a + b The "+"" inside the ab are called a operators 
# and the ab are operants

# Arithmetic Operators - +, -, *, /, %, **
a = 10
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# Modulo Operator (%) Used To Calculate Remainder Means if a%b the remainder will the calculated
print(a%b) #Modulo

# To Calculate the Power Value we use "**" like a spuare
print(a**b)

# --------------------- #

# Relational / Comparison Operators - >, >=, <, <=, ==, !=

a = 10
b = 5

print(a > b) # The relational Operators Check the Relation/ Comparison Hence the print will be True/Flase.
# Same Like For All Operators


# --------------------- #

# Assignment Operators - = , +=

    # a = b we assign the a value to b but it is a simple way.
    # To write in a short way we write like this 
    # if 
a = 5
a = a + 1 # answer will 6 
a += 1 #its also will be 6 this is short form to write the operators for operation

print (a)

# --------------------- #

     #LOgical Operators - not, and, or
     # not - make true false and false true means Reverse the values
     #EX - 
var = False 
print(not var) # it will becom true
print(not (5>8)) # For the values

    # And - If the Both Values are T Then The Result Will Be T Otherwise It is False.
    #Ex - 
print((5>3) and (3>8)) #false 

    #OR - if both values are false then it is F Otherwise it is true

# There are much other like bitwise and membership operators.

#-----------------------------------------------------------------------#

    #Operator Precedence - Priority To which is Given 
            # IT is mainly used when there is messy operation or simple also
'''
            ()
    # Arithmetic - +, -, *, /, %, **
    # Relational / Comparison - >, >=, <, <=, ==, !=
    # Assignment - = , +=
    # Logical - not, and, or
            Not
            And 
            Or
'''

#-----------------------------------------------------------------------#

# Type Conversion - Converting one type of to another type and it is done only with compatible type of data
    # int --> Float (allow)
    # Float --> Int (Allow)
    # int --> bool (allow)

# There are 2 types 1) type conversion (implicit --> python) 2) Type Casting

ans1 = int(5 + 10.0) #casting
ans2  = 5 + 10.0 #conversion
print(ans1, type(ans1))
print(ans2, type(ans2))


#-----------------------------------------------------------------------#
# Taking Input From User
Username = input ("Enter Your Name:")
print("Welcome", Username)

    #Sum of 2 number
a = int(input ("enter value of a : "))
b = int (input ("enter the value of b :"))
sum = a + b #concatination
print(sum)



#-----------------------------------------------------------------------#

# Finishing The Day With All The learnings With A Program 
    # WAP to Print the average of 2 numbers

a = int(input("Enter the 1 number : "))
b = int(input("Enter the 2 number : "))
Average = a*b/2
print(Average)