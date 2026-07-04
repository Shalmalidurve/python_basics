def Two_sum(list,target):
    for i in range (len(list)):
        for j in range (i,(len(list))):
            if list[i]+list[j]==target:
                return f"{i},{j}"
            
    return "Not found"

list=[int(x) for x in input("Enter the list of numbers: ").split()]
target=int(input("Enter target: "))

print(Two_sum(list,target))