# #Assignment Problems  
# Q1. Write a program that asks the user for their name and age, then prints a 
# sentence like:
    #Hello KBS, you are 19 years old!

name = (input("Enter Your Name "))
Age = int(input("Enter Your Age"))
print("Hello",name,",you are",Age,"years old!")


# Q2. Take two numbers as input from the user and print their sum, difference, 
# product, and quotient. 

a = int(input("Enter the 1st value"))
b = int(input("Enter the 2nt value"))
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#Q3. Ask the user to enter two integers and one float. Convert them all to floats 
#and print their average.

a = float(input("Enter the 1st value"))
b = float(input("Enter the 2nd value"))
c = float(input("Enter the 3rt value"))

print(a*b*c/3)

# Q4. The user enters a string containing a number (e.g., ). Convert it to: 
# •  an integer 
# •  a float 
# •  a string again 
# Print all three values with their types.

a =str(input("Enter the string containing the number"))
an_int = int(a)
a_float = float(a)
a_string = str(a)

print(an_int, type(an_int))
print(a_float, type(a_float))
print(a_string, type(a_string))



# Q5. Evaluate and print the result of the following expression:  
    # x = 10 + 3 * 2 ** 2 
# Based on what you learnt in the lecture explain why the output is what it is. 

x = 10 + 3 * 2 ** 2
print (x)  # the output will be 22


# Q6. Write a program to swap values of two numbers entered by the user.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before swapping:")
print(f"num1 = {num1}, num2 = {num2}")

# Method 1: Using a temporary variable
temp = num1
num1 = num2
num2 = temp

print("After swapping:")
print(f"num1 = {num1}, num2 = {num2}")


# Q7. Ask the user for a temperature in Celsius (string input). Convert it to , 
# then calculate and print temperature in Fahrenheit. 
# Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32

celsius_str = input("Enter temperature in Celsius: ")
celsius_temp = float(celsius_str)

fahrenheit_temp = (celsius_temp * (9/5)) + 32

print(f"Temperature in Celsius: {celsius_temp}°C")
print(f"Temperature in Fahrenheit: {fahrenheit_temp}°F")


# Q8. Take the radius (r) as user input and print the area. 
# Use the formula: Area = π * r2 (value of π = 3.14)

r = int(input("enter the radius"))
pi = 3.13
area = pi * r * r
print(area)

# Q9. Ask the user for:  Principal (P), Rate (R), Time (T). Convert all to and 
# compute simple interest: 
# SI = (P ∗ R ∗ T )/100

p = float(input("Enter the Principal value"))
r = float(input("Enter the Rate value"))
t = float(input("Enter the time value"))
si = (p * r * t)/ 100
print(si)

# Q10. Take a decimal number as input (like ) and output its: 
# •  integer part - 45
# •  fractional part - .78 
