import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sistemaLogin import SistemaLogin
from db import db
from sistemaCadastro import SistemaCadastro
from hash_manager import hasheando  # Assuming hasheando is a required function
from utils import render_imagem, trata_imagem  # Assuming these functions are correctly defined in utils module
from sistemaChoices import SistemaChoices
from sistemaTF import SistemaTF
import os
def marca_correta(value):
    if value == "VERDADEIRO":
        return 1
    else:
        return 0
class TemplateBase:
    def __init__(self):
        self.root = None
    
    def buildTemplateBase(self):
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "bg02.png")
        PATH_ICO = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "favicon.ico")
        
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg=DARK_BLUE)
        self.imgTratada = trata_imagem(PATH1, 500, 500)
        self.imgRenderizada = render_imagem(self.imgTratada)
        self.root.iconbitmap(PATH_ICO)
        
        self.label_bg = tk.Label(self.root, image=self.imgRenderizada, bg=DARK_BLUE)
        self.label_bg.place(x=0, y=0)
    
    def buildAppPage(self, renderView=""):
        self.buildTemplateBase()
        if renderView == "":
            pass
        else:
            renderView(self.root)
        self.root.mainloop()
        
   #/***************************************HOME***********************************/
    
    def buildHomePage(self):
        self.buildTemplateBase()
        self.root.title('AppLab')
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title0.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "logo.png")
        self.img1Tratada = trata_imagem(PATH2, 250, 250)
        self.img1Renderizada = render_imagem(self.img1Tratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_4 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.btn_login = tk.Button(self.grid_area_1, text="Login" , width=10, height=1, bg="ORANGE", border=None, fg=DARK_BLUE, command=lambda: self.goToLogin())
        self.btn_registerStudent = tk.Button(self.grid_area_1, text="Matricula",  width=10, height=1, bg="ORANGE", border=None, fg=DARK_BLUE, command=lambda: self.goToRegisterStudent())
        self.btn_project = tk.Button(self.grid_area_1, text="O Projeto", width=10, height=1, bg="ORANGE", border=None, fg=DARK_BLUE, command=lambda: self.goToHome())
        
        self.label_image = tk.Label(self.grid_area_3, image=self.img1Renderizada, bg=DARK_BLUE)
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
       
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_project.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.btn_registerStudent.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.btn_login.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.label_title.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.label_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
           
        self.root.mainloop()

    #/***************************************LOGIN***********************************/
    
    def buildLoginPage(self):
        self.buildTemplateBase()
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title2.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "logo.png")
        self.img1Tratada = trata_imagem(PATH2, 250, 50)
        self.img1Renderizada = render_imagem(self.img1Tratada)
        self.titleTratada = trata_imagem(PATH1, 200, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_4 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        

        self.btn_registerStudent = tk.Button(self.grid_area_1, text="Matricula",  width=10, height=1, bg="ORANGE", border=None, fg=DARK_BLUE, command=lambda: self.goToRegisterStudent())
        self.btn_project = tk.Button(self.grid_area_1, text="AppLab",  width=10, height=1, bg="ORANGE", border=None, fg=DARK_BLUE, command=lambda: self.goToHome())
        
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
        self.label_email_institucional = tk.Label(self.grid_area_3, text='Email institucional', bg=DARK_BLUE, fg="ORANGE")
        self.label_password = tk.Label(self.grid_area_3, text='Senha Usuário' , bg=DARK_BLUE, fg="ORANGE")
        
        self.input_email_institucional = tk.Entry(self.grid_area_3)
        self.input_password = tk.Entry(self.grid_area_3, show="*")
        
        self.btn_login = tk.Button(self.grid_area_3, text="Login",  width=10, height=1, bg="GREENYELLOW", border=None, fg=DARK_BLUE, command=lambda: self.pressLogin(self.input_email_institucional.get(), self.input_password.get()))
        
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_project.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.btn_registerStudent.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.label_title.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.label_email_institucional.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        self.input_email_institucional.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.label_password.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.input_password.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.btn_login.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        
        
        self.root.mainloop()

    #/*********************************Register Student***********************************/

        
    def buildStudentRegister(self):
        self.buildTemplateBase()
        
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title1.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "btn01.png")
        self.btnTratada = trata_imagem(PATH2, 100, 60)
        self.btnRenderizada = render_imagem(self.btnTratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_4 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.btn_project = tk.Button(self.grid_area_1, text="AppLab", bg="#476475", border=None, command=lambda: self.goToHome())
        self.btn_login = tk.Button(self.grid_area_1, text="Login")
        self.btn_registerStudent = tk.Button(self.grid_area_3, text="Matricula")
        
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
        
        self.label_email_institucional = tk.Label(self.grid_area_3, text="Email institucional", bg=DARK_BLUE, fg="ORANGE")
        self.label_password_1 = tk.Label(self.grid_area_3, text="Senha Usuário", bg=DARK_BLUE, fg="ORANGE")
        self.label_password_2 = tk.Label(self.grid_area_3, text="Confirme a senha", bg=DARK_BLUE, fg="ORANGE")
        self.label_question_recovery = tk.Label(self.grid_area_3, text="RE", bg=DARK_BLUE, fg="ORANGE")
        
        self.input_email_institucional = tk.Entry(self.grid_area_3)
        self.input_password_1 = tk.Entry(self.grid_area_3, show="*")
        self.input_password_2 = tk.Entry(self.grid_area_3, show="*")
        self.input_recovery_answer = tk.Entry(self.grid_area_3)
        
        self.btn_registerStudent = tk.Button(self.grid_area_3, text="CADASTRAR", bg="ORANGE", fg="WHITE", command=lambda: self.pressRegister(self.input_email_institucional.get(), self.input_password_1.get(), self.input_password_2.get(), self.input_recovery_answer.get()))
        
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_project.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.btn_login.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.label_title.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7)    
        self.label_email_institucional.place(relx=0.2, rely=0.1, relwidth=0.4, anchor=tk.CENTER)
        self.input_email_institucional.place(relx=0.7, rely=0.1, relwidth=0.4, anchor=tk.CENTER)
        self.label_password_1.place(relx=0.2, rely=0.3, relwidth=0.4, anchor=tk.CENTER)
        self.input_password_1.place(relx=0.7, rely=0.3, relwidth=0.4, anchor=tk.CENTER)
        self.label_password_2.place(relx=0.2, rely=0.5, relwidth=0.4, anchor=tk.CENTER)
        self.input_password_2.place(relx=0.7, rely=0.5, relwidth=0.4, anchor=tk.CENTER)
        self.label_question_recovery.place(relx=0.2, rely=0.7, relwidth=0.4, anchor=tk.CENTER)
        self.input_recovery_answer.place(relx=0.7, rely=0.7, relwidth=0.4, anchor=tk.CENTER)
        self.btn_registerStudent.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

        self.root.mainloop()
        
        
    def buildAdminRegister(self):
        self.buildTemplateBase()
        
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title1.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "btn01.png")
        self.btnTratada = trata_imagem(PATH2, 100, 60)
        self.btnRenderizada = render_imagem(self.btnTratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_4 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.btn_project = tk.Button(self.grid_area_1, text="AppLab", bg="#476475", border=None, command=lambda: self.goToHome())
        self.btn_login = tk.Button(self.grid_area_1, text="Login")
        self.btn_registerStudent = tk.Button(self.grid_area_3, text="Matricula")
        
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
        
        self.label_email_institucional = tk.Label(self.grid_area_3, text="Email institucional", bg=DARK_BLUE, fg="ORANGE")
        self.label_password_1 = tk.Label(self.grid_area_3, text="Senha Usuário", bg=DARK_BLUE, fg="ORANGE")
        self.label_password_2 = tk.Label(self.grid_area_3, text="Confirme a senha", bg=DARK_BLUE, fg="ORANGE")
        self.label_question_recovery = tk.Label(self.grid_area_3, text="RE", bg=DARK_BLUE, fg="ORANGE")
        
        self.input_email_institucional = tk.Entry(self.grid_area_3)
        self.input_password_1 = tk.Entry(self.grid_area_3, show="*")
        self.input_password_2 = tk.Entry(self.grid_area_3, show="*")
        self.input_recovery_answer = tk.Entry(self.grid_area_3)
        
        self.btn_registerStudent = tk.Button(self.grid_area_3, text="CADASTRAR", bg="ORANGE", fg="WHITE", command=lambda: self.pressRegister(self.input_email_institucional.get(), self.input_password_1.get(), self.input_password_2.get(), self.input_recovery_answer.get()))
        
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_project.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.btn_login.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.label_title.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7)    
        self.label_email_institucional.place(relx=0.2, rely=0.1, relwidth=0.4, anchor=tk.CENTER)
        self.input_email_institucional.place(relx=0.7, rely=0.1, relwidth=0.4, anchor=tk.CENTER)
        self.label_password_1.place(relx=0.2, rely=0.3, relwidth=0.4, anchor=tk.CENTER)
        self.input_password_1.place(relx=0.7, rely=0.3, relwidth=0.4, anchor=tk.CENTER)
        self.label_password_2.place(relx=0.2, rely=0.5, relwidth=0.4, anchor=tk.CENTER)
        self.input_password_2.place(relx=0.7, rely=0.5, relwidth=0.4, anchor=tk.CENTER)
        self.label_question_recovery.place(relx=0.2, rely=0.7, relwidth=0.4, anchor=tk.CENTER)
        self.input_recovery_answer.place(relx=0.7, rely=0.7, relwidth=0.4, anchor=tk.CENTER)
        self.btn_registerStudent.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

        self.root.mainloop()
        
    #/************************************PROFESSOR REGISTER**************************************/
    
    def buildTeacherRegister(self, idAdmin):
        self.buildTemplateBase()
        
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title1.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "btn01.png")
        self.btnTratada = trata_imagem(PATH2, 100, 60)
        self.btnRenderizada = render_imagem(self.btnTratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_4 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.btn_project = tk.Button(self.grid_area_1, text="AppLab", bg="#476475", border=None, command=lambda: self.goToHome())
        self.btn_login = tk.Button(self.grid_area_1, text="Login")
        self.btn_registerStudent = tk.Button(self.grid_area_3, text="Cadastrar")
        
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
        
        self.label_email_institucional = tk.Label(self.grid_area_3, text="Email institucional", bg=DARK_BLUE, fg="ORANGE")
        self.label_password_1 = tk.Label(self.grid_area_3, text="Senha Usuário", bg=DARK_BLUE, fg="ORANGE")
        self.label_password_2 = tk.Label(self.grid_area_3, text="Confirme a senha", bg=DARK_BLUE, fg="ORANGE")
        self.label_question_recovery = tk.Label(self.grid_area_3, text="RE", bg=DARK_BLUE, fg="ORANGE")
        
        self.input_email_institucional = tk.Entry(self.grid_area_3)
        self.input_password_1 = tk.Entry(self.grid_area_3, show="*")
        self.input_password_2 = tk.Entry(self.grid_area_3, show="*")
        self.input_recovery_answer = tk.Entry(self.grid_area_3)
        
        self.btn_registerStudent = tk.Button(self.grid_area_3, text="CADASTRAR", bg="ORANGE", fg="WHITE", command=lambda: self.pressRegister(self.input_email_institucional.get(), self.input_password_1.get(), self.input_password_2.get(), self.input_recovery_answer.get()))
        
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_project.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.btn_login.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.label_title.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7)    
        self.label_email_institucional.place(relx=0.2, rely=0.1, relwidth=0.4, anchor=tk.CENTER)
        self.input_email_institucional.place(relx=0.7, rely=0.1, relwidth=0.4, anchor=tk.CENTER)
        self.label_password_1.place(relx=0.2, rely=0.3, relwidth=0.4, anchor=tk.CENTER)
        self.input_password_1.place(relx=0.7, rely=0.3, relwidth=0.4, anchor=tk.CENTER)
        self.label_password_2.place(relx=0.2, rely=0.5, relwidth=0.4, anchor=tk.CENTER)
        self.input_password_2.place(relx=0.7, rely=0.5, relwidth=0.4, anchor=tk.CENTER)
        self.label_question_recovery.place(relx=0.2, rely=0.7, relwidth=0.4, anchor=tk.CENTER)
        self.input_recovery_answer.place(relx=0.7, rely=0.7, relwidth=0.4, anchor=tk.CENTER)
        self.btn_registerStudent.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

        self.root.mainloop()
    # /**************************************Profile Student***************************************/
   #/***************************************HOME***********************************/
    
    def buildProfileStudent(self, dataStudent):
        self.buildTemplateBase()
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title0.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "avatar-C.png")
        self.img1Tratada = trata_imagem(PATH2, 250, 250)
        self.img1Renderizada = render_imagem(self.img1Tratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_4 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.btn_ranking = tk.Button(self.grid_area_1, text="RANKING" , width=10 , height=1, bg="ORANGE")
        self.btn_v_ou_f = tk.Button(self.grid_area_1, text="V-F QUIZ" , width=10, height=1 , bg="ORANGE")
        self.btn_quiz = tk.Button(self.grid_area_1, text="CHOICES", width=10, height=1, bg="ORANGE")
        self.btn_interativo = tk.Button(self.grid_area_1, text="CHOICES", width=10, height=1, bg="ORANGE")

        
        self.label_image = tk.Label(self.grid_area_3, image=self.img1Renderizada, bg=DARK_BLUE)
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
       
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_v_ou_f.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.btn_quiz.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.btn_interativo.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.btn_ranking.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.label_title.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.label_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
           
        self.root.mainloop()    
    
    # /***************************************PROFILE ADMIN***********************************/
    
    def buildProfileAdmin(self, idAdmin):
        self.buildTemplateBase()
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title0.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "avatar-B.png")
        self.img1Tratada = trata_imagem(PATH2, 250, 250)
        self.img1Renderizada = render_imagem(self.img1Tratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_4 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.btn_ranking = tk.Button(self.grid_area_1, text="RANKING" , width=10 , height=1, bg="ORANGE")
        self.btn_v_ou_f = tk.Button(self.grid_area_1, text="V-F QUIZ" , width=10, height=1 , bg="ORANGE")
        self.btn_quiz = tk.Button(self.grid_area_1, text="CHOICES", width=10, height=1, bg="ORANGE")
        self.btn_interativo = tk.Button(self.grid_area_1, text="CHOICES", width=10, height=1, bg="ORANGE")

        
        self.label_image = tk.Label(self.grid_area_3, image=self.img1Renderizada, bg=DARK_BLUE)
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
       
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_v_ou_f.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.btn_quiz.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.btn_interativo.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.btn_ranking.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.label_title.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.label_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
           
        self.root.mainloop()    
    
    
    # /***********************************PROFILE PROFESSOR**********************************/
    def buildProfileTeacher(self, idTeacher):
        self.buildTemplateBase()
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title0.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "avatar-A.png")
        self.img1Tratada = trata_imagem(PATH2, 250, 250)
        self.img1Renderizada = render_imagem(self.img1Tratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_4 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.btn_ranking = tk.Button(self.grid_area_1, text="RANKING" , width=10 , height=1, bg="ORANGE")
        self.btn_v_ou_f = tk.Button(self.grid_area_1, text="V-F QUIZ" , width=10, height=1 , bg="ORANGE")
        self.btn_quiz = tk.Button(self.grid_area_1, text="CHOICES", width=10, height=1, bg="ORANGE")
        self.btn_interativo = tk.Button(self.grid_area_1, text="CHOICES", width=10, height=1, bg="ORANGE")

        
        self.label_image = tk.Label(self.grid_area_3, image=self.img1Renderizada, bg=DARK_BLUE)
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
       
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_v_ou_f.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.btn_quiz.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.btn_interativo.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        self.btn_ranking.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.label_title.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.label_image.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
           
        self.root.mainloop()    
    
    def buildRanking(self):
        self.buildTemplateBase()
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title0.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "avatar-A.png")
        self.img1Tratada = trata_imagem(PATH2, 250, 250)
        self.img1Renderizada = render_imagem(self.img1Tratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.root.mainloop()    

    def buildTrueOrFalse(self):
        self.buildTemplateBase()
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title0.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "avatar-A.png")
        self.img1Tratada = trata_imagem(PATH2, 250, 250)
        self.img1Renderizada = render_imagem(self.img1Tratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.root.mainloop()    

    def buildAddTrueOrFalse(self, idTeacher):
        self.buildTemplateBase()
        DARK_BLUE = "#242231"
        self.idTeacher = idTeacher
        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title5.png")
        self.titleTratada = trata_imagem(PATH1, 200, 40)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
        self.label_enunciado = tk.Label(self.grid_area_3, text="Enunciado: ", bg=DARK_BLUE, fg="ORANGE")
        

        self.input_enunciado = tk.Entry(self.grid_area_3)
        self.label_true_false = tk.Label(self.grid_area_3, text="Indique a Resposta:", bg=DARK_BLUE, fg="ORANGE", font=("Comic Sans", 10, "bold"))
        self.answer = ttk.Combobox(self.grid_area_3, values=["VERDADEIRO", "FALSO"])
        
        self.label_explicacao  = tk.Label(self.grid_area_3, text="Explicação da Resposta:", bg=DARK_BLUE, fg="ORANGE", font=("Comic Sans", 10, "bold"))
        self.input_explicacao = tk.Entry(self.grid_area_3)
        
        self.btn_saveTF = tk.Button(self.grid_area_3, text="SALVAR", bg="ORANGE", fg=DARK_BLUE, font=("Comic Sans", 14, "bold"), command=lambda: self.saveTrueOrFalse(self,
                        self.idTeacher,
                        self.input_enunciado.get(),
                        self.answer.get(),
                        self.input_explicacao.get()))
        
                
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        
        
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.label_title.place(relx=0, rely=0.40)
        
        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        
        
        
        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.label_enunciado.place(relx=0, rely=0.20)
        self.input_enunciado.place(relx=0, rely=0.30)
        self.label_true_false.place(relx=0, rely=0.40)
        self.answer.place(relx=0, rely=0.50)
        self.label_explicacao.place(relx=0, rely=0.60)
        self.input_explicacao.place(relx=0, rely=0.70)
        
        self.btn_saveTF.place(relx=0.5, rely=0.80, anchor=tk.CENTER)
        
        self.root.mainloop()    
    

    def buildChoices(self):
        self.buildTemplateBase()
        DARK_BLUE = "#242231"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title0.png")
        PATH2 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "avatar-A.png")
        self.img1Tratada = trata_imagem(PATH2, 250, 250)
        self.img1Renderizada = render_imagem(self.img1Tratada)
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)
        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.root.mainloop()    
    
    def buildAddChoices(self, idTeacher):
        self.idTeacher = idTeacher
        self.buildTemplateBase()
        DARK_BLUE = "#242231"
        GOLD_PROFILE = "#FFBA09"
        GREEN_BTN = "#34B12F"

        PATH1 = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "title4.png")
        self.titleTratada = trata_imagem(PATH1, 250, 50)
        self.titleRenderizada = render_imagem(self.titleTratada)        
        self.grid_container = tk.Frame(self.root, bg=DARK_BLUE)
        self.grid_area_1 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_2 = tk.Frame(self.grid_container, bg=DARK_BLUE)
        self.grid_area_3 = tk.Frame(self.grid_container, bg=DARK_BLUE)

        self.label_enunciado = tk.Label(self.grid_area_3, text="Enunciado", font=("Arial", 14), bg=DARK_BLUE, fg="white")
        self.label_correct = tk.Label(self.grid_area_3, text="Correta", font=("Arial", 14), bg=DARK_BLUE, fg="white")
        self.label_a = tk.Label(self.grid_area_3, text="Alternativa A", font=("Arial", 14), bg=DARK_BLUE, fg="white")
        self.label_b = tk.Label(self.grid_area_3, text="Alternativa B", font=("Arial", 14), bg=DARK_BLUE, fg="white")
        self.label_c = tk.Label(self.grid_area_3, text="Alternativa C", font=("Arial", 14), bg=DARK_BLUE, fg="white")
        self.label_d = tk.Label(self.grid_area_3, text="Alternativa D", font=("Arial", 14), bg=DARK_BLUE, fg="white")
        self.label_e = tk.Label(self.grid_area_3, text="Alternativa E", font=("Arial", 14), bg=DARK_BLUE, fg="white")
        self.label_explicacao = tk.Label(self.grid_area_3, text="Explicacao", font=("Arial", 14), bg=DARK_BLUE, fg="white")
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)

        self.input_enunciado = tk.Entry(self.grid_area_3, font=("Arial", 14), bg="white")
        self.input_correct = tk.Entry(self.grid_area_3, font=("Arial", 14), bg="white")
        self.input_a = tk.Entry(self.grid_area_3, font=("Arial", 14), bg="white")
        self.input_b = tk.Entry(self.grid_area_3, font=("Arial", 14), bg="white")
        self.input_c = tk.Entry(self.grid_area_3, font=("Arial", 14), bg="white")
        self.input_d = tk.Entry(self.grid_area_3, font=("Arial", 14), bg="white")
        self.input_e = tk.Entry(self.grid_area_3, font=("Arial", 14), bg="white")
        self.input_explicacao = tk.Entry(self.grid_area_3, font=("Arial", 14), bg="white")

        self.btn_back = tk.Button(self.grid_area_1, text="Profile", font=("Arial", 14), height=1 , width=15, bg=GOLD_PROFILE , fg="BLACK", command=lambda: self.goToProfileTeacher(idTeacher))
        self.btn_save = tk.Button(self.grid_area_3, text="Salvar", command=lambda: self.saveChoice(self.input_enunciado.get(),self.input_a.get(), self.input_b.get(), self.input_c.get(), self.input_d.get(), self.input_e.get(), self.input_correct.get(), self.input_explicacao.get(), self.idTeacher), font=('Arial', 14), height=1, width=15, bg=GREEN_BTN , fg="BLACK")


        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)

        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_back.place(relx=0.1, rely=0.5, relwidth=0.7, relheight=0.1)

        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)  
        self.label_title.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7) 
        self.label_enunciado.place(relx=0.1, rely=0)
        self.input_enunciado.place(relx=0.5, rely=0)
        self.label_correct.place(relx=0.1, rely=0.1)
        self.input_correct.place(relx=0.5, rely=0.1)
        self.label_a.place(relx=0.1, rely=0.2)
        self.input_a.place(relx=0.5, rely=0.2)
        self.label_b.place(relx=0.1, rely=0.3)
        self.input_b.place(relx=0.5, rely=0.3)
        self.label_c.place(relx=0.1, rely=0.4)
        self.input_c.place(relx=0.5, rely=0.4)
        self.label_d.place(relx=0.1, rely=0.5)
        self.input_d.place(relx=0.5, rely=0.5)
        self.label_e.place(relx=0.1, rely=0.6)
        self.input_e.place(relx=0.5, rely=0.6)
        self.label_explicacao.place(relx=0.1, rely=0.7)
        self.input_explicacao.place(relx=0.5, rely=0.7)
        self.btn_save.place(relx=0.6, rely=0.9, relwidth=0.3, relheight=0.1)


        self.root.mainloop()   
                
    def pressRegister(self, d1, d2, d3, d4):
        email_institucional = d1
        password_1 = d2
        password_2 = d3
        recovery_answer = d4
        
        if email_institucional == '' or password_1 == '' or password_2 == '' or recovery_answer == '':
            return messagebox.showerror('Erro', 'Todos os campos devem estar preenchidos')
        elif password_1 != password_2:
            return messagebox.showerror('Erro', 'As senhas devem ser iguais')
        else:
            estudante = SistemaCadastro(email_institucional, password_1, recovery_answer)
            try:
                estudante.generateUserStudentDb(db)
                return messagebox.showinfo('Sucesso', 'Registrado com sucesso')
            except ValueError:
                return messagebox.showerror('ERROR', 'Erro ao registrar usuario')
    
    def pressLogin(self, d1, d2):
        email_institucional = d1
        password = d2
        if email_institucional == '' or password == '':
            return messagebox.showerror('Erro', 'Todos os campos devem estar preenchidos')
        else:
            key_admin = "@jpiaget.com.br"
            key_student = "@jpiaget.g12.com"
            key_teacher = "@jpiaget.pro.br"
            if email_institucional.endswith(key_admin):
                user_check = SistemaLogin(email_institucional, password)
                userData = user_check.checkLoginStudent()
                return userData
                return "ADMINISTRADOR"
            elif email_institucional.endswith(key_student):
                return "ESTUDANTES"
            elif email_institucional.endswith(key_teacher):
                return "PROFESSORES"
            else:
                return messagebox.showerror('Erro', 'Email ou senha inválidos')
            
            
    def goToHome(self):
        self.root.destroy()
        self.template = TemplateBase()
        self.template.buildHomePage()

    def goToRegisterStudent(self):
        self.root.destroy()
        self.template = TemplateBase()
        self.template.buildStudentRegister()

    def goToRegisterAdmin(self):
        self.root.destroy()
        self.template = TemplateBase()
        self.template.buildAdminRegister()
        
    def goToRegisterTeacher(self, idAdmin):
        self.root.destroy()
        self.template.buildTeacherRegister(idAdmin)
        
    def goToProfileStudent(self, idStudent):
        self.root.destroy()
        self.template = TemplateBase()
        self.template.buildProfileStudent(idStudent)

    def goToProfileAdmin(self, idAdmin):
        self.root.destroy()
        self.template = TemplateBase()
        self.template.buildProfileAdmin(idAdmin)   
        
        
    def goToProfileTeacher(self, idTeacher):
        self.root.destroy()
        self.template = TemplateBase()
        self.template.buildProfileTeacher(idTeacher)        
        
    def goToLogin(self):
        self.root.destroy()
        self.template = TemplateBase()
        self.template.buildLoginPage()     
        
    def saveChoice(self, enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e, input_correct, explicacao, idTeacher):
        newChoice = [
            enunciado,
            alternativa_a,
            alternativa_b,
            alternativa_c,
            alternativa_d,
            alternativa_e,
            input_correct,  # Supondo que a alternativa correta seja obtida de um campo de entrada
            explicacao,
            idTeacher
        ]

        if '' in newChoice:
            messagebox.showerror('Error', 'Todos os campos devem estar preenchidos')
            return

        # Criando uma instância de SistemaChoices com os dados fornecidos
        sistema = SistemaChoices(newChoice[0], newChoice[1], newChoice[2], newChoice[3], newChoice[4], newChoice[5], newChoice[6], newChoice[7], newChoice[8])

        try:
            sistema.insert_new_choice(db, usuario_professor_id=newChoice[-1])
            messagebox.showinfo('Sucesso', 'Escolha salva com sucesso!')
        except Exception as e:
            messagebox.showerror('Error', f'Erro ao salvar escolha: {str(e)}')

    def saveTrueOrFalse(self,
                        usuario_professor_id,
                        enunciado,
                        is_correta,
                        explicacao
                        ):
        is_correta_nro = marca_correta(is_correta)
        newTF= [
                enunciado,
                is_correta_nro,
                explicacao,
                usuario_professor_id
            ]

        if '' in newTF:
            return messagebox.showerror('Error', 'Todos os campos devem estar preenchidos')
        else:    
            sistema = SistemaTF(newTF[0], newTF[1], newTF[2])

            try:
                sistema.insert_new_TF(db, usuario_professor_id=newTF[-1])
                messagebox.showinfo('Sucesso', 'Escolha salva com sucesso!')
            except Exception as e:
                messagebox.showerror('Error', f'Erro ao salvar escolha: {str(e)}')

    
# Example usage
template = TemplateBase()
#template.buildAddTrueOrFalse("c4697db7-876c-4323-9f21-2bad9d675ba1")
template.buildHomePage()