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
data = f.read() #use to read the file line by line means pointer by pointer
print(type(data))
print(data)
f.close()
 # always close file after using it because its necceessary for the 
# unusual actions.

# data = f.readline()  use to read the line


