dict_map={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
def phone_num(n,index=0,o=None,val=""):
    global dict_map

    if o==None:
        o=[]

    if index==len(n):
        o.append(val)
        return 

    if int(n[index]) not in dict_map.keys():
        return ("wrong")
    
    key=int(n[index])
    char=dict_map[key]

    for i in range (0,len(char)):
        print(f"{i},{o}")
        phone_num(n,index+1,o,val+char[i])
    
    return o
    
n=input("Enter the key: ")
print(phone_num(n))