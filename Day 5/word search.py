data=True
with open("sample.txt","r") as f:
    while data:
        data = f.readline()
        if("Python"  in data):
            print(f"found in line {data}")
            print(data.count("Python"))
            break
            
        print(data)
