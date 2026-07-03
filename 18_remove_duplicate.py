def remove_duplicate(string):
    is_repeated=False
    seen = set()
    for char in string:
        if char not in seen:
            seen.add(char)
            is_repeated=False
        else:
            is_repeated=True

        if not is_repeated:
            print(char , end="")

string=input("Enter text: ")
remove_duplicate(string)

'''
string=input("Enter text: ")
STRING=set(string)  #REMOVED DUPLICATES BUT ORDER IS NOT PRESERVED
print(STRING)
'''