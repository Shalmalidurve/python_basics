def merge_two_list(l1,l2):
    for num in range (len(l2)):
        l1.append(l2[num])
    for i in range (len(l1)-1):
        for n in range (len(l1)-1):
            if l1[n]>l1[n+1]:
                l1[n], l1[n+1] = l1[n+1],l1[n]
            else:
                pass
    return f"{l1}"

l1=[int(x) for x in input("Enter list 1: ").split()]
l2=[int(x) for x in input("Enter list 2: ").split()]

print(merge_two_list(l1,l2))


