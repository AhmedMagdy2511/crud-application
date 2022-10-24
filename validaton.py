import re
def string_cheack(message):
    str=input(message)
    if str.isdigit() or not str:
        print("invalid text")
        return string_cheack(message)
    else:
        return str
def int_cheack(message):
    num=input(message)
    if num.isalpha() or not num:
        print("invalid number")
        return string_cheack(message)

    else:
        return num
def email_validation(message):
        email=input(message)
        reg="^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*$"
        if re.search(reg,email):
            return email
        else:
            print("invalid email")
            return input(message)
def password_validation(message):
    password=input(message)
    if not password:
        print("invalid password")
        return password_validation(message)
    else:
        return str(password)

def date_cheack(message):
    date=input(message)
    dreg="[0-9]{2}-[0-1]{1}[0-9]{1}-[0-9]{4}"
    if re.search(dreg,date) and date:
        return date
    else:
        print("wrong date formation dd-mm-yyyy")
        return date_cheack(message)