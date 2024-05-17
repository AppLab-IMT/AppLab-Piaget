import tkinter as tk
from tkinter import ttk 
from db import db
from utils import render_imagem, trata_imagem, check_role_by_email  
from validators import validate_input_email

def t04():
    BLUE_BG = "#00102A"
    root = tk.Tk()
    root.geometry("500x700")
    root.title("Cadastrar na AppLab")
    root.resizable(False, False)
    root.config(bg=BLUE_BG)
    
    # set background image
    PATH1 = "assets/images/bg01.png"
    img1 = trata_imagem(PATH1, 500, 700)
    r1 = render_imagem(img1)
    lr1 = tk.Label(root, image=r1)
    lr1.place(x=0, y=0)
    lr1.config(bg=BLUE_BG)

    label_title_page = tk.Label(root, text="CADASTRA na AppLAB!")
    label_title_page.configure(bg=BLUE_BG, fg="ORANGE", font=("Poppins", 22))
    label_title_page.place(relx=0.5, rely=0.1, anchor=tk.CENTER, height=30)

    label_email_institucional = tk.Label(root, text="Email institucional")
    label_email_institucional.configure(bg=BLUE_BG, fg="WHITE", font=("Poppins", 22))
    label_email_institucional.place(relx=0.5, rely=0.2, anchor=tk.CENTER, height=30)
    
    entry_email_institucional = tk.Entry(root)
    entry_email_institucional.configure(bg="WHITE", fg="BLACK", font=("Poppins", 22))
    entry_email_institucional.place(relx=0.5, rely=0.25, anchor=tk.CENTER, height=30)
    
    label_password = tk.Label(root, text="Senha")
    label_password.configure(bg=BLUE_BG, fg="WHITE", font=("Poppins", 22))
    label_password.place(relx=0.5, rely=0.30, anchor=tk.CENTER, height=30)
    
    entry_password = tk.Entry(root, show="*")
    entry_password.configure(bg="WHITE", fg="BLACK", font=("Poppins", 22))
    entry_password.place(relx=0.5, rely=0.35, anchor=tk.CENTER, height=30)
    
    confirm_label_password = tk.Label(root, text="Confirmar Senha")
    confirm_label_password.configure(bg=BLUE_BG, fg="WHITE", font=("Poppins", 22))
    confirm_label_password.place(relx=0.5, rely=0.40, anchor=tk.CENTER, height=30)
    
    confirm_entry_password = tk.Entry(root, show="*")
    confirm_entry_password.configure(bg="WHITE", fg="BLACK", font=("Poppins", 22))   
    confirm_entry_password.place(relx=0.5, rely=0.45, anchor=tk.CENTER, height=30)
    
    # Marco pergunta
    marco_recovery_question = tk.LabelFrame(root, text="Recuperar Senha", font=("Comic Sans", 10, "bold"), pady=10)
    marco_recovery_question.config(bd=2, pady=5)
    marco_recovery_question.place(relx=0.5 ,rely=0.60, anchor=tk.CENTER)
        
    # Pergunta
    label_recovery_question = tk.Label(marco_recovery_question, text="Documento para recuperacao de conta", font=("Comic Sans", 10, "bold"))
    label_recovery_question.grid(row=0, column=0, sticky='e', padx=5, pady=8)
    recovery_question = ttk.Combobox(marco_recovery_question, values=["Registro Estudantil - RE", "Registro Professor - RP", "Registro Administrativo - RA"], width=30)
    recovery_question.current(0)
    recovery_question.grid(row=0, column=1, padx=5, pady=8)

    label_recovery_answer = tk.Label(marco_recovery_question, text="Resposta escolhida: ", font=("Comic Sans", 10, "bold"))


t04()
