n = [str(x) for x in input("enter text: ").split()]
print(n)
for i in range (len(n)):
    word = str(n[i])
    word = word[::-1]
    print(word)

