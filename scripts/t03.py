from re import split
import tkinter as tk
from tkinter import messagebox
from utils import trata_imagem, render_imagem, check_role_by_email


def switch_to_login(root):
    root.destroy()
    from t02 import t02
    t02()
    
def exibe_imagem(email):
    LETTER = check_role_by_email(email)
    PNG = ".png"
    IMG_PATH = "assets/images/avatar-"
    if LETTER == "A":
        return IMG_PATH +LETTER+PNG
    elif LETTER == "B":
        return IMG_PATH +LETTER+PNG
    elif LETTER == "C":
        return IMG_PATH +LETTER+PNG
    
def decode_names(email):
    decode_nome_sobrenome = email[:-15]
    split_por_ponto = decode_nome_sobrenome.split('.')
    primeiro_nome = split_por_ponto[0]
    ultimo_nome = split_por_ponto[1]
    data_listada = [primeiro_nome, ultimo_nome, "Jogar", switch_to_play, "Ranking", 'switch_to_ranking']
    return data_listada

def define_btn_e_texto(email):
    LETTER = check_role_by_email(email)
    if LETTER == "A":
        decode_nome_sobrenome = email[:-15]
        split_por_ponto = decode_nome_sobrenome.split('.')
        primeiro_nome = split_por_ponto[0]
        ultimo_nome = split_por_ponto[1]
        
        data_listada = [primeiro_nome, ultimo_nome, "Jogar", "switch_to_play", "Ranking", 'switch_to_ranking']
        return data_listada
    elif LETTER == "B":
        decode_nome_sobrenome = email[:-15]
        split_por_ponto = decode_nome_sobrenome.split('.')
        primeiro_nome = split_por_ponto[0]
        ultimo_nome = split_por_ponto[1]
       
        data_listada = [primeiro_nome, ultimo_nome, "Cadastrar", 'switch_to_ switch_to_controlled_users', "Ranking", 'switch_to_ranking']
        return data_listada
    elif LETTER == "C":
        decode_nome_sobrenome = email[:-15]
        split_por_ponto = decode_nome_sobrenome.split('.')
        primeiro_nome = split_por_ponto[0]
        ultimo_nome = split_por_ponto[1]
        data_listada = [primeiro_nome, ultimo_nome, "Questoes",' switch_to_questions', "Ranking", 'switch_to_ranking']
        return data_listada
    else:
        return  messagebox.showerror("Erro", "Email inválido")
def t03(user_data):
    print(user_data)
    root = tk.Tk()
    root.geometry("500x700")
    root.title("Bem-Vindo")
    root.resizable(width=False, height=False)
    
    BLUE_BG = "#00102A"
    img_path = exibe_imagem(user_data[1])
    img2 = trata_imagem(img_path, 350, 300)
    r2 = render_imagem(img2)

    lr2 = tk.Label(root, image=r2)
    lr2.config(bg=BLUE_BG)
    lr2.place(relx=0.18, rely=0.22)
   
    lista_dados = define_btn_e_texto(user_data[1])
    user = user_data[0] + "-" + user_data[1]
    lanel_username = tk.Label(root, text=user)
   
    btn_root_loguear = tk.Button(root, text=lista_dados[2])
    btn_root_loguear.configure(bg="#9AFF96", fg="BLACK", font=("Poppins", 22))
    btn_root_loguear.place(relx=0.3, rely=0.8, anchor=tk.CENTER, height=50, width=190)
    
    btn_root_cadastro = tk.Button(root)
    btn_root_cadastro.configure(bg="#CEFFFC", fg="BLACK", text=lista_dados[4], font=("Poppins", 22))
    btn_root_cadastro.place(relx=0.72, rely=0.8, anchor=tk.CENTER,  height=50, width=190)
    
    root.mainloop()
    

t03(['id01','nome.sobrenome@jpiaget.com.br', 'nome-sobrenome', "ADMINISTRADORES", 21, 'uie29'])