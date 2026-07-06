def product(n):
    if n<10:
        return n
    
    m=n%10
    n=n//10
    return product(n)*m

n=int(input("Number: "))
print(product(n))