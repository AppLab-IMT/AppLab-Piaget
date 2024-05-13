import tkinter as tk
from PIL import Image, ImageTk
from consultas import consulta_profile_e_senha
from db import db
def trata_imagem(image_path, size_width, size_height):
    path = Image.open(f"{image_path}")
    tratada = path.resize((size_width, size_height))
    return tratada

def render_imagem(photoImg):
    return ImageTk.PhotoImage(photoImg)

def separa_tupla_em_lista(tupla):
    lista=[]
    for i in tupla:
        for el in i:
            lista.append(el)
    return lista

def logarse(email, senha):

   consulta = "SELECT id, username, role FROM usuarios WHERE email_institucional = '{email}' AND password = '{senha}'".format(email, senha)
   consulta_efetiva = db(consulta_profile_e_senha(email, senha))
   return consulta_efetiva