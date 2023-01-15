def get_todos():
    with open("files/todos.txt", "r") as localFile:
        todos_local = localFile.readlines()
        return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
