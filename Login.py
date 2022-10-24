#########################Authuntication Function#############################################33
from validaton import string_cheack,password_validation
from projects_menu import project_handeler
#Read the user data
def read_data():
    try:
        file = open("users.txt", "r")
    except Exception as e:
        print(e)
        return False
    else:
        all_users=file.readlines()
        file.close()
        return all_users

def user_name_cheack(user_name):
    users_data = read_data()
    for user in users_data:
        project_details = user.split(":")
        if project_details[1] == user_name:
            user_index=users_data.index(user)
            return user_index
    else:
        print("/_!_\  wrong user name")
        return

def split_projects():
    projects = read_data()
    projects_details = []
    for project in projects:
        projects_details.append(project.split(":"))
    return projects_details

def user_data(user_index):


    user = split_projects()
    user = user[user_index]

    return user

def Login_validation(user_name,password):
    user_index=user_name_cheack(user_name)
    user=user_data(user_index)

    if user[2].strip("\n") == password:

        print("---------------------------------------------")
        print(f"======{user[1]}======")
        print(f"user id : {user[0]}")
        print(f"user name : {user[1]}")
        print(f"user first name : {user[3]}")
        print(f"user last name : {user[4]}")
        print(f"user email : {user[5]}")
        return True

def Login():
    print("===============Login=================")
    user_name=string_cheack("Enter your user name")
    password=input("Enter your user password")
    if Login_validation(user_name,password):


        print(f"===============Successfully loged in as {user_name}===============")
        return project_handeler(user_name)
    else:
        print("Failed to login")
        return Login()
