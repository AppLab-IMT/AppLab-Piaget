import tkinter as tk


import os
from utils import render_imagem, trata_imagem

class AppLab():
    def __init__(self):
        pass
    
    def buildTemplateBase(self):
        self.DARK_BLUE = "#242231"
        self.LIGHT_ORANGE = "ORANGE"
        self.LIGHT_YELLOW = "#FEFFC7"
        self.PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "bg02.png")
        self.PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "logo01Text.png")
        self.PATH3 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "logo.png")

        self.root = tk.Tk()
        self.root.geometry("1440x920")
        self.root.resizable(False, False)
        self.root.configure(bg=self.DARK_BLUE)
        self.imgTratada = trata_imagem(self.PATH1, 1440, 920)
        self.imgRenderizada = render_imagem(self.imgTratada)
        self.imgTitleTratada = trata_imagem(self.PATH2, 440, 100)
        self.imgTitleRenderizada = render_imagem(self.imgTitleTratada)
        self.imgCharactersTratada = trata_imagem(self.PATH3, 420, 480   )
        self.imgCharactersRenderizada = render_imagem(self.imgCharactersTratada)
        
        self.label_bg = tk.Label(self.root, image=self.imgRenderizada, bg=self.DARK_BLUE)
        self.label_bg.place(x=0, y=0)
        
        
    def buildLandingPage(self):
        self.buildTemplateBase()
        
        self.view50_1 = tk.Label(self.root,  bg=self.DARK_BLUE)
        self.view50_1.place(relx=0.25, rely=0.5, relwidth=0.4, relheight=0.6, anchor=tk.CENTER)
        
        self.view50_2 = tk.Label(self.root,  bg=self.DARK_BLUE)
        self.view50_2.place(relx=0.75, rely=0.5, relwidth=0.4, relheight=0.6, anchor=tk.CENTER)
        
        
        self.title = tk.Label(self.view50_1, image=self.imgTitleRenderizada, bg=self.DARK_BLUE)
        self.title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        
        
        self.imgCharacter = tk.Label(self.view50_2, image=self.imgCharactersRenderizada, bg=self.DARK_BLUE)
        self.title.place(relx=0.6, rely=0.35, anchor=tk.CENTER)
        self.imgCharacter.place(relx=0.35, rely=0.45, anchor=tk.CENTER)


        self.btnLogin = tk.Button(self.view50_1, text="LOGIN" , font=("Roboto", 22), width=80, bg=self.LIGHT_ORANGE, border=None, fg=self.DARK_BLUE, command=lambda: self.buildLogin())
        self.btnLogin.place(relx=0.51, rely=0.55,  relheight=0.1,  anchor=tk.CENTER)
       
        
    
    
    def buildLogin(self):
        self.buildTemplateBase()
        
        self.view50_1 = tk.Label(self.root,  bg=self.DARK_BLUE)
        self.view50_1.place(relx=0.25, rely=0.5, relwidth=0.4, relheight=0.6, anchor=tk.CENTER)
        
        self.view50_2 = tk.Label(self.root,  bg=self.DARK_BLUE)
        self.view50_2.place(relx=0.75, rely=0.5, relwidth=0.4, relheight=0.6, anchor=tk.CENTER)
        
       
        self.root.mainloop()            
        
    def buildLoop(self):    
        self.root.mainloop()
        
    def handleLogin(self):
        self.root.destroy()
        self.template = AppLab()
        self.template.buildLoginPage()  
        self.root.mainloop()
    def handleLogin(self):
        self.root.destroy()
        self.template = AppLab()
        self.template.buildLoginPage()  
        
        
        
        
appLab = AppLab()
appLab.buildLandingPage()
        
        
        