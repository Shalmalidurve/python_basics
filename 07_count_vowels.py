def count_vowels(n):
    n=n.replace(" ","")
    if n.isalpha():
        n=n.lower()
        j=0
        for i in n:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                j=j+1
            else:
                pass
        print(f"The Numberofvowels are {j}" )
    else:
        print("Enter string input")

n=input("Enter string input: ")
count_vowels(n)