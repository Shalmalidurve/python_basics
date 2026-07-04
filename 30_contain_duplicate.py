def contain_duplicate(list):
    seen=set()
    for i in range (len(list)):
        if list[i] not in seen:
            seen.add(list[i])
        else:
            return True
        
    return False

list=[int(x) for x in input("Enter numbers: ").split()]
print(contain_duplicate(list))