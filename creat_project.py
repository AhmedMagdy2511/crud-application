from validaton import string_cheack,int_cheack,date_cheack
import time
def Register(*args):
    id=round(time.time())
    try:
        file=open("projects.txt","a")
    except Exception as e:
        print(e)
        return False
    else:
        data=(f"{id}:{args[0]}:{args[1]}:{args[2]}:{args[3]}:{args[4]}\n")
        file.write(data)
        file.close()
        return True

def project_info():
    print("--------create project----------")
    project_title = string_cheack("Enter project title")
    project_details = string_cheack("Enter project details")
    target = int_cheack("Total target of the project")
    start_date = date_cheack("Enter project start date dd-mm-yyyy")
    end_date = date_cheack("Enter project end date dd-mm-yyyy")

    if Register(project_title,project_details,target,start_date,end_date):
        print("--------project saved successfully----------")
    else:
        print("something went wrong")
