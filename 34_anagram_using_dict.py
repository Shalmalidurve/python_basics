def anagram (s1,s2):
    dict={}
    for ch in s1:
        if ch in dict:
            dict[ch]+=1
        else:
            dict[ch]=1

    for char in s2:
        if char in dict:
            dict[char]-=1
        else:
            dict[char]=-1

    for val in dict.values():
        if val!=0:
            return False

    else:
        return True
    
s1=input("STRING 1: ")
s2=input("String 2: ")
print(anagram(s1,s2))

