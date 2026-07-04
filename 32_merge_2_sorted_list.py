def merge_two_sorted_list_fast(l1, l2):
    merged = []
    i = 0  # Pointer for l1
    j = 0  # Pointer for l2

    # Compare elements from both lists side-by-side
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    # If there are any leftover numbers in l1 or l2, dump them at the end
    merged.extend(l1[i:])
    merged.extend(l2[j:])

    return merged

l1 = [int(x) for x in input("Enter list 1: ").split()]
l2 = [int(x) for x in input("Enter list 2: ").split()]
print(merge_two_sorted_list_fast(l1, l2))
