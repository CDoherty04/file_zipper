import PySimpleGUI as SimpGUI
from zipper import make_archive

# Front-end
c_label = SimpGUI.Text("Select files to compress: ", background_color="white", text_color="black")
c_input = SimpGUI.Input()
c_button = SimpGUI.FilesBrowse("Choose", key="files")

d_label = SimpGUI.Text("Select destination folder: ", background_color="white", text_color="black")
d_input = SimpGUI.Input()
d_button = SimpGUI.FolderBrowse("Choose", key="folder")

run_button = SimpGUI.Button("Compress")
output_label = SimpGUI.Text(key="output", text_color="green", background_color="white")

window = SimpGUI.Window("File Zipper", background_color="white", layout=[[c_label, c_input, c_button],
                                                                         [d_label, d_input, d_button],
                                                                         [run_button, output_label]])

# Back-end
while True:
    event, values = window.read()

    if event == SimpGUI.WIN_CLOSED:
        break
    elif event == "Compress":
        filepaths = values[0].split(";")
        folder = values[1]
        make_archive(filepaths, folder)
        window["output"].update("Compression successful!")

window.close()
