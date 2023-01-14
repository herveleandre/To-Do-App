from functions import get_todos
import time

todos = []
title = "TODO-APP-PYTHON"
print(title)
todayDate = time.strftime("%B-%d-%Y ")
print(todayDate)
while True:
    user_input = (input('Please add, show, edit, complete, or exit '))
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todo = user_input[4:]
        todos = get_todos()

        todos.append(todo + "\n")

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_input.startswith("show"):

        todos = get_todos()

        # List Comprehension
        # newTodoList = [item.strip('\n') for item in todos]

        # newTodoList = []
        # for items in todos:
        #    items = items.strip('\n')
        #    newTodoList.append(items)

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item.capitalize()}")

    elif user_input.startswith("edit"):
        number = int(input("Please enter a number to edit: "))
        number = number - 1
        new_todo = input("Enter a new To DO: ") + "\n"
        editTodo = todos[number].strip("\n")
        print(f"{editTodo} has been replaced with {new_todo}")
        todos[number] = new_todo
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_input.startswith('complete'):
        completeNumber = int(input("Which number is completed: "))

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        index = completeNumber - 1
        removeTodo = todos[index].strip('\n')
        print(f"{removeTodo} has been completed and deleted")
        todos.pop(index)
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    else:
        print("Invalid Command")

        break

print("Thank You For Using The ToDOList APP")
