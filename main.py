import PySimpleGUI as sg

import processes

prompt = sg.Text("Enter a To-Do")
to_do = sg.InputText(key='todo')
add_button = sg.Button('ADD', tooltip='click to add a To-Do')
edit_button = sg.Button('EDIT', tooltip='click to edit a To-Do')
complete_button = sg.Button('COMPLETE', tooltip='click to mark a To-Do as Complete')
close_button = sg.Button('CLOSE', tooltip='click to close app')
list_box = sg.Listbox(values=processes.get_todos(), key='todos',
                      enable_events=True, size=[40, 10])

layout = [[prompt],
          [to_do, add_button],
          [list_box, edit_button, complete_button],
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
            todos = processes.get_todos()
            new_todo = value['todo'] + '\n'
            todos.append(new_todo)
            processes.write_todos(todos)
            box['todos'].update(values=todos)
        case 'EDIT':
            todo_to_edit = value['todos'][0]
            new_todo = value['todo']
            todos = processes.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            processes.write_todos(todos)
            box['todos'].update(values=todos)
        case 'COMPLETE':
            todo_that_is_completed = value['todos'][0]
            todos = processes.get_todos()
            index = todos.index(todo_that_is_completed)
            todos.pop(index)
            processes.write_todos(todos)
            box['todos'].update(values=todos)
        case 'todos':
            box['todo'].update(value=value['todos'][0])
        case 'CLOSE':
            break
        case sg.WIN_CLOSED:
            break
box.close()
