def count_zero(num):
         
    if num<10 and num>0:
        return 0
    if num==0:
        return 1
    i = count_zero(num//10)
    if num%10==0:
        i+=1
    return i
    
num=int(input("Enter number: "))
print(count_zero(abs(num)))  #negative to positive number
    