def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

n=int(input("Enter the value of n: "))
print(sum(n))
print(fact(n))