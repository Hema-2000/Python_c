user_name= input("enter username")
pass_word=input("enter password")
if(user_name=="admin"):
    if pass_word=="username":
        print("login successfully")
    elif pass_word=="1234":
        print("suggest strong password")
    else:
        print("invalid password")
else:
    if user_name=="guest":
        if pass_word=="guest":
            print("login successfully")
        else:
            print("invalid password")
    else:
        print("invalid user_name")