def read_data():
    try:
        file = open("projects.txt", "r")
    except Exception as e:
        print(e)
        return False
    else:
        all_projects=file.readlines()
        file.close()
        return all_projects

def split_projects():
    projects = read_data()
    projects_details=[]
    for project in projects:
        projects_details.append(project.split(":"))
    return projects_details
def list_project_details():
    projects=split_projects()
    for project in projects:
            print("---------------------------------------------")
            print(f"======{project[1]}======")
            print(f"project id : {project[0]}")
            print(f"project title : {project[1]}")
            print(f"project description : {project[2]}")
            print(f"project target : {project[3]}")
            print(f"project start date : {project[4]}")
            print(f"project end date : {project[5]}")



