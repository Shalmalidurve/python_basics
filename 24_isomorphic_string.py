def isomorphic(s1,s2):
    d1={}
    d2={}
    status=True
    if len(s1)==len(s2):       
        for char1,char2 in zip(s1,s2):  #WE USE ZIP TO LOOP TO THROUGH 2 STRINGS AT ONCE.
        
            if char1 in d1 and d1[char1]!=char2:
                status=False
                print("not")
                break
            if char2 in d2 and d2[char2]!=char1:
                status=False 
                print("not")
                break

            d1[char1]=char2
            d2[char2]=char1
    if status:
        print("isomorphic")

s1=input("Enter text 1: ")
s2=input("Enter text 2: ")

isomorphic(s1,s2)
    
