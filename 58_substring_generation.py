def substring(string,left=0):
    if left==len(string):
        return
    
    for right in range (left+1,len(string)+1):
        print (f"{string[left:right]}")

    return substring(string,left+1)

s=input("Enter string: ")
substring(s)