import tkinter as tk


import tkinter as tk
from tkinter import PhotoImage
from uuid import uuid4
from app.scripts.hash_manager import hasheando
from utils import render_imagem, trata_imagem
import os
from app.scripts.userFactory import UserFactory, UsuarioFactory

class RegisterStudentTemplate():
    """docstring for ClassName."""
    def __init__(self, arg):
        super(UsuarioFactory, self).__init__()
        self.arg = arg
        

    def buildProfileStudent(self):
        self.dataUser = self.getUserData()
        self.user = UserFactory(dataUser[1], dataUser[0], dataUser[2], dataUser[3], dataUser[4], dataUser[5])

    def getUserData(self):
        self.username = inputEmailInstitucional.get().split('@')[0].replace(".", "-")
        self.email_institucional = inputEmailInstitucional.get()
        self.password = inputPassword.get()
        self.recovery_question = inputRecoveryQuestion.get()
        self.recovery_answer = inputRecoveryAnswerr.get()
        self.role="Estudantes"
        return[
            self.username,
            self.email_institucional,
            self.password,
            self.recovery_question,
            self.recovery_answer,
            self.role
        ]
# Example usage
user = TemplateUser()
user.buildProfileStudent(['Nome do Usuario', 'Email do Usuario', 'Role do Usuario'])
