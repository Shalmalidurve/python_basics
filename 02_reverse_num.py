a = int(input("enter a number"))
num=a
i=0
while a>0:
    b=a//10
    i=i+1
    a=b

m = i-1
rev_num=0
while num>0:
    rev_num = int(((10**m)*(num%10))+rev_num)
    num=num//10
    m=m-1

print(rev_num)