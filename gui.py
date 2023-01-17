import functions
import PySimpleGUI as sg
import  time

sg.theme('DarkTeal11')

clock = sg.Text('', key='clock')
label = sg.Text('Enter To-Do')
input_box = sg.InputText(tooltip='Enter a To-Do',
                         key='todo')
button = sg.Button('Add')
listBox = sg.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=[43, 10])
editButton = sg.Button('Edit')
complteButton = sg.Button('Complete')
exitButton = sg.Button('Exit')
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, button],
                           [listBox, editButton, complteButton],
                           [exitButton]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%B-%d-%Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case('Add'):
            todos = functions.get_todos()
            newTodo = values['todo']
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

        case('Complete'):
            todoComplete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todoComplete)
            functions.write_todos("files/todos.txt", todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case('Exit'):
            break

        case('todos'):
            window['todo'].update(value=values['todos'][0])


        case sg.WIN_CLOSED:
            break



window.close()
