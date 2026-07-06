def power(x,n):
    if n==0:
        return 1
    
    return (x*(power(x,(n-1))))
    
x=int(input("Enter base: "))
n=int(input("Enter index: "))
print(power(x,n))
