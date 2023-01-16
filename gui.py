import functions
import PySimpleGUI as sg

label = sg.Text('Enter To-Do')
input_box = sg.InputText(tooltip='Enter a To-Do', key='todo')
button = sg.Button('Add')

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, button]],
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
        case sg.WIN_CLOSED:
            break



window.close()
