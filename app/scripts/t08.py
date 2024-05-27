import tkinter as tk
from tkinter import messagebox, END, BOTH, YES
import os
import sqlite3
from utils import trata_imagem, render_imagem

def db(query, parameters=()):
    db_name = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
    # Conectar-se ao banco de dados e executar a consulta
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters).fetchall()  # Use fetchall() to retrieve all records
        conn.commit()
        return result

def consulta_ranking():
    consulta = """SELECT usuarios.email_institucional, usuarios.username, score_total.total_score
                  FROM usuarios
                  INNER JOIN usuario_estudante
                      ON usuario_estudante.usuario_id = usuarios.id
                  RIGHT JOIN score_total
                      ON score_total.usuario_id_estudante = usuario_estudante.id
                  WHERE usuario_estudante.is_active = 1
                  ORDER BY score_total.total_score DESC;"""
    return db(consulta)

def carregar_ranking(table):
    resultado_formatado = consulta_ranking()

    table.delete(0, END)  # Limpar a tabela antes de carregar os novos dados

    # Adiciona cabeçalhos das colunas
    table.insert(END, "Email Institucional     Username     Score Total")
    table.insert(END, "-" * 60)

    # Adiciona os dados formatados à tabela
    for linha in resultado_formatado:
        email_institucional, username, total_score = linha
        table.insert(END, f"{email_institucional:<25} {username:<15} {total_score:<10}")

def ordenar_score(table):
    resultado_formatado = consulta_ranking()

    # Ordena os resultados pelo total_score
    resultado_formatado.sort(key=lambda x: x[2], reverse=True)

    table.delete(0, END)  # Limpar a tabela antes de carregar os novos dados

    # Adiciona cabeçalhos das colunas
    table.insert(END, "Email Institucional     Username     Score Total")
    table.insert(END, "-" * 60)

    # Adiciona os dados formatados à tabela
    for linha in resultado_formatado:
        email_institucional, username, total_score = linha
        table.insert(END, f"{email_institucional:<25} {username:<15} {total_score:<10}")

def buscar_username(entry_busca, table):
    username = entry_busca.get()

    resultado_formatado = consulta_ranking()

    resultado_filtrado = [linha for linha in resultado_formatado if username.lower() in linha[1].lower()]

    table.delete(0, END)  # Limpar a tabela antes de carregar os novos dados

    # Adiciona cabeçalhos das colunas
    table.insert(END, "Email Institucional     Username     Score Total")
    table.insert(END, "-" * 60)

    # Adiciona os dados formatados à tabela
    for linha in resultado_filtrado:
        email_institucional, username, total_score = linha
        table.insert(END, f"{email_institucional:<25} {username:<15} {total_score:<10}")

def t08():
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

    label_title_page = tk.Label(root, text="RANKING")
    label_title_page.configure(bg=BLUE_BG, fg="ORANGE", font=("Poppins", 22))
    label_title_page.place(relx=0.5, rely=0.1, anchor=tk.CENTER, height=30)

    frame_ranking = tk.Frame(root, bg="orange")
    frame_ranking.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.9, relheight=0.6)  # Defina o relwidth e relheight para 90%

    scrollbar = tk.Scrollbar(frame_ranking)
    scrollbar.pack(side="right", fill="y")

    table = tk.Listbox(frame_ranking, yscrollcommand=scrollbar.set, width=50, bg="white")  # Defina a largura da tabela para 50
    table.pack(expand=YES, fill=BOTH)
    scrollbar.config(command=table.yview)

    button_ordenar = tk.Button(root, text="Ordenar por Score", font=("Poppins", 12), bg="green", fg="orange", command=lambda: ordenar_score(table))
    button_ordenar.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    entry_busca = tk.Entry(root, font=("Poppins", 12))
    entry_busca.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

    button_busca = tk.Button(root, text="Buscar", font=("Poppins", 12), bg="white", fg="orange", command=lambda: buscar_username(entry_busca, table))
    button_busca.place(relx=0.8, rely=0.85, anchor=tk.CENTER)

    carregar_ranking(table)
    
    root.mainloop()

def mostrar_ranking():
    t08()

mostrar_ranking()
