def exist(arr,target,index=0,output=None):
   
    if output==None:
        output=[]

    if len(arr)==0 or index==len(arr):
        if sum(output)==target:
            return sum(output)==target
        return False
    
    output.append(arr[index])
    if exist(arr,target,index+1,output):
        return True
    output.pop()
    if exist(arr,target,index+1,output):
        return True
    return False

arr=[int(x) for x in input("Enter numbers: ").split()]
target=int(input("Enter target: "))
print (exist(arr,target))