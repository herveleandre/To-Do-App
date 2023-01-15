import functions
import PySimpleGUI as sg

label = sg.Text('Enter To-Do')
input_box = sg.InputText(tooltip='Enter a To-Do')
button = sg.Button('Add')

window = sg.Window('My To-Do App', layout=[[label], [input_box, button]])
window.read()
window.close()
