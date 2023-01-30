import PySimpleGUI as sg

prompt = sg.Text("Enter a To-Do",text_color='black')
to_do = sg.InputText()
add_button = sg.Button('ADD', tooltip='click to add a To-Do')
edit_button = sg.Button('EDIT', tooltip='click to edit a To-Do')
complete_button = sg.Button('COMPLETE', tooltip='click to mark a To-Do as Complete')
close_button = sg.Button('CLOSE', tooltip='click to close app')

layout = [[prompt], [to_do, add_button], [edit_button], [complete_button], [close_button]]

box = sg.Window("TO-DO", layout)
box.read()
box.close()
