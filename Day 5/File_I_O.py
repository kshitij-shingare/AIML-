#file IO means files Input and Output
#How to Open FIle 
#operations - read , write ,append
#delete file 


# File Operations
#Open,read & close

 #f = open("data.txt","r") return file object - storing file object in the f

# the "r" after the text file name is Called as mode 
#  there are multiple mode such as read , open , write etc...
# the most basic operation we do is read "r"

f = open("data.txt","r")
data = f.readline() #use to read the file line by line means pointer by pointer
print(type(data))
print(data)
f.close()
 # always close file after using it because its necceessary for the 
# unusual actions.

# data = f.readline()  use to read the line
#writing the file 
f = open("data.txt","w")
f.write("123")
f.close()

#with keyword 
#we use the with keyword to open the file
#when we open the file using with keyword it automatically close the file

with open("data.txt","w") as f:
    f.write("123")

#modes in file handling
# "r" - read (default - if not write any mode it automatically takes read mode) 
# "w" - write,truncate file first (clear file)
# "x" - create a file,return error if file already exist,open for writing (used rarely)
# "a" - append means writes at end (pointer at the end)
# "r+" - read and write (pointer at starting)
# "w+" - write and read (clear file first,pointer at starting)
# "a+" - append and read (pointer at end)
# "b" - binary mode (used for images, audio, video files)
# "t" - text mode (default)

#delete file (use os module) 
import os
os.remove("data.txt")

#exception handling in file handling 
# try and except 
# try - block of code which may cause an error
# except - block of code which is executed if an error occurs
# finally - block of code which is executed whether an error occurs or not 
# else - block of code which is executed if no error occurs

try:
    f = open("data.txt","r")
    data = f.readline()
    print(data)
    f.close()
except:
    print("file not found") 

# json module 
# JSON - JavaScript Object Notation
import json 
# 
dict = {
    "name" : "Kshitij",
    "age" : 21,
    "city" : "Mumbai"
}
#dump - write dict into json file
with open("data.json","w") as f:
    json.dump(dict,f)

# load - convert json to dict and read json file 
#dumps - convert dict to json string 
#
with open("data.json","r") as f:
    data = json.load(f)
    print(data) 