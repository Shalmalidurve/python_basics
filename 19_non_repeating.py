def non_repeating(string):
    seen={}
    found=False
    for char in string:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1

    for key,value in seen.items():
        if value==1:
            print(key)
            found=True
            break
        else:
            found=False
    
    if not found:
        print("No unique character")
string=input("Enter text: ")
non_repeating(string)

    
