import tkinter as tk
from utils import trata_imagem, render_imagem
def tela1():
    
    # define variaveis constantes
    WIDTH_VIEW = 450
    WIDTH_frame_2a = int(WIDTH_VIEW *  0.125)
    WIDTH_frame_2b = int(WIDTH_VIEW *  0.875)
    HEIGHT_VIEW = 700
    
    HEIGHT_FRAME_1 = int(HEIGHT_VIEW *  5 / 100)
    HEIGHT_FRAME_2 = int(HEIGHT_VIEW * 90 / 100)
    HEIGHT_FRAME_3 = int(HEIGHT_VIEW *  5 / 100)
    VIEW = f"{WIDTH_VIEW}x{HEIGHT_VIEW}"
    BLUE_BG = "#00102A"
    YELLOW = "yellow"
    ORANGE = "orange"
    LOGO_API = 'assets/images/logoApp.png' 
    PATH_BG = "assets/images/bg01.png"
    
    # chama tela principal
    root = tk.Tk()
    
    root.geometry(VIEW)
    root.title("Bem-Vindo ao AppLab")
    root.iconbitmap(LOGO_API)
    root.configure(bg=BLUE_BG)
    root.resizable(width=False, height=False)
    
    # trata e seteia img de fundo
    bg_tratado = trata_imagem(PATH_BG, WIDTH_VIEW, HEIGHT_VIEW)
    bg_renderizado = render_imagem(bg_tratado)
    bg_label = tk.Label(root, image=bg_renderizado)
    bg_label.config(bg=BLUE_BG)
    bg_label.place(x=0, y=0)
    
    # grid - frames - widgets
    frame_1 = tk.Frame(root, width=WIDTH_VIEW, height=HEIGHT_FRAME_1)
    frame_1.configure(bg=BLUE_BG)
    frame_2A = tk.Frame(root, width=WIDTH_frame_2a, height=HEIGHT_FRAME_2)
    frame_2A.configure(bg=ORANGE)
    frame_2B = tk.Frame(root, width=WIDTH_frame_2b, height=HEIGHT_FRAME_2)
    frame_2B.configure(bg=BLUE_BG)
    frame_3 = tk.Frame(root, width=WIDTH_VIEW, height=HEIGHT_FRAME_3)
    frame_3.configure(bg=BLUE_BG)
    frame_1.pack()
    frame_2A.place(relwidth=0.75, relx=0.1, rely=0.5, anchor=tk.CENTER)
    frame_2B.place(relwidth=0.15, relx=0.5, rely=0.5, anchor=tk.CENTER)
    frame_3.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
    root.mainloop()
    
    
tela1()