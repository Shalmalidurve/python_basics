def reverse(num):
    if num<10:
        return num
    
    x=num
    i=0
    while x>=10:                #power = len(str(num)) - 1
        x=x//10
        i+=1
    m=num%10
    
    return ((m*(10**i))+(reverse(num//10)))

num=int(input("Enter number: "))
print(reverse(num))