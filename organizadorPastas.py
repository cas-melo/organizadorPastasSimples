import PySimpleGUI as sg
sg.theme('DarkGrey15')

layout = [
    [sg.Text("Insira o diretório da pasta:")],
    [sg.InputText(key="diretorio_pasta")],
    [sg.Button("Organizar pasta"), sg.Button("Cancelar")],
    [sg.Text("", key="texto_sucesso")]
]

# Cria a janela, (Título, valor do layout)
janela1 = sg.Window("Organizador de pastas", layout)

while True:
    evento, valores = janela1.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break

    elif evento == "Organizar pasta":
        import os
        import shutil

        path = valores['diretorio_pasta']
        files = os.listdir(path)

        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1: ]

            if os.path.exists(path+ '/' +extension):
                shutil.move(path+ '/'+file, path+'/'+extension+'/'+file)
            else:
                os.mkdir(path+'/'+extension)
                shutil.move(path+'/'+file, path+'/'+extension+'/'+file)


        janela1['texto_sucesso'].update("Pasta organizada com sucesso!")
        

janela1.close()
    



