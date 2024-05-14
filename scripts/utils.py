import tkinter as tk
from PIL import Image, ImageTk
import os 

## Utils 4 images
def path_4_imagem(end_path):
    return os.path.join(os.path.dirname(__file__),  "assets", "/images/", end_path)

def trata_imagem(image_path, size_width, size_height):
    path = Image.open(f"{image_path}")
    tratada = path.resize((size_width, size_height))
    return tratada

def render_imagem(img_tratada):
    return ImageTk.PhotoImage(img_tratada)

def separa_tupla_em_lista(tupla):
    lista=[]
    for i in tupla:
        for el in i:
            lista.append(el)
    return lista

def check_role_by_email(email):
    decode_role = email[-6:-3]
    if decode_role == "g12":
        estudantes = "A"
        return estudantes
    elif decode_role == "com":
        administradores = "B"
        return administradores
    elif decode_role == "pro":
        professores = "C"
        return professores
    else:
        return "E-MAIL INVALIDO"


    