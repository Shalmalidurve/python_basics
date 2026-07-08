def linear_search(list,target,index=0):
    if index>=len(list):
        return ("Not Found")

    if list[index]==target:
        return index

    return (linear_search(list,target,index+1))

list=[int(x) for x in input("Enter list: ").split()]
target=int(input("Enter number: "))
print(linear_search(list,target))
