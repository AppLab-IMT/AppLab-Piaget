from tkinter import messagebox
from hash_manager import hasheando
from db import db

class SistemaLogin(object):
    """docstring for SistemaLogin."""
    def __init__(self, email_institucional, password):
        email_institucional = email_institucional.lower()
        password_hashed = hasheando(password)


    def checkLoginStudent(self):
        try:
            query = """SELECT usuarios.id,
                              usuarios.email_institucional,
                              usuarios.username,
                              score_total.total_score,
                              score_total.usuario_id_estudante
                              FROM usuarios
                              INNER JOIN usuario_estudante ON usuario_estudante.usuario_id = usuarios.id
                              RIGHT JOIN score_total ON score_total.usuario_id_estudante = usuario_estudante.id
                              WHERE email_institucional = ? AND password = ?;"""
            parameters={'email_institucional': self.email_institucional, 'password': self.password_hashed}
            result = db(query, parameters)
            return result
        except ValueError :
            return messagebox.showerror('Erro', 'Email ou senha inválido')
        