from list_project import list_project_details, split_projects
from validaton import int_cheack,date_cheack,string_cheack
from delete_project import project_cheack_index


def data_write(new_data):
    try:
        file = open("projects.txt", "w")
    except Exception as e:
        print(e)
        return False
    else:
        for item in new_data:
            data = (f"{item[0]}:{item[1]}:{item[2]}:{item[3]}:{item[4]}:{item[5]}")
            file.writelines(data)
        file.close()
        return True


def update(list, type):
    type_dic = {
        "title": 1,
        "description": 2,
        "target": 3,
        "start": 4,
        "end": 5
    }
    index = type_dic.get(type)

    if type == "start" or type == "end":
        new_data=date_cheack("Enter new data")
    elif type == "target":
        new_data=int_cheack("Enter new data")
    else:
        new_data = string_cheack("Enter new data")
    print(f"old data is {list[index]}")
    list[index] = new_data
    print(f"new data is {list[index]}")
    return list


def update_list(list, id_index):
    oldtable = split_projects()
    oldtable[id_index] = list
    test = data_write(oldtable)
    return test


def select_update(list):
    print("""
    Enter waht you want to update
    1-Update Title
    2-Update description
    3-Update Target
    4-Update Start date
    5-Update End date
    6-Enter different id
    """)
    choice = int(int_cheack("choose number"))
    if choice in [1, 2, 3, 4, 5]:

        if choice == 1:
            type = "title"
            new_list = update(list, type)
            return new_list
        elif choice == 2:
            type = "description"
            new_list = update(list, type)
            return new_list
        elif choice == 3:
            type = "target"
            new_list = update(list, type)
            return new_list
        elif choice == 4:
            type = "start"
            new_list = update(list, type)
            return new_list
        elif choice == 5:
            type = "end"
            new_list = update(list, type)
            return new_list
        elif choice == 6:
            # return
            return update_handeler()
        else:
            exit()
    else:
        print("wrong choice")
        check = string_cheack("do you want to continue (y) or (n)")
        if check == "y":
            return select_update(list)
        elif check == "n":
            return
        else:
            exit(1)


def list_to_update(id_index):
    projects = split_projects()
    project = projects[id_index]
    print(f"--------Project {project[1]} selected------")
    return project


def update_handeler():
    list_project_details()
    id = int_cheack("Enter the id you want to update")

    id_index = project_cheack_index(id)
    #if id_index:
    listToUpdate = list_to_update(id_index)
    updatedlist = select_update(listToUpdate)
    newlist = update_list(updatedlist, id_index)
    if newlist:
        print("----------------Project Updated successfully----------------------")
    return
    # else:
    #     print("something went wrong")
