import uuid4 from uuid
import tkinter as tk

import db from db

class Usuario():
    """docstring for ClassName."""
    def __init__(self, email_institucional=None, password=None, recovery_answer=None, isActive=True):
         self.id = str(uuid4())
         self.email_institucional = email_institucional
         self.username = self.generateUsername()
         self.password = password
         self.passwordEncrypted = self.generateHash()
         self.recovery_question = self.generateRecoveryQuestion()
         self.recovery_answer = recovery_answer
         self.role = self.generateRole()
         self.idProprio = str(uuid4())
         self.profile = self.buildProfile()
         self.register = self.buildRegister()
         self.totalScore = 0
         self.isActive = isActive
         self.root = tk.Tk()
         
     
    def generateUsername(self):
        username = '@' + self.email_institucional.split('@')[0].replace('.', '-')
        return username

     
    def generateHash(self):
        if self.password == None:
            reverse = self.recovery_answer[::-1]
            hash = "!AAUG!"
            final = hash + reverse + hash
            return final
        else:
            self.hashing = "!AAUG!"
            self.hashed = self.hashing + self.password[::-1] + self.hashing
            return self.hashed
     
    def generateRecoveryQuestion(self):
        keyAdmin = "@jpiaget.com.br"
        keyTeacher = "@jpiaget.pro.br"
        keyStudent = "@jpiaget.g12.br"
        
        if self.email_institucional.endswith(keyAdmin):
            role = "RA"
            return role
        elif self.email_institucional.endswith(keyTeacher): 
            role = "RP"
            return role
        elif self.email_institucional.endswith(keyStudent):
            role = "RE"
            return role
        else:
            return False
     
    def generateRole(self):
        keyAdmin = "@jpiaget.com.br"
        keyTeacher = "@jpiaget.pro.br"
        keyStudent = "@jpiaget.g12.br"
        
        if self.email_institucional.endswith(keyAdmin):
            role = "ADMINISTRADORES"
            return role
        elif self.email_institucional.endswith(keyTeacher): 
            role = "PROFESSORES"
            return role
        elif self.email_institucional.endswith(keyStudent):
            role = "ESTUDANTES"
            return role
        else:
            return False
        
     
    def validatePassword(self):
         pass
     
    def toDBUsuarioModel(self):
        return {
            'id' : self.id,
            'email_institucional' : self.email_institucional,
            'username' : self.username,
            'password' :self.passwordEncrypted,
            'recovery_answer':self.recovery_answer,
            'role':self.role
        }
    
    
    def toDBEstudanteModel(self):
        return {
            'id' : self.idProprio,
            'is_active' : self.isActive,
            'usuario_id': self.id
        }
     
    def toDBScoreModel(self):
        return{
            'id' : str(uuid4),
            'total_score' : self.totalScore,
            'usuario_id_estudante' : self.idProprio
        }
    def toRankingModel(self):
        pass     
    def toProfileModel(self):
         pass
     
    def toInsertDb(self, db):
        pass  
         
    def toUpdateDb(self, db):
         pass
     
    def toDeleteDb(self, db):
         pass

    def toSearchDbById(self, db):
        pass
    
    def toValidateLogin(self, db, eI, pU):
        pass
    
    def buildProfile(self):
        pass
    
    def buildRegister(self):
        pass
    
    def buildConfigUser(self):
        pass
    
    def db(self, db):
        pass
    
    def buildLogin(self, db):
        