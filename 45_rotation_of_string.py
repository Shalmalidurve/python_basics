#CHECK IF THE STRING IS THE ROTATION OF OTHER

def rotation (s1,s2):
    s3=""
    s4=""
    if len(s1)!=len(s2):
        return False
    
    for i2 in range (len(s2)):

        if s2[i2] not in s1:
            return False
        
        if s1[0] ==s2[i2]:
            s3=s2[i2:len(s2)]
            s4=s2[0:i2]
            if s3+s4==s1:
                print(s1,s2,s3,s4,s4+s3)
                return True
        
    return False

s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
print(rotation(s1,s2))
            
        


