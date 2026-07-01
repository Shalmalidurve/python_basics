def palindrome(n):
  

    original=n
    num = n
    i=0
    while n>0:
        b=n//10
        i=i+1
        n=b

    m=i-1
    rev_num=0
    while num>0:
        rev_num = ((10**m)*(num%10)+rev_num)
        num=num//10
        m=m-1

    if (original==rev_num):
        print("The number is palindrome")
    else:
        print("The number is not palindrome")
        
n=int(input('enter the number'))
palindrome(n)