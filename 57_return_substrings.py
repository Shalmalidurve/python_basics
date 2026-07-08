str=""
is_first_run = True

def subsequence(i_s,o_s=""):
    global str,is_first_run
    if len(i_s) == 0:
        if is_first_run:
            str = o_s
            is_first_run = False  
        else:
            str=str+","+o_s
        return
    
    subsequence(i_s[1:],o_s)
    subsequence(i_s[1:],o_s + i_s[0])

    return str

string=input("Enter string: ")
print(subsequence(string))