import tkinter as tk
from tkinter import messagebox
import re
from user import User
from db import Db

class CadastraUsuario:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x300')
        self.root.title('Cadastra-se')

        self.label_email_institucional = tk.Label(self.root, text='Email institucional')
        self.label_password = tk.Label(self.root, text='Senha Usuário')
        self.label_confirm_password = tk.Label(self.root, text='Confirme a senha')
        self.label_recovery_question = tk.Label(self.root, text='RE - Registro Estudantil')

        self.email_institucional = tk.Entry(self.root, width=50)
        self.password = tk.Entry(self.root, show='*', width=50)
        self.confirm_password = tk.Entry(self.root, show='*', width=50)
        self.recovery_answer = tk.Entry(self.root, width=50)

        self.label_email_institucional.pack()
        self.email_institucional.pack()
        self.label_password.pack()
        self.password.pack()
        self.label_confirm_password.pack()
        self.confirm_password.pack()
        self.label_recovery_question.pack()
        self.recovery_answer.pack()

        self.button_submit = tk.Button(self.root, text='Cadastrar', command=self.submitStudent)
        self.button_submit.pack()

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email)

    def submitStudent(self):
        if (self.password.get() == self.confirm_password.get() and 
            self.email_institucional.get() != '' and 
            self.password.get() != '' and 
            self.confirm_password.get() != '' and 
            self.recovery_answer.get() != ''):

            if not self.validate_email(self.email_institucional.get()):
                return messagebox.showerror('Erro', 'Email institucional inválido')

            try:
                user = User(self.email_institucional.get(), self.confirm_password.get(), self.recovery_answer.get())
                user.insertUserToDB(Db)
                messagebox.showinfo('Cadastrado', 'Cadastrado com sucesso!')
                self.clear_form()
            except ValueError as e:
                return messagebox.showerror('Erro', str(e))
        else:
            return messagebox.showerror('Erro', 'Todos os campos devem estar preenchidos e senha e confirmação devem ser iguais')

    def clear_form(self):
        self.email_institucional.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.confirm_password.delete(0, tk.END)
        self.recovery_answer.delete(0, tk.END)

    def formStudent(self):
        self.root.mainloop()


cadastro = CadastraUsuario()
cadastro.formStudent()
