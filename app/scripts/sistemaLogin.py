from tkinter import messagebox
from hash_manager import hasheando, rainbow
from db import db
from utils import separa_tupla_em_lista

class SistemaLogin(object):
    """docstring for SistemaLogin."""
    def __init__(self):
        pass

    def checkLoginStudent(self, db, eI, pU):
        self.email_institucional = eI
        self.password = pU
        self.passwordEncrypted = hasheando(self.password)
        
        query = """SELECT usuarios.id,
                    usuarios.email_institucional,
                    usuarios.username,
                    score_total.total_score,
                    score_total.usuario_id_estudante
                FROM usuarios
                INNER JOIN usuario_estudante ON usuario_estudante.usuario_id = usuarios.id
                RIGHT JOIN score_total ON score_total.usuario_id_estudante = usuario_estudante.id
                WHERE usuarios.id =? AND password = ?
                ;"""
        consulta = db(query, parameters=(self.email_institucional, self.passwordEncrypted))
        if(len(consulta) < 0):
            return False
        else:
            return True
        
    def checkIdUser(self, db, email_institucional):
        email_institucional = email_institucional
        query = """SELECT id FROM usuarios WHERE email_institucional = ?;"""
        parameters = (email_institucional)
        return db(query, parameters)
        