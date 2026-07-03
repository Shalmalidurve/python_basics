def anagram(string1,string2):
    str1=string1.lower()
    str2=string2.lower()
    
    if sorted(str1)==sorted(str2):
        print("ANAGRAM")

    else:
        print("Not anagram")

string1= input("Enter text 1: ")
string2= input("Enter text 2: ")
anagram(string1,string2)