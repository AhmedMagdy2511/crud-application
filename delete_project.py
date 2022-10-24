from list_project import list_project_details,read_data
from validaton import int_cheack

def deleting(new_data):
    try:
        file = open("projects.txt", "w")
    except Exception as e:
        print(e)
        return False
    else:
        file.writelines(new_data)
        file.close()
        return True

def project_cheack_index(id):
    projects = read_data()
    for project in projects:
        project_details = project.split(":")
        if project_details[0] == id:
            # print(user_details[0])
            # print(f"found{id}")
            project_index=projects.index(project)
            return project_index
    else:
        print("/_!_\  wrong id")
        return


def delete_project(id):

    project_cheack_index(id)
    project_index=project_cheack_index(id)
    projects = read_data()
    del projects[project_index]
    cheack= deleting(projects)
    return cheack


def delete_handeler():
    list_project_details()
    id = int_cheack("Enter the id you want to delete")

    cheack = delete_project(id)
    if cheack:
        print("----------------Project deleted successfully----------------------")
    else:
        print("something went wrong")
