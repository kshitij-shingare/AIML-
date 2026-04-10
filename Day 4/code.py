# file i/o - read the data from file
# opening file 
# operations - read , write, append

#  file operations - open, read & close
#sample.txt is a file name and 'r' is mode r= read
f = open("sample.txt","r")
data = f.read()
print(data)

f.close()

# reading a line 
f = open("sample.txt","r")
data = f.readline()
print(data)

f.close()

# writing in files


# =============================================#

#  With Keyword - used for the file is open and work done
            #  it will automatically gets close.

with open("sample.txt","r") as f:
    data = f.read()
    print(data)
    print(len(data))




# =============================================#

# Modes - modes are used to open file

# r - reading [ deafault]

# w - writing, trucates files first  - override data



# X - #creates new & open for writing
    f = open("samplee.txt","x")

f.write("ayyyyyyyyyyyyyyyyyyyyyyyyyyy Bhai new file create krto")

f.close()



# a - #writing, appends at end

f = open("samplee.txt","a")

f.write("ayyyyyyyyyyyyyyyyyyyyyyyyyyy Bhai new text append krto")

f.close()



# b - #binary mode

# t - #text mode [default]

# + - #opens disk file for update(r & w)

# =============================================# 

# word search activity
data = True
line = 1
word = "python"
with open("asii.txt","r") as f:
    while data:
        data = f.readline()
        if(word in data):
            print(f"{word} found",{line})
            break
        
        print(data)
        line +=1



# =============================================# 

# Deleting the file

import os
os.remove("hi.txt")

# =============================================# 

# Exceptin handling - try,except,else,finally

try:
    x = int(input("Enter to divide by 10"))
    ans = 10/x

except ZeroDivisionError:
    print(f"Divide by 0 is not allowed")

else:
    print(ans)

finally:
    print("End of program")

# finally
    # some block of code which must be excute either it throw excpt
    # or not.

# =============================================# 

# List Comprehensions
# - [outfput for item in iterable if condition]
sq = [i*i for i in range(6)]
print(sq)



