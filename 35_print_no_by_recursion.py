def recursion(n):
    if n==1:
        print (1)
    else:
        print (n) 
        recursion(n-1)

def rec(n):
    if n==0:
        return
    
    rec(n-1)

    print(n)


n=int(input("Enter number: "))
recursion(n)
print("\n")
rec(n)
