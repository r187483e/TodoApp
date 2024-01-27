import PySimpleGUI as sg
from zip_extractorfile import extract_archive

sg.theme("Black")
label1 = sg.Text("select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("choose",key="archive")

label2 = sg.Text("select dest dir:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("choose",key="folder")

compress_button = sg.Button("Extract")
output_label =sg.Text(key="output",text_color="green")


window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button,output_label]])

while True:

    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath,dest_dir)
    window["output"].update(value="Extraction completed!")




window.close()