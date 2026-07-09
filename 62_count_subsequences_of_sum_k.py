#Count subsequences whose sum equals K
i=0
def count(arr,target,index=0,output=None):
    global i
    if output==None:
        output=[]
    
    if len(arr)==0 or index==len(arr):

        if sum(output)==target:
            i+=1
            print(f"{output}")
        return

    output.append(arr[index])
    count(arr,target,index+1,output)
    output.pop()
    count(arr,target,index+1,output)

    return (f"The total number of subsequences with sum {target} are {i}")

arr=[int(x) for x in input("Enter numbers: ").split()]
target=int(input("Enter target: "))
print(count(arr,target))

#Time Complexity:n*(2**n)
#Space Complexity: n
#Recursive Relation: T(n)=2T(n-1)+O(1)