import tkinter as tk
from tkinter import messagebox
from uuid import uuid4
class Usuario:
    def __init__(self, email_institucional=None, password=None, recovery_answer=None, initialScore=0, initialPosts=0, responsable=None, isActive = 1, initialRegistrations=0, initialMatches=0, totalWin=0, totalLooses = 0):
        self.id = str(uuid4())
        self.idProprio = str(uuid4())
        self.email_institucional = self.email_institucional
        self.username = self.generateUsername(email_institucional)
        self.passwordHashed = self.generateHash(password)
        self.recoveryQuestion = self.generateRecoveryQuestion(email_institucional)
        self.recoveryAnswer = recovery_answer
        self.role = self.generateRole(email_institucional)
        self.scoreTotal = initialScore
        self.questionsRegistered = initialPosts
        self.usersRegistered = initialRegistrations
        self.responsable = responsable
        self.isActive = isActive
        self.totalMatches = initialMatches
        self.totalWin = totalWin
        self.totalLooses = totalLooses
        
        
    def generateHash(self, password):
        reverse = password[:-1]
        hash = "!AAUG!"
        final = hash + reverse + hash
        return final

    def generateUsername(self, email_institucional):
        username = email_institucional.split('@')[0].replace('.', '-')
        return username

    def generateRecoveryQuestion(self, email_institucional):
        self.email_institucional = email_institucional
        key_admin = '@jpiaget.com.br'
        key_student = '@jpiaget.g12.br'
        key_teacher = '@jpiaget.pro.br'
        if self.email_institucional == None:
            return messagebox.showerror('Erro', 'O campo e-mail institucional é obrigatório')
        else:
            if self.email_institucional.endswith(self.key_admin):
                return "RA"
            elif self.email_institucional.endswith(self.key_student):
                return "RE"
            elif self.email_institucional.endswith(self.key_teacher):
                return "RP"
            else:
                return messagebox.showerror('Erro', 'O padrão de chave não é incorreto')
             
    def generateRole(self, email_institucional):
        self.email_institucional = email_institucional
        key_admin = '@jpiaget.com.br'
        key_student = '@jpiaget.g12.br'
        key_teacher = '@jpiaget.pro.br'
        if self.email_institucional == None:
            return messagebox.showerror('Erro', 'O campo e-mail institucional é obrigatório')
        else:
            if self.email_institucional.endswith(self.key_admin):
                return "ADMIN"
            elif self.email_institucional.endswith(self.key_student):
                return "ESTUDANTE"
            elif self.email_institucional.endswith(self.key_teacher):
                return "PROFESSOR"
            else:
                return messagebox.showerror('Erro', 'O padrão de chave não é incorreto')
            
    def usuarioDBModel(self):
        return{
            'id': self.id,
            'email_institucional': self.email_institucional,
            'username': self.username,
            'password': self.passwordHashed,
            'recovery_question': self.recoveryQuestion,
            'recovery_answer': self.recoveryAnswer,
            'role': self.role
        }
    def scoreDBModel(self):
        return{
            'id': self.idProprio,
            'score_total': self.scoreTotal,
            'total_matches': self.totalMatches,
            'total_looses': self.totalLooses,
            'total_win': self.totalWin,
            'usario_estudante_id': self.id
        }

    def estudanteDBModel(self):
        return{
            'id': self.idProprio,
            'is_active': self.isActive,
            'usuario_id': self.id
        }
        
    def adminDBModel(self):
        return{
            'id': self.idProprio,
            'is_active': self.isActive,
            'usuario_id': self.id,
            'responsable': self.responsable,
            'users_registered': self.usersRegistered
        }
        
    def teacherDBModel(self):
        return{
            'id': self.idProprio,
            'is_active': self.isActive,
            'usuario_id': self.id,
            'responsable': self.responsable,
            'questions_registered': self.questionsRegistered,
        }
        
    def insertUsuarioDb(self, db):
        query = "INSERT INTO usuarios (id, email_institucional, username, password, recovery_question, recovery_answer, role) VALUES (?, ?, ?, ?, ?, ?, ?)"
        exc = db(query, (self.id, self.email_institucional, self.username, self.passwordHashed, self.recoveryQuestion, self.recoveryAnswer, self.role))
        return exc
    
    def updateUsuarioDb(self, db, updates):
      set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
      query = f"UPDATE usuarios SET {set_clause} WHERE id = ?"
      try:
          exc = db(query, (*updates.values(), self.id))
          return exc
      except Exception as e:
          messagebox.showerror('Erro', f'Erro ao atualizar usuário no banco de dados: {e}')
          return None

      def deleteUsuarioDb(self, db):
          query = "DELETE FROM usuarios WHERE id = ?"
          try:
              exc = db(query, (self.id,))
              return exc
          except Exception as e:
              messagebox.showerror('Erro', f'Erro ao deletar usuário no banco de dados: {e}')
              return None

      @classmethod
      def createUsuario(cls, db, email_institucional, password, recovery_answer, initialScore=0, initialPosts=0, responsable=None, isActive=1, initialRegistrations=0, initialMatches=0, totalWin=0, totalLooses=0):
          usuario = cls(email_institucional, password, recovery_answer, initialScore, initialPosts, responsable, isActive, initialRegistrations, initialMatches, totalWin, totalLooses)
          return usuario.insertUsuarioDb(db)
      
        
      def buildFormRegistration(self):
          
          
          