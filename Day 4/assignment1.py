# word search 
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