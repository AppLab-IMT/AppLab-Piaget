import tkinter as tk
from tkinter import messagebox
from utils import trata_imagem, render_imagem, separa_tupla_em_lista, wrap_text
from consultas import select_10_tf

def renderiza_perguntas(root, perguntas, i):
    # Limpar a tela anterior
    for widget in root.winfo_children():
        widget.destroy()

    BLUE_BG = "#00102A"
    label_pergunta = tk.Label(root, text=perguntas[i][1], wraplength=450)
    label_pergunta.configure(bg=BLUE_BG, fg="WHITE", font=("Poppins", 16), justify="left")
    label_pergunta.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    btn_true = tk.Button(root, text="VERDADEIRO", command=lambda: check_click(root, "Verdadeiro", perguntas, i))
    btn_true.configure(bg="greenyellow", foreground="black", font=("Poppins", 22))
    btn_true.place(relx=0.3, rely=0.9, anchor=tk.CENTER)

    btn_false = tk.Button(root, text="FALSO", command=lambda: check_click(root, "Falso", perguntas, i))
    btn_false.configure(bg="red", foreground="black", font=("Poppins", 22))
    btn_false.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

    if i < len(perguntas) - 1:
        btn_next = tk.Button(root, text="PRÓXIMA", command=lambda: renderiza_perguntas(root, perguntas, i + 1))
        btn_next.configure(bg="blue", fg="white", font=("Poppins", 18))
        btn_next.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


def addDbScore():
    query = "UPDATE TABLE score_total"

def check_click(root, x, datalist, i):
    if (x == "Verdadeiro" and datalist[i][2] == 1) or (x == "Falso" and datalist[i][2] == 0):
        
        
        
        
        msg = "Parabéns, você acertou!" + "\n" + datalist[i][3]
        messagebox.showinfo("Parabéns", msg)
    else:
        messagebox.showerror("Erro", "Resposta Incorreta")

def game_flow(root, perguntas):
    renderiza_perguntas(root, perguntas, 0)

def t05():
    data_tuplas = select_10_tf()
    data_list = separa_tupla_em_lista(data_tuplas)
    perguntas = [data_list[i:i + 7] for i in range(0, len(data_list), 7)]

    root = tk.Tk()
    root.geometry("500x700")
    root.title("Bem-Vindo ao AppLab")
    root.resizable(width=False, height=False)

    BLUE_BG = "#00102A"

    PATH1 = "assets/images/bg01.png"
    img1 = trata_imagem(PATH1, 500, 700)
    r1 = render_imagem(img1)
    lr1 = tk.Label(root, image=r1)
    lr1.place(x=0, y=0)

    label_title_page = tk.Label(root, text="VERDADEIRO OU FALSO")
    label_title_page.configure(bg=BLUE_BG, fg="ORANGE", font=("Poppins", 22))
    label_title_page.place(relx=0.5, rely=0.1, anchor=tk.CENTER, height=30)

    game_flow(root, perguntas)

    root.mainloop()

t05()
