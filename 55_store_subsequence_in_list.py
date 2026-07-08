list=[]
def subsequences(i_str,o_str=""):
    if len(i_str)==0:
        list.append(o_str)
        return

    subsequences(i_str[1:],o_str)  #NOT INCLUDED

    subsequences(i_str[1:],o_str+i_str[0]) #INCLUDED

    return list

s=input("Enter string: ")
print(subsequences(s))