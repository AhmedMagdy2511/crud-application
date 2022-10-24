import Registeration as R,Login as L
choice=""
while choice != 3:
    print("choose from :""\n1- LogIN""\n2- Register")
    choice=int(input())
    if (choice == 1):
        L.Login()
    elif choice == 2:
        R.user_info()