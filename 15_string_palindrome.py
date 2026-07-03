text = input("Enter text")
reversed=""
for char in text:
    reversed = char + reversed

if text==reversed:
    print("TEXT IS PALINDROME")

else:
    print("NOT PALINDROME")