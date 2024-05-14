import tkinter as tk
from tkinter import messagebox
from utils import separa_tupla_em_lista, trata_imagem, render_imagem
from consultas import search_user_by_email_institucional, search_user_data_by_email
from hash_manager import rainbow
from t03 import t03

def check_credentials(email_institucional, password, root):
    user_tupla = search_user_by_email_institucional(email_institucional)
    if user_tupla:
        user_lista = separa_tupla_em_lista(user_tupla)
        hashP = user_lista[0]
        emailP = email_institucional
        digestHashP = rainbow(hashP, password)
        if digestHashP:
            consulta2 = search_user_data_by_email(emailP)
            lista_consulta = separa_tupla_em_lista(consulta2)
            render_t03(root, lista_consulta)
        else:
            messagebox.showerror("Erro", "Email ou senha inválidos")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado")

def switch_to_home(root):
    root.destroy()  # Destruir a janela principal
    import t01
    t01.t01()

def render_t03( user_data):
    tk.Tk().destroy()  # Oculta a janela principal
    t03( user_data)

def t02():
    BLUE_BG = "#00102A"

    root = tk.Tk()
    root.geometry("500x700")
    root.configure(bg=BLUE_BG)
    root.title(f"Bem-Vindo ao LOGIN")
    root.resizable(width=False, height=False)

    PATH2 = "assets/images/logoText.png"

    img2 = trata_imagem(PATH2, 350, 100)
    r2 = render_imagem(img2)

    lr2 = tk.Label(root, image=r2)
    lr2.config(bg=BLUE_BG)
    lr2.place(relx=0.18, rely=0.1)

    label_email_institucional = tk.Label(root)
    label_email_institucional.configure(bg=BLUE_BG, fg="WHITE", text="Email institucional", font=("Poppins", 22))
    label_email_institucional.place(relx=0.5, rely=0.3, anchor=tk.CENTER, height=50)

    entry_email_institucional = tk.Entry(root)
    entry_email_institucional.configure(bg="WHITE", fg="BLACK", font=("Poppins", 22))
    entry_email_institucional.place(relx=0.5, rely=0.40, anchor=tk.CENTER, height=50)

    label_senha = tk.Label(root)
    label_senha.configure(bg=BLUE_BG, fg="WHITE", text="Senha", font=("Poppins", 22))
    label_senha.place(relx=0.5, rely=0.50, anchor=tk.CENTER, height=50)

    entry_senha = tk.Entry(root)
    entry_senha.configure(bg="WHITE", fg="BLACK", font=("Poppins", 22))
    entry_senha.place(relx=0.5, rely=0.60, anchor=tk.CENTER, height=50)

    btn_root_loguear = tk.Button(root, command=lambda: check_credentials(entry_email_institucional.get(), entry_senha.get(), root))
    btn_root_loguear.configure(bg="#9AFF96", fg="BLACK", text="Entrar", font=("Poppins", 22))
    btn_root_loguear.place(relx=0.3, rely=0.8, anchor=tk.CENTER, height=50, width=190)
    
    btn_root_cadastro = tk.Button(root, text="Voltar", command=lambda: switch_to_home(root))
    btn_root_cadastro.configure(bg="#FFDDCE", fg="BLACK", font=("Poppins", 22))
    btn_root_cadastro.place(relx=0.72, rely=0.8, anchor=tk.CENTER, height=50, width=190)

    root.mainloop()
