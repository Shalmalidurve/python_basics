def max(arr,index=0):
    if len(arr)<=1 or index == len(arr)-1:
        return arr[index]
    
    m=max(arr,index+1)

    if arr[index]>m:
        return arr[index]
    
    return m

arr=[int(x) for x in input("Enter list: ").split()]
print(max(arr))