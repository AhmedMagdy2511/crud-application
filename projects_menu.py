from creat_project import project_info
from list_project import list_project_details
from delete_project import delete_handeler
from update_project import update_handeler
def project_handeler(user_name):
    while True:
        print(f"------------Welcome {user_name}--------------")
        print("choose from :""\n1- Create project""\n2- List Projects""\n3- Delete Project""\n4- Update Project""\n5- Exit")
        choice = int(input())
        if (choice == 1):
            project_info()
        elif choice == 2:
            list_project_details()
        elif choice == 3:
            delete_handeler()
        elif choice == 4:
            update_handeler()
        elif choice == 5:
            return
