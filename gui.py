import functions
import PySimpleGUI as sg

label = sg.Text('Enter To-Do')
input_box = sg.InputText(tooltip='Enter a To-Do',
                         key='todo')
button = sg.Button('Add')
listBox = sg.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=[43, 10])
editButton = sg.Button('Edit')
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, button], [listBox, editButton]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case('Add'):
            todos = functions.get_todos()
            newTodo = values['todo'] + "\n"
            todos.append(newTodo)
            functions.write_todos("files/todos.txt", todos)
            window['todos'].update(values=todos)

        case('Edit'):
            todoEdit = values['todos'][0]
            newTodo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todoEdit)
            todos[index] = newTodo
            functions.write_todos("files/todos.txt", todos)
            window['todos'].update(values=todos)

        case('todos'):
            window['todo'].update(value=values['todos'][0])


        case sg.WIN_CLOSED:
            break



window.close()
