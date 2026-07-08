def occurrence(string,target,index=0):

    if len(string)<=0 or index==len(string):
            return ""
    
    s=occurrence(string,target,index+1)
    if string[index]==target:
        return s
    else:
        return string[index]+s

string= input("Enter string: ")
target= input("Enter target: ")
print(occurrence(string,target))