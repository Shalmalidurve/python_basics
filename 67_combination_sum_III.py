def com_sum(k,n):
    output=[]
    def backtrack(remaining_sum,path,index):
        if len(path)==k and remaining_sum==0:
            output.append(list(path))
            return 
        
        if len(path)>k:
            return
        
        for i in range(index,10):
            if i>remaining_sum :
                break
            path.append(i)
            backtrack(remaining_sum-i,path,i+1)
            path.pop()
                       
    backtrack(n,[],1)
    return output

k=int(input("Enter k: "))
n=int(input("Enter n: "))
print(com_sum(k,n))
