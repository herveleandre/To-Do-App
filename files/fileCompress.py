import functions
import PySimpleGUI as sg


label1 = sg.Text('Choose File')
input_box1 = sg.Input()
button1 = sg.FileBrowse('Choose')

label2 = sg.Text('Choose Destination')
input_box2 = sg.Input()
button2 = sg.FolderBrowse('Choose')

compressButton = sg.Button('Compress')

window = sg.Window('Files Compressor', layout=[[label1, input_box1, button1],
                                               [label2, input_box2, button2],
                                               [compressButton]])
window.read()
window.close()
