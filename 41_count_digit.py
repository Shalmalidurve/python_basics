def count(n):
    if n<10:
        return 1
    n=n//10
    return count(n)+1

n=int(input("Enter an integer: "))
print(count(n))