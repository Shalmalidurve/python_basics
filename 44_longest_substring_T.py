#LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
#SLIDING WINDOW
def longest_substring(string):
    left=0
    max_length=0
    seen=set()
    best_substrings=[]
    for right in range (len(string)):
        while string[right] in seen:
            seen.remove(string[left])
            left+=1

        seen.add(string[right])
        current_length=right-left+1

        if current_length > max_length:
            max_length=current_length
            best_substrings=[string[left:right+1]]

        elif current_length==max_length:
            if string[left:right+1]  not in best_substrings:
                best_substrings.append(string[left:right+1])
            
    return (best_substrings, max_length)
    
string=input("Enter string: ")
print(longest_substring(string))


