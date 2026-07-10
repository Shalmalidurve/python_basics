def sum(arr,target):
    output=[]
    arr.sort()
    def backtrack(target,index,path):
    
        if target==0:
            output.append(list(path))
            return 
        
        for i in range(index,len(arr)):

            if arr[i]>target:
                break

            path.append(arr[i])
            backtrack(target-arr[i],index+1,path)
            path.pop()
           
    backtrack(target,0,[])
    return output

arr=[int(x) for x in input("Enter numbers: ").split()]
target=int(input("Enter number: "))
print(sum(arr,target))