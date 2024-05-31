import tkinter as tk
from utils import trata_imagem, render_imagem


def switch_to_login(root):
    root.destroy()
    from t02 import t02
    t02()

def switch_to_register(root):
    root.destroy()
    from t04 import t04
    t04()

def t01():
    root = tk.Tk()
    root.geometry("500x700")
    root.title("Bem-Vindo ao AppLab")
    root.resizable(width=False, height=False)
    
    BLUE_BG = "#00102A"
    
    PATH1 = "./assets/images/bg01.png"
    PATH2 = "assets/images/img01_welcome.png"
    PATH3 = "assets/images/logo.png"
    
    img1 = trata_imagem(PATH1, 500, 700)
    img2 = trata_imagem(PATH2, 350, 100)
    img3 = trata_imagem(PATH3, 250, 250)
    
    r1 = render_imagem(img1)
    r2 = render_imagem(img2)
    r3 = render_imagem(img3)
    
    lr1 = tk.Label(root, image=r1)
    lr2 = tk.Label(root, image=r2)
    lr2.config(bg=BLUE_BG)
    lr3 = tk.Label(root, image=r3)
    lr3.config(bg=BLUE_BG)
    
    lr1.place(x=0, y=0)
    lr2.place(relx=0.18, rely=0.1)
    lr3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
   
    btn_root_loguear = tk.Button(root, text="Entrar", command=lambda: switch_to_login(root))
    btn_root_loguear.configure(bg="#9AFF96", fg="BLACK", font=("Poppins", 22))
    btn_root_loguear.place(relx=0.3, rely=0.8, anchor=tk.CENTER, height=50, width=190)
    
    btn_root_cadastro = tk.Button(root)
    btn_root_cadastro.configure(bg="#CEFFFC", fg="BLACK", text="Matricula", font=("Poppins", 22) ,command=lambda: switch_to_register(root))
    btn_root_cadastro.place(relx=0.72, rely=0.8, anchor=tk.CENTER,  height=50, width=190)
    
    root.mainloop()
    

t01()
