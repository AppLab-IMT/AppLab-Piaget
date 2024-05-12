import tkinter as tk

from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("500x700")
root.resizable(width=False, height=False)
root.config(bg="orange")

# Carrega a imagem de fundo e redimensiona
background_image = Image.open("assets/images/bg01.png")
resized_background_image = background_image.resize((500, 700))

# Carrega a imagem de boas-vindas
welcome_image = Image.open("assets/images/img01_welcome.png")

# Carrega imagem de personagems
welcome_image2 = Image.open("assets/images/logo.png")


# Converte as imagens para o formato compatível com o Tkinter
render_background = ImageTk.PhotoImage(resized_background_image)
render_welcome = ImageTk.PhotoImage(welcome_image)
render_characters = ImageTk.PhotoImage(welcome_image2)
# Cria um label para exibir a imagem de fundo
label_background = tk.Label(root, image=render_background)
label_background.place(x=0, y=0, relwidth=1, relheight=1)

# Cria um label para exibir a imagem de boas-vindas sobre a imagem de fundo
label_welcome = tk.Label(root, image=render_welcome, bg="#010F28")
label_welcome.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

label_characters = tk.Label(root, image=render_characters, bg="#010F28")
label_characters.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

btn_root_login = tk.Button(command=rootLogin)

root.mainloop()
