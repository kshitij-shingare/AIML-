# ------------------------------------------------------#
# Strings
word = "python"
cj ='a' #for single character
word2 = "Hi"
print(len(word))

# concatinate
print(word,"",word2)
# printing indexes
print(word[2])

# Strings Are Immutable in Python

# Slicing String

# slicing - parting a string
# syntax - str[start : end]
str = "python"

a= str[0:3] # slicing and storing in another variable
print (a) 
# Negative Index - a normal string starts from 0 to n-1 and negative index of normal string
#                   is -1 to -n+1


# String Formatting
#   when we are going to create a dynamic string(var & vals)

# 1) format () function - introduced in python3 - use placeholders and placement values

a = 5
b = 10
sum = a+b
# normal formatting
print("language is {}".format("python"))
print("sum is {}".format(sum))

# index based formatting
print("sum of {1} & is {0} id {2}".format(a,b,sum))

# values based formatting
print("values of vard{a} & {b}".format(a=5, b=10))



# 2)f- strings

#  literal string interpolation - embedd in the string'
#  f"{we can write here expression or variables etc}""

a =5
b =10

print(f"sum of {a} and {b} is {a + b}")
# ------------------------------------------------------#

#  Lists - mutable sequence of values
marks = [99,89,100,65,92,"KBS"]
print(marks[1])
print(len(marks))
#  strings are immutable in python but lists are mutable in python
marks[2] =18
print(marks)

# slicing in lists
# when we do slicing in python we create a substring of it

print(marks[0:4])
print(marks[0:len(marks)])

# Lists Methods
#  l.append(val) - add one lement 
