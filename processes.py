FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """read text file and returns list of data"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(value, filepath=FILEPATH):
    """write the value(to-do) into text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(value)
