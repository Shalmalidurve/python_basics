i=0
def subsequences(i_str,o_str=""):
    global i              
    #Integers in Python are immutable (unchangeable), you cannot modify an integer; you can only replace it with a new one.
    #As Python sees an = assignment inside a function, it automatically assumes you to create a new local variable named i.
    #Because it thinks it's a local variable, it tries to read the right side (i + 1) before that local variable has been created yet, 
    #causing the crash


    # In previous qs, we created list gloabally; in the function we just used"append"; we modified the list
    #and not completely change it, hence no need to specify there as "global list"


    if len(i_str)==0:
        i=i+1
        return

    subsequences(i_str[1:],o_str)
    subsequences(i_str[1:],o_str+i_str[0])

    return i

s=input("Enter string: ")
print(subsequences(s))