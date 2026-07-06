def sorted(n,index=0):
    if len(n)==0 or index+1==len(n):
        return True
    
    if n[index]<n[index+1]:
        n.pop(0)
    else:
        return False
    
    
    return sorted(n,index=0)

n=[int(x) for x in input("Enter list: ").split()]
print(sorted(n))