def reverse_word (string):
    
    list=[]
    for word in string:
        list.insert(0,word)

    reverse=" ".join(list)              #CONVERTS LIST INTO STRING
    return(reverse)

string=(str(x) for x in input("Enter string: ").split())
print(reverse_word(string))