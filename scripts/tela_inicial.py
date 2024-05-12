import tkinter as tk
from PIL import Image, ImageTk

from CONSTANTS import PATH_IMAGES
from helpers import trata_imagem, render_imagem
from clickRouter import rootLogin, rootMatricula

def tela_inicial():
    root = tk.Tk()
    root.geometry("500x700")
    root.resizable(width=False, height=False)
    root.config(bg="orange")
    root.title("AppLab")
    PATH_BG = f"{PATH_IMAGES}bg01.png"
    PATH_WELCOME = f"{PATH_IMAGES}img01_welcome.png"
    PATH_CHARACTERS = f"{PATH_IMAGES}logo.png"
    # Carrega a imagem de fundo e redimensiona
    img01 = render_imagem(trata_imagem(PATH_BG, 500, 700))
    img02 = render_imagem(trata_imagem(PATH_WELCOME, 294, 112))
    img03 = render_imagem(trata_imagem(PATH_CHARACTERS, 300, 300))


    # Labels para bg, boas-vindas e personagems
    label_background = tk.Label(root, image=img01)
    label_background.place(x=0, y=0, relwidth=1, relheight=1)

    label_welcome = tk.Label(root, image=img02, bg="#010F28")
    label_welcome.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    label_characters = tk.Label(root, image=img03, bg="#010F28")
    label_characters.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    btn_root_login = tk.Button(command=rootLogin)
    btn_root_login.configure(bg="#9AFF96", fg="BLACK", text="Login", font=("Poppins", 22))
    btn_root_login.place(relx=0.3, rely=0.8, anchor=tk.CENTER,  height=50, width=190)

    btn_root_matricula = tk.Button(command=rootMatricula)
    btn_root_matricula.configure(bg="#CEFFFC", fg="BLACK", text="Matricula", font=("Poppins", 22))
    btn_root_matricula.place(relx=0.72, rely=0.8, anchor=tk.CENTER,  height=50, width=190)

    root.mainloop()


tela_inicial()