dict={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

def phone_num(n,index=0,o=None,val=""):
    global dict
    if o==None:
        o=[]

    if index==len(n):
        return o.append(val)

    if int(n[index]) not in dict.keys():
        return ("wrong")
    
    key=int(n[index])
    str=dict[key]

    for i in range (0,len(str)):
        phone_num(n,index+1,o,val+str[i])
    
    return o
    
n=input("Enter the key: ")
print(phone_num(n))