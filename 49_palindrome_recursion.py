def palindrome(string):
    s=""
    if len(string)<2:
        return True
    if len(string)==2 or len(string)==3:
        if string[0]!=string[-1]:
            return False
        else:
            return True
    
    if len(string)>3:
        if string[0]==string[-1]:
            s=string[1:-1]                  # dont use pop function by converting into list...learn about that
            return palindrome(s)
        
    return False

string= input("Enter string: ")
print(palindrome(string))