def compress_string(string):
    seen={}
    for char in string:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1

    for key,values in seen.items():
        print(key,values,sep="",end="")

string=input("Enter text: ")
compress_string(string)
