username = input("Enter u username: ")

username.find(" ")

if len(username) >  12:
    print("U username high 12 charters")
elif not username.find(" ") == -1:
    print("u username cant contain spaces")
elif not username.isalpha():
    print("u username cant contain numbers")
else:
    print(f"welcome {username}")
