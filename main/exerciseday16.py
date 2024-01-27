import PySimpleGUI as sg
from converters import convert


sg.theme("Black")
label1 = sg.Text("Enter feet")
input1 =sg.Input(key="feet")

label2 = sg.Text("Enter inches")
input2 =sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button =sg.Button("Exit")

window = sg.Window("Convertor",layout= [[label1,input1],
                                        [label2,input2],
                                        [convert_button,exit_button, output_label]])

while True:
    event,values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    inches = float(values['feet'])
    feet = float(values['inches'])

    result = convert(inches, feet)
    window['output'].update(value=f"{result}m", text_color="blue")



window.close()


