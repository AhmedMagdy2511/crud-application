from validaton import string_cheack,email_validation,int_cheack,password_validation
import time
def Register(*args):
    id=round(time.time())
    try:
        file=open("users.txt","a")
    except Exception as e:
        print(e)
        return False
    else:
        data=(f"{id}:{args[3]}:{args[4]}:{args[0]}:{args[1]}:{args[2]}\n")
        file.write(data)
        file.close()


def password_confirm(password):
    confirm = input("Confirm Password")
    if confirm == password:
        return True
    else:
        print("Wrong password")
        return password_confirm(password)

def user_info():
    first_name = string_cheack("Enter Your first name")
    last_name = string_cheack("Enter your Last name")
    Email = email_validation("Enter email")
    User_name = string_cheack("Enter your user name")
    password = password_validation("Enter your password")
    if password_confirm(password):
        print("password confirmed")
    else:
        print("Wrong password")
        exit(0)
    user=Register(first_name,last_name,Email,User_name,password)
