'''
list =[ 10,20,30,40,50] #reverse the list
list.reverse()
print(list)


num =[10,20,30,40,50] 
n=num[::-1]
print(n)
'''

#TO CHCECK IF A GIVEN LIST IS SORTED

num = [int(x) for x in input("Enter numbers: ").split()]

is_ascending = True
is_descending = True

for i in range(len(num) - 1):
    
    if num[i] > num[i + 1]:
        is_ascending = False
    
   
    if num[i] < num[i + 1]:
        is_descending = False
        
   
    if not is_ascending and not is_descending:
        break

if is_ascending and is_descending:
    print("Sorted (All elements are identical)")
elif is_ascending:
    print("Sorted in Ascending order")
elif is_descending:
    print("Sorted in Descending order")
else:
    print("Not sorted")
