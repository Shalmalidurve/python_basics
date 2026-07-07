def is_palindrome(string):
    s1=string[0:(len(string)//2)]
    s2=string[(len(string)-len(s1)):len(string)]
              
    if s1==s2[::-1]:
        return True
    return False

def longest_palindrome (string):
   
    max_length=0
    best_substring=[]
    for left in range(len(string)):
        for right in range (left+1,len(string)+1):
            
            current_slice=(string[left:right])
    
            if is_palindrome(current_slice):
                current_length=len(current_slice)
            
                if current_length>max_length:
                    max_length=current_length
                    best_substring=[current_slice]

                elif current_length==max_length and max_length>0:
                    if current_slice not in best_substring:
                        best_substring.append(current_slice)

    return (best_substring,max_length)

string=input("Enter string: ")
print(is_palindrome(string))
print(longest_palindrome(string))