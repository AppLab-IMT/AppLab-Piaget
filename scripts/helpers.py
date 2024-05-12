import tkinter as tk
from PIL import Image, ImageTk

def trata_imagem(image_path, size_width, size_height):
    path = Image.open(f"{image_path}")
    tratada = path.resize((size_width, size_height))
    return tratada

def render_imagem(photoImg):
    return ImageTk.PhotoImage(photoImg)