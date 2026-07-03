def longest_word(string):
    list_str = string.split()
    max_length=0
    for word in list_str:
        if len(word)>max_length:
            max_length=len(word)
            longest_word=word
    return longest_word 
string=input("enter text: ")
print(longest_word(string))