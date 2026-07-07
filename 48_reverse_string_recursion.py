def reverse_string(string):
    if len(string)<=1:
        return string
    return (string[-1]+reverse_string(string[0:len(string)-1]))

string=input("Enter string: ")
print(reverse_string(string))