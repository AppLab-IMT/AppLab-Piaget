from multiprocessing.connection import answer_challenge
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from networkx import goldberg_radzik
from sistemaFase01 import SistemaFase01
from sistemaRanking import SistemaRanking
from sistemaLogin import SistemaLogin

import tkinter as tk
from tkinter import END, BOTH, YES
from utils import trata_imagem, render_imagem

from sistemaCadastro import SistemaCadastro
from hash_manager import hasheando  # Assuming hasheando is a required function
from utils import render_imagem, trata_imagem, separa_tupla_em_lista  # Assuming these functions are correctly defined in utils module
from sistemaChoices import SistemaChoices
from sistemaTF import SistemaTF
import os
import sqlite3

    
    
def db(query, parameters=()):
    db_name = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters).fetchall()
        conn.commit()
        return result
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
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(bg=DARK_BLUE)
        self.imgTratada = trata_imagem(PATH1, 500, 700)
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
        
        
    def buildAdminRegister(self, idAdmin):
        self.buildTemplateBase()
        self.idAdmin= idAdmin
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
        
        self.btn_registerStudent = tk.Button(self.grid_area_3, text="CADASTRAR", bg="ORANGE", fg="WHITE", command=lambda: self.pressRegisterAdmin(self.input_email_institucional.get(), self.input_password_1.get(), self.input_password_2.get(), self.input_recovery_answer.get()))
        
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
        self.idAdmin = idAdmin
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
        self.btn_cadastrar_professores = tk.Button(self.grid_area_1, text="+Professores" , width=10, height=1 , bg="ORANGE", command=lambda: self.goToRegisterTeacher(idAdmin))
        self.btn_cadastrar_admin = tk.Button(self.grid_area_1, text="+Admin", width=10, height=1, bg="ORANGE", command=lambda: self.goToRegisterAdmin(idAdmin))

        
        self.label_image = tk.Label(self.grid_area_3, image=self.img1Renderizada, bg=DARK_BLUE)
        self.label_title = tk.Label(self.grid_area_2, image=self.titleRenderizada, bg=DARK_BLUE)
       
        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.btn_cadastrar_professores.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.btn_cadastrar_admin.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
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
        self.fase_01 = SistemaFase01()
        self.questions_fase_01 = self.loadQuestions(db)
        
        self.current_question = 0
        self.current_answer = 0
        
        self.question = self.questions_fase_01[self.current_question]
        self.question_text = self.wrap_text(self.question[1][1], 50)
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
        
        question_text = self.wrap_text(self.question_text[0].format(self.current_question), 25)  # Assuming wrap_text wraps text at 50 characters
        self.label_question = tk.Label(self.grid_area_2, text=question_text, bg=DARK_BLUE, fg="ORANGE", wraplength=250, justify="left")
        
        self.btn_true = tk.Button(self.grid_area_3, bg="GREENYELLOW", fg="BLACK", text="VERDADEIRO", command=lambda: self.checkAnswer(1, 1))
        self.btn_false = tk.Button(self.grid_area_3, bg="RED", fg="BLACK", text="FALSO", command=lambda: self.checkAnswer(0, 1))

        self.grid_container.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.75)
        self.grid_area_1.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.grid_area_2.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.3)
        self.grid_area_3.place(relx=0.3, rely=0.3, relwidth=0.7, relheight=0.7)
        self.label_question.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.8)
        self.btn_true.place(relx=0.7 , rely=0.7)
        self.btn_false.place(relx=0.2 , rely=0.7)

        self.root.mainloop()
    def checkAnswer(self, answer, correct_answer):
        if answer == correct_answer:
            
            return messagebox.showinfo("Resposta Certa", "Resposta Certa!")
        else:
            return messagebox.showerror("Resposta Errada", "Resposta Errada!")
    def checkAnswer2(self, answer, correct_answer):
        if answer == correct_answer:
            return messagebox.showinfo("Resposta Certa", "Resposta Certa!")
        else:
            return messagebox.showerror("Resposta Errada", "Resposta Errada!")

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
        self.questions_fase_02 = self.loadChoices(db)
        self.q1_set = self.questions_fase_02[0]
        print(self.q1_set)
        self.set_1 = [self.q1_set[0][0], self.q1_set[0][1], self.q1_set[0][2], self.q1_set[0][3], self.q1_set[0][4], self.q1_set[0][5], self.q1_set[0][6], self.q1_set[0][7], self.q1_set[0][8], self.q1_set[0][9], self.q1_set[0][10], self.q1_set[0][11]]
        self.set_2 = [self.q1_set[1][0], self.q1_set[1][1], self.q1_set[1][2], self.q1_set[1][3], self.q1_set[1][4], self.q1_set[1][5], self.q1_set[1][6], self.q1_set[1][7], self.q1_set[1][8], self.q1_set[1][9], self.q1_set[1][10], self.q1_set[1][11]]
        self.set_3 = [self.q1_set[2][0], self.q1_set[2][1], self.q1_set[2][2], self.q1_set[2][3], self.q1_set[2][4], self.q1_set[2][5], self.q1_set[2][6], self.q1_set[2][7], self.q1_set[2][8], self.q1_set[2][9], self.q1_set[2][10], self.q1_set[2][11]]
        self.set_4 = [self.q1_set[3][0], self.q1_set[3][1], self.q1_set[3][2], self.q1_set[3][3], self.q1_set[3][4], self.q1_set[3][5], self.q1_set[3][6], self.q1_set[3][7], self.q1_set[3][8], self.q1_set[3][9], self.q1_set[3][10], self.q1_set[3][11]]
        self.set_5 = [self.q1_set[4][0], self.q1_set[4][1], self.q1_set[4][2], self.q1_set[4][3], self.q1_set[4][4], self.q1_set[4][5], self.q1_set[4][6], self.q1_set[4][7], self.q1_set[4][8], self.q1_set[4][9], self.q1_set[4][10], self.q1_set[4][11]]

        print(self.set_5)

        
        
        
        
        
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
        
        self.render_view = 0
        
        if  self.render_view == 0: 
            self.render_set(self.grid_area_1, self.grid_area_2, self.grid_area_3,  self.set_1)
        elif self.render_view == 1:
            self.render_set(self.grid_area_1, self.grid_area_2, self.grid_area_3,  self.set_2)
        elif self.render_view == 2:
            self.render_set(self.grid_area_1, self.grid_area_2, self.grid_area_3,  self.set_3)
        else:
            self.render_set(self.grid_area_1, self.grid_area_2, self.grid_area_3,  self.set_4)
            

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
    def pressRegisterAdmin(self, d1, d2, d3, d4):
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
                estudante.generateUserAdminDb(db)
                return messagebox.showinfo('Sucesso', 'Registrado com sucesso')
            except ValueError:
                return messagebox.showerror('ERROR', 'Erro ao registrar usuario')    
    def pressLogin(self, d1, d2):
        self.email_institucional = d1
        self.password = hasheando(d2)
        self.key_admin = '@jpiaget.com.br'
        self.key_student = '@jpiaget.g12.br'
        self.key_teacher = '@jpiaget.pro.br'
        if self.email_institucional == '' or self.password == '':
            return messagebox.showerror('Erro', 'Todos os campos devem estar preenchidos')
        else:
            if self.email_institucional.endswith(self.key_admin):
                sL = SistemaLogin()
                if sL.checkLoginStudent(db, self.email_institucional, self.password):
                    id = sL.checkIdUser(db, self.email_institucional)
                    return self.goToProfileAdmin(id)
                else:
                    return  messagebox.showerror('Erro', 'Senha inválidos')	 
                
            elif self.email_institucional.endswith(self.key_student):
                sL = SistemaLogin()
                if sL.checkLoginStudent(db, self.email_institucional, self.password):
                    id = sL.checkIdUser(db, self.email_institucional)
                    return self.goToProfileStudent(id)
                else:
                    return  messagebox.showerror('Erro', 'Senha inválidos')	    
            elif self.email_institucional.endswith(self.key_teacher):
                sL = SistemaLogin()
                if sL.checkLoginStudent(db, self.email_institucional, self.password):
                    id = sL.checkIdUser(db, self.email_institucional)
                    return self.goToProfileTeacher(id)
                else:
                    return  messagebox.showerror('Erro', 'Senha inválidos')	 
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

    def goToRegisterAdmin(self, idAdmin):
        self.root.destroy()
        self.template = TemplateBase()
        self.template.buildAdminRegister(idAdmin)
        
    def goToRegisterTeacher(self, idAdmin):
        self.root.destroy()
        self.template = TemplateBase()
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

    def loadQuestions(self, db):
        query = "SELECT * FROM questoes_verdadeiro_ou_falso ORDER BY updated_at DESC LIMIT 10"
        result = [db(query)]
    
        return result
    
    def loadChoices(self, db):
        query = "SELECT * FROM questoes_choice ORDER BY updated_at DESC LIMIT 10"
        result = [db(query)]
        return result

    
    
    def wrap_text(self, text, max_words=15):
        words = text.split()
        wrapped_lines = []
        current_line = []
        for word in words:
            current_line.append(word)
            if len(current_line) >= max_words:
                wrapped_lines.append(" ".join(current_line))
                current_line = []
        if current_line:
            wrapped_lines.append(" ".join(current_line))
        return wrapped_lines
    
    def render_set(self, gridArea, gridArea1, gridArea2, setData):
        self.gridArea = gridArea
        self.gridArea1 = gridArea1
        self.gridArea2 = gridArea2
        self.id = setData[0]
        self.enunciado = setData[1] 
        self.a = setData[2]
        self.b = setData[3]
        self.c = setData[4]
        self.d = setData[5]
        self.e = setData[6]
        self.answer = setData[7]
        self.explicacao = setData[8]
        self.author = setData[9]
        self.fase = setData[10]
        self.last_updated = setData[11]
        
        
        self.labelEnunciado = tk.Label(self.gridArea, text=self.enunciado, font=("Arial", 10), bg="blue", fg="white", wraplength=100)
        self.btnA = tk.Button(self.gridArea1, text=self.a, font=("Arial", 10), bg="ORANGE", fg="black", wraplength=200, command=lambda: self.checkAnswer2("a", self.answer))
        self.btnB = tk.Button(self.gridArea2, text=self.b, font=("Arial", 10), bg="ORANGE", fg="black", wraplength=200, command=lambda: self.checkAnswer2("b", self.answer))
        self.btnC = tk.Button(self.gridArea2, text=self.c, font=("Arial", 10), bg="ORANGE", fg="black", wraplength=200, command=lambda: self.checkAnswer2("c", self.answer))
        self.btnD = tk.Button(self.gridArea2, text=self.d, font=("Arial", 10), bg="ORANGE", fg="black", wraplength=200, command=lambda: self.checkAnswer2("d", self.answer))
        self.btnE = tk.Button(self.gridArea2, text=self.e, font=("Arial", 10), bg="ORANGE", fg="black", wraplength=200, command=lambda: self.checkAnswer2("e", self.answer))

        

        self.labelEnunciado.pack(side="top", fill="both", expand=True)
        self.btnA.pack(side="top", fill="both", expand=True)
        self.btnB.pack(side="top", fill="both", expand=True)
        self.btnC.pack(side="top", fill="both", expand=True)
        self.btnD.pack(side="top", fill="both", expand=True)
        self.btnE.pack(side="top", fill="both", expand=True)
        
        
        
# Example usage
template = TemplateBase()
#template.buildAddTrueOrFalse("c4697db7-876c-4323-9f21-2bad9d675ba1")
template.buildHomePage()