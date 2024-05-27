import tkinter as tk
from tkinter import messagebox
from utils import trata_imagem, render_imagem, check_role_by_email
from switch_pages import switch_to_login, switch_to_register, switch_to_ranking, switch_to_play1, switch_to_play2


def switch_to_login(root):
    root.destroy()
    from t02 import t02
    t02()

def switch_to_ranking(root):
    root.destroy()
    from t08 import t08
    t08()

def switch_to_register(root):
    root.destroy()
    from t04 import t04
    t04()



def switch_to_questions(root):
    root.destroy()
    from t06 import t06
    t06()

def exibe_imagem(email):
    LETTER = check_role_by_email(email)
    PNG = ".png"
    IMG_PATH = "assets/images/avatar-"
    return IMG_PATH + LETTER + PNG

def decode_names(email):
    decode_nome_sobrenome = email[:-15]
    split_por_ponto = decode_nome_sobrenome.split('.')
    primeiro_nome = split_por_ponto[0]
    ultimo_nome = split_por_ponto[1]
    return primeiro_nome, ultimo_nome

def define_btn_e_texto(root, email):
    LETTER = check_role_by_email(email)
    primeiro_nome, ultimo_nome = decode_names(email)
    if LETTER == "A":
        return [primeiro_nome, ultimo_nome, "Jogar", lambda: switch_to_play1(root), "Ranking", lambda: switch_to_ranking(root)]
    elif LETTER == "B":
        return [primeiro_nome, ultimo_nome, "Cadastrar", lambda: switch_to_register(root), "Ranking", lambda: switch_to_ranking(root)]
    elif LETTER == "C":
        return [primeiro_nome, ultimo_nome, "Questoes", lambda: switch_to_play2(root), "Ranking", lambda: switch_to_ranking(root)]
    else:
        messagebox.showerror("Erro", "Email inválido")
        return []

def t03(user_data):
    print(user_data)
    BLUE_BG = "#00102A"
    root = tk.Tk()
    root.geometry("500x700")
    root.title("Bem-Vindo")
    root.config(bg=BLUE_BG)
    root.resizable(width=False, height=False)
    
    img_path = exibe_imagem(user_data[1])
    img2 = trata_imagem(img_path, 350, 300)
    r2 = render_imagem(img2)

    lr2 = tk.Label(root, image=r2)
    lr2.config(bg=BLUE_BG)
    
    lr2.place(relx=0.18, rely=0.22)
   
    lista_dados = define_btn_e_texto(root, user_data[1])
    if not lista_dados:
        return  # Se houver erro, não continuar

    user = user_data[2]
    label_username = tk.Label(root, text=user)
    label_username.configure(bg=BLUE_BG, fg="WHITE", font=("Roboto", 22))
    label_username.place(relx=0.3 , rely=0.65)
   
    btn_function_1 = tk.Button(root, text=lista_dados[4], command=lista_dados[5])
    btn_function_1.configure(bg="#9AFF96", fg="BLACK", font=("Poppins", 22))
    btn_function_1.place(relx=0.3, rely=0.8, anchor=tk.CENTER, height=50, width=190)
    
    btn_root_cadastro = tk.Button(root, text=lista_dados[2], command=lista_dados[3])
    btn_root_cadastro.configure(bg="#CEFFFC", fg="BLACK", font=("Poppins", 22))
    btn_root_cadastro.place(relx=0.72, rely=0.8, anchor=tk.CENTER,  height=50, width=190)
    
    root.mainloop()


