def substring(string,target):
    num=len(target)
    word=[]
    for i in range (len(string)+num-1):
        
        word.append(string[i:i+num])
    
    freq={}
    for x in word:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1

    
    for key,values in freq.items():
        if key==target:
            print(values)
            break

string=input("Enter text: ")
target=input("Enter target: ")
substring(string,target)