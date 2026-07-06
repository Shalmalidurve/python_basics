def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    
    return fibonacci(n-1)+fibonacci(n-2)
    

n= int(input("enter: "))

def series(n):
    for i in range (0,n):
        print (fibonacci(i),end = " ")

series(n)
