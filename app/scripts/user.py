import os
from uuid import uuid4
import hashlib
from db import Db

class User:
    def __init__(self, email_institucional, password, recovery_answer):
        self.id = str(uuid4())
        self.email_institucional = email_institucional
        self.username = '@' + self.generateUsername()
        self.password = password
        self.passwordEncrypted = self.generateHash()
        self.recovery_question = self.generateRecoveryQuestion()
        self.recovery_answer = recovery_answer
        self.role = self.generateRole()

    def generateUsername(self):
        username = self.email_institucional.split("@")[0].replace('.', '-')
        return username

    def generateHash(self):
        if '!' in self.password:
            r = self.password[:-1]
            hash = '!AAUG!'
            hashed = hash + r + hash
            return hashed
        else:
            return hashlib.sha256(self.password.encode()).hexdigest()

    def generateRecoveryQuestion(self):
        if self.email_institucional.endswith('@jpiaget.g12.br'):
            return 'RE'
        elif self.email_institucional.endswith('@jpiaget.pro.br'):
            return 'RP'
        elif self.email_institucional.endswith('@jpiaget.com.br'):
            return 'RA'
        else:
            return False

    def generateRole(self):
        if self.email_institucional.endswith('@jpiaget.g12.br'):
            return 'ESTUDANTES'
        elif self.email_institucional.endswith('@jpiaget.pro.br'):
            return 'PROFESSORES'
        elif self.email_institucional.endswith('@jpiaget.com.br'):
            return 'ADMINISTRADORES'
        else:
            return False

    def toDBModel(self):
        return {
            'id': self.id,
            'email_institucional': self.email_institucional,
            'username': self.username,
            'password': self.passwordEncrypted,
            'recovery_question': self.recovery_question,
            'recovery_answer': self.recovery_answer,
            'role': self.role
        }

    def insertUserToDB(self, Db):
        conexion = Db(os.path.join(os.path.dirname(__file__), "..", "data", "database.db"))
        conexion.conectar()
        query = "INSERT INTO usuarios (id, email_institucional, username, password, recovery_question, recovery_answer, role) VALUES (:id, :email_institucional, :username, :password, :recovery_question, :recovery_answer, :role)"
        conexion.executar_query(query, self.toDBModel())  # Removed self
        conexion.desconectar()
