def second_largest(n):
    n=set(n)
    n=list(n)
    for pass_num in range (len(n)):
        for i in range (len(n)-1):
            if n[i]>n[i+1]:
             n[i],n[i+1]=n[i+1],n[i]
    
    
    print(n[-2])

n=[int(x) for x in input("Enter a list of numbers: ").split()]
second_largest(n)