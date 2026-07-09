#Print subsequence
'''
def subsequence(string,o_str=""):
    if len(string)==0:
        print (f"{o_str}")
        return

    subsequence(string[1:],o_str+string[0])
    subsequence(string[1:],o_str)

s=input("Enter string: ")
subsequence(s)
'''


#Print all subsequences whose sum equals K:
def subseq_sum(arr,target,output=None):
    sum=0
    if output==None:
        output=[]
    if len(arr)==0:
        for i in range (0,len(output)):
            sum+=output[i]
    
        if sum==target:
            print (f"{output}")

        return
    
    
    output.append(arr[0])
    subseq_sum(arr[1:],target,output)
    output.pop()
    subseq_sum(arr[1:],target,output)

arr=[int(x) for x in input("Enter numbers: ").split()]
target=int(input("Enter number: "))
subseq_sum(arr,target)