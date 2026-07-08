list=[int(x) for x in input("Enter a sorted list: ").split()]
def binary_search(list,target,low=0,high=None):
    if high==None:
        high=len(list) -1

    if low>high:
        return ("Not Found")
    
    b = (low+high)//2

    if list[b]==target:
        return b
    
    elif list[b]<target:
        return (binary_search(list,target,low=b+1,high=high))
    
    elif list[b]>target:
        return (binary_search(list,target,low=low,high=b-1))
    
target=int(input("Target: "))
print(binary_search(list,target))