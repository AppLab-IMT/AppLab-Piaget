import tkinter as tk
from utils import trata_imagem, render_imagem
def t08():
    BLUE_BG = "#00102A"
    root = tk.Tk()
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
    
    
    root.mainloop()
    