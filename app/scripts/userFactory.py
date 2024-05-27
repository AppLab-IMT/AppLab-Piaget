from uuid import uuid4
from hash_manager import hasheando

class UserFactory   :
    def __init__(self, email_institucional, password, recovery_answer):
        self.id = str(uuid4())
        self.email_institucional = email_institucional
        self.username = self.generateUsername()
        self.password = password
        self.encryptedPassword = hashPassword()
        self.recovery_question = self.generateRecoveryQuestion()
        self.recovery_answer = recovery_answer
        self.role = self.generateRole()

    def hashPassword(self):
        return hasheando(self.password)
    
    def generateUsername(self):
        username = self.email_institucional.split('@')[0].replace(".", "-")
        return username 
    
    def generateRole(self):
        if self.email_institucional.endswith("@jpiaget.g12.br"):
            role = "ESTUDANTES"
            return role
        elif self.email_institucional.endswith("@jpiaget.pro.br"):
            role = "PROFESSORES"
            return role
        else:
            role = "ADMINISTRADORES"
            return role
    
    def generateRecoveryQuestion(self):
        if self.email_institucional.endswith("@jpiaget.g12.br"):
            recovery_question = "RE"
            return recovery_question
        elif self.email_institucional.endswith("@jpiaget.pro.br"):
            recovery_question = "RP"
            return recovery_question
        else:
            recovery_question = "RA"
            return recovery_question
            
    def toDBModel(self):
        return {
            'id' : self.id,
            'email_institucional' : self.email_institucional,
            'username' : self.username,
            'password' :self.encryptedPassword,
            'recovery_answer':self.recovery_answer,
            'role':self.role
        }
    
    def toProfileList(self):
        return [
            self.id,
            self.email_institucional,
            self.username,
            self.role,
            self.avatar
        ]
    
    def toCompareList(self):
        return [
            self.email_institucional,
            self.password
        ]
    
        

