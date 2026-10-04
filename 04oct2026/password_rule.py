password=input("enter the password:")
if len(password)>=8 and "@" in password:
    print("valid password")
else:
    print("invalid password")    