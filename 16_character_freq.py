def count_char(string):
    freq={}                     #CREATING DICTIONARY
    for char in string:
        if char in freq:
            freq[char]+=1   
        else:
            freq[char]=1
    print(freq)
        
string=input("Enter string: ")
count_char(string)