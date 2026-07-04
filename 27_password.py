FORBIDDEN=['password','1234','admin']                  
def password(my_password):                         #sum,enumerate,bool
    print("Dangerous Passwords to Avoid:")
    
    for i,word in enumerate(FORBIDDEN,start=1):
        print(f"Rank {i}: {word}")


    allowed=my_password not in FORBIDDEN 
    necessary=sum(letter.isalpha() for letter in my_password)>=3 and sum(letter.isdigit() for letter in my_password)>=2

    if allowed and necessary:
        return "Password Secured"
    else:
        return "This password is forbidden."
    

my_password=input("Enter your password: ")
print(password(my_password))