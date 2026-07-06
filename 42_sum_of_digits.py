def sum(n):
    if n<10:
        return n
    
    m=n%10
    n=n//10

    return sum(n)+m

n=int(input("Enter the number: "))
print(sum(n))