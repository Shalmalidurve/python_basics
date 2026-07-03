def most_freq_char(string):
    seen={}
    for char in string:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1
    
    num=seen.values()
    maximum=max(num)

    for key,values in seen.items():
        while values==maximum:
            print(key)
            break

string=input("Enter text: ")
most_freq_char(string)