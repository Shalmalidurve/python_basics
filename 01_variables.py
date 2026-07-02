''' QS 1
a=float(input("enter no: "))
b=float(input("enter another no: "))

sum=a+b
diff=a-b
product=a*b

if (b==0):
    print("division not possible")
     
elif (b!=0) :
    div = a/b
    floor_div =a//b
    mod =a%b
    print(f"\ndivsion={div}",f"Floor div= { floor_div}" ,f"Modulus = {mod}", sep='\n')

pow = a**b

print(f"SUM: {sum}",f"Diff: {diff}" ,f"Product: {product}" ,f"Power = {pow}",sep='\n')
'''

'''QS 2
temp = float(input("What is the temperature in degree celsius"))

f= ((temp * 9)/5)+32

print (f"The temperature in farhenite is {f} ")
'''

a=2
b=3

c=a
a=b
b=c

print(a,b)

a = "hii"
b = str(8)

a=[a,b]
 
b = a[0]
a=a[1]
print (a,b)
