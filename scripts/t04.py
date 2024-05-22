import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from uuid import uuid4  # Importe ttk para usar o Combobox
import sqlite3
import os

from hash_manager import hasheando
from utils import render_imagem, trata_imagem, check_role_by_email  
from validators import validate_input_email

def switch_to_slash(root):
    root.destroy()
    from t01 import t01
    t01()
    
    
def t04():
    BLUE_BG = "#00102A"
    root = tk.Tk()
    root.geometry("500x700")
    root.title("Cadastrar na AppLab")
    root.resizable(False, False)
    root.configure(bg=BLUE_BG)
    
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
    label_recovery_answer.grid(row=1, column=0, sticky='e', padx=5, pady=8)
    recovery_answer = tk.Entry(marco_recovery_question, width=33)
    recovery_answer.grid(row=1, column=1, padx=5, pady=8)        
    
    label_advice = tk.Label(marco_recovery_question, text="*A resposta inserida será sua chave de recuperação!", font=("Comic Sans", 9, "bold"), foreground="blue")
    label_advice.grid(row=2, column=0, columnspan=2, sticky='e', padx=5, pady=8)
    
    btn_submit = tk.Button(root, text="Voltar", command=lambda:switch_to_slash(root))
    btn_submit.configure(bg="#FFF496", fg="BLACK", font=("Poppins", 22))
    btn_submit.place(relx=0.3, rely=0.80, anchor=tk.CENTER, height=50, width=190)
    
    btn_voltar = tk.Button(root, text="Cadastrar" , command=lambda:transaction1(entry_email_institucional.get(), confirm_entry_password.get(), recovery_question.get(),  recovery_answer.get() ))
    btn_voltar.configure(bg="#9AFF96", fg="BLACK", font=("Poppins", 22))
    btn_voltar.place(relx=0.7, rely=0.80, anchor=tk.CENTER, height=50, width=190)
        
    root.mainloop()
   

def transaction1(email_institucional, password, recovery_question, recovery_answer):
    role = "ESTUDANTES"
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
    usuario_id = str(uuid4())
    usuario_id_estudante = str(uuid4())

    # Separar o nome do email institucional
    separa_email = email_institucional.split("@")
    email_fullname = separa_email[0]
    username = email_fullname.replace(".", "-")
    hash_email = separa_email[1]
    
    if hash_email == "jpiaget.g12.br":

    # Conectar-se ao banco de dados e executar a transação
        # Conectar-se ao banco de dados e executar a transação
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            try:
                # Iniciar a transação
                conn.execute("BEGIN TRANSACTION")

                # Inserir dados na tabela Usuarios
                query_usuarios = '''
                    INSERT INTO Usuarios (id, email_institucional, username, password, recovery_question, recovery_answer, role)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                '''
                parameters_usuarios = (usuario_id, email_institucional, username, hasheando(password), recovery_question, recovery_answer, role)
                cursor.execute(query_usuarios, parameters_usuarios)

                # Inserir dados na tabela usuario_estudante
                query_usuario_estudante = '''
                    INSERT INTO usuario_estudante (id, is_active, usuario_id)
                    VALUES (?, ?, ?)
                '''
                parameters_usuario_estudante = (usuario_id_estudante, 1, usuario_id)
                cursor.execute(query_usuario_estudante, parameters_usuario_estudante)

                # Inserir dados na tabela score_total
                query_score_total = '''
                    INSERT INTO score_total (id, total_score, usuario_id_estudante)
                    VALUES (?, ?, ?)
                '''
                parameters_score_total = (str(uuid4()), 0, usuario_id_estudante)
                cursor.execute(query_score_total, parameters_score_total)

                # Confirmar a transação
                conn.commit()
            except sqlite3.Error as e:
                # Em caso de erro, reverter a transação
                conn.rollback()
                print(f"An error occurred: {e}")
                return None

        return messagebox.showinfo("Sucesso", "Usuario criado com sucesso \n Volte a tela principal e click em login para ingressar em sistema!")
    else:
        return messagebox.showerror("Erro", "Email do ALUNO inválido \n O email de alunos segue o padrão \n primeiroNome.ultimoSobrenome@jpiaget.g12.br")