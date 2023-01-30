import PySimpleGUI as sg

import processes

prompt = sg.Text("Enter a To-Do")
to_do = sg.InputText(key='todo')
add_button = sg.Button('ADD', tooltip='click to add a To-Do')
edit_button = sg.Button('EDIT', tooltip='click to edit a To-Do')
complete_button = sg.Button('COMPLETE', tooltip='click to mark a To-Do as Complete')
close_button = sg.Button('CLOSE', tooltip='click to close app')

layout = [[prompt],
          [to_do, add_button],
          [edit_button],
          [complete_button],
          [close_button]
          ]

box = sg.Window("TO-DO",
                layout,
                font=('Helvetica', 15)
                )
while True:
    event, value = box.read()
    print(event)
    print(value)
    match event:
        case 'ADD':
            todos=processes.get_todos()
            new_todo=value['todo']
            todos.append(new_todo)
            processes.write_todos(todos)
        case 'EDIT':
            pass
        case 'COMPLETE':
            pass
        case 'CLOSE':
            break
        case sg.WIN_CLOSED:
            break
box.close()
