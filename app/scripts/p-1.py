import tkinter as tk
from utils import trata_imagem, render_imagem
from switch_pages import switch_to_register, switch_to_login



def main():
    BG_COLOR = "#00102A"
    BG_COLOR2="#ffb300"
    BG_COLOR3 = "#F3BC00"
    TEXT_COLOR = "#f8f8ff"
    TEXT_COLOR2 = "#424949"

    IMG_BG = "assets/images/bg01.png"
    IMG_LOGO = "assets/images/logoApp.png"

    
    root = tk.Tk()
    root.geometry('700x600')
    root.configure(bg=BG_COLOR)
    root.resizable(width=False, height=False)
    root.title('AppLab')
    
    img_tratada = trata_imagem(IMG_BG, 700, 600)
    img_renderizada = render_imagem(img_tratada)
    bg_label = tk.Label(root , image=img_renderizada)
    bg_label.place(x=0, y=0)
    
    frame_1 = tk.Frame(root, bg=BG_COLOR, width=700 , height=100)
    frame_1.pack()
    
    frame_2 = tk.Frame(root, bg=BG_COLOR2, width=700 , height=400)
    frame_2.pack()
    
    frame_3 = tk.Frame(root, bg=BG_COLOR, width=700 , height=100)
    frame_3.pack()
    
    
    image_label_1 = "assets/images/bg01.png"
    image_label_1 = trata_imagem(image_label_1, 700, 100)
    image_label_1 = render_imagem(image_label_1)
    label_1 = tk.Label(frame_1, image=IMG_BG)
    label_1.pack()
    
    
    image_label_2 = trata_imagem(IMG_LOGO, 700, 100)
    image_label_2 = render_imagem(image_label_2)
    label_2 = tk.Label(frame_2, image=image_label_2)
    label_2.pack()
    button_register = tk.Button(frame_3, text="Matricula", bg=BG_COLOR3, fg=TEXT_COLOR2, font=("Poppins", 22), command=lambda: switch_to_register(root))
    button_register.place(relx=0.35, rely=0.5, anchor=tk.CENTER, height=50, width=190)
    
    button_login = tk.Button(frame_3, text="LOGIN", bg=BG_COLOR3, fg=TEXT_COLOR2, font=("Poppins", 22), command=lambda: switch_to_register(root))
    button_login.place(relx=0.65, rely=0.5, anchor=tk.CENTER, height=50, width=190)
    root.mainloop()

main()


