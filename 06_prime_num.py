N =int(input("Enter the value of N: "))

print("The prime numbers from 1 to N are: ")

if (N>=2):
    print("2")
    
m = ""
for i in range(3,N+1):
    if (i%2!=0):
        m=i
        for j in range (3,i):
            if (i%j==0):
                m=""
        if m == i:
            print (m)
    else:
        pass

