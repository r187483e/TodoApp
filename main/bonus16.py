import PySimpleGUI as sg
from zipcreator import make_archive

label1 = sg.Text("select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("choose",key ="files")

label2 = sg.Text("select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("choose",key="folder")

compress_button = sg.Button("Compress")
output_label =sg.Text(key="output",text_color="green")


window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button,output_label]])
while True:
    event, values = window.read()
    print(event)
    print(values)
    filepath = values['files'].split(";")
    folder = values['folder']
    make_archive(filepath, folder)
    window["output"].update(value="compression completed")
    


window.close()
