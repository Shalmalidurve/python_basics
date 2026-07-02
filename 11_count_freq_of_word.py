separate = [str(x) for x in input("Enter string: ").split()]
print(separate)
m=0
for i in range (len(separate)):
    repeated=False

    for j in range (0,i): #for execution at first index i.e. this loop is not executed as range(0,0)
        if separate[i]==separate[j]:
            repeated=True
            break

    if not repeated:    
        for j in range (len(separate)):
            if separate[i]==separate[j]:
                m=m+1
       
        print(separate[i],":",m)
        m=0

