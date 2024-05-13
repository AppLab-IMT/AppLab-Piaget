import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from CONSTANTS import PATH_IMAGES
from helpers import trata_imagem, render_imagem
from consultas import consulta_profile_e_senha
from db import db
from tela_inicial import tela_inicial
import os 
def consulta_usuario(email_institucional, input_password):
    consulta = f"""SELECT usuarios.id, usuarios.username, usuarios.email_institucional, usuarios.password, usuarios.role
                   FROM usuarios 
                   WHERE email_institucional = '{email_institucional}' AND password = '{input_password}'"""
    result = db(consulta)
    if result:
        id, username, email, passwordCorrect, role = result[0]  # Assuming result returns only one row
        if email_institucional == email and input_password == passwordCorrect:
            if role == "ESTUDANTES":
                print("BEM-VINDO ALUNO")
            elif role == "PROFESSORES":
                print("BEM-VINDO PROFESSOR")
            elif role == "ADMINISTRADORES":
                print("BEM-VINDO ADMINISTRADOR")
            else:
                messagebox.showinfo("Erro", "Papel do usuário desconhecido")
        else:
            messagebox.showinfo("Erro", "Email ou senha incorretos")
    else:
        messagebox.showinfo("Erro", "Email ou senha incorretos")

def click_inicio():
    consulta_usuario(input_email_institucional.get(), input_senha.get())

def tela_login(root):
    root.geometry("500x700")
    root.resizable(width=False, height=False)
    root.config(bg="#010F28")
    root.title("AppLab")
    
    label_title = tk.Label(root, text="AppLab", bg="#010F28", fg="ORANGE", font=("Poppins", 40))
    label_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    label_title_page = tk.Label(root, text="LOGIN", bg="#010F28", fg="WHITE", font=("Poppins", 50))
    label_title_page.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    
    label_email = tk.Label(root, text="Email institucional", bg="#010F28", fg="white", font=("Poppins", 22))
    label_email.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    global input_email_institucional
    input_email_institucional = tk.Entry(root)
    input_email_institucional.configure(bg="#FFFFFF", fg="BLACK", font=("Poppins", 22))
    input_email_institucional.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    label_senha = tk.Label(root, text="Senha", bg="#010F28", fg="white", font=("Poppins", 22))
    label_senha.place(relx=0.3, rely=0.61, anchor=tk.CENTER)
    
    global input_senha
    input_senha = tk.Entry(root)
    input_senha.configure(bg="#FFFFFF", fg="BLACK", font=("Poppins", 22), show="*")
    input_senha.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    btn_root_loguear = tk.Button(root, command=click_inicio)
    btn_root_loguear.configure(bg="#9AFF96", fg="BLACK", text="Entrar", font=("Poppins", 22))
    btn_root_loguear.place(relx=0.3, rely=0.8, anchor=tk.CENTER,  height=50, width=190)

    btn_root_matricula = tk.Button(root, command=lambda: tela_inicial(root))
    btn_root_matricula.configure(bg="#FFDDCE", fg="BLACK", text="Voltar", font=("Poppins", 22))
    btn_root_matricula.place(relx=0.72, rely=0.8, anchor=tk.CENTER,  height=50, width=190)


root = tk.Tk()
tela_login(root)
root.mainloop()
