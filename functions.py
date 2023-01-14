def get_todos():
    with open("files/todos.txt", "r") as localFile:
        todos_local = localFile.readlines()
        return todos_local
