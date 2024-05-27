from uuid import uuid4
from db import db

class SistemaCadastro:
    
    def __init__(self, email_institucional, confirm_password, recovery_answer):
        self.id = str(uuid4())
        self.email_institucional = email_institucional.lower()
        self.username = self.generateUsername()
        self.password = confirm_password
        self.hashedPassword = self.generateHashing()
        self.recovery_question = self.generateRecoveryQuestion()
        self.recovery_answer = recovery_answer
        self.role = self.generateRole()
        self.idProprio = str(uuid4())
        
    def generateHashing(self):
        self.normal = self.password
        self.reverseP = self.normal[::-1]
        self.hashing = "!AAUG!"
        self.hashed = self.hashing + self.reverseP + self.hashing
        return self.hashed
    
    def generateRecoveryQuestion(self):
        roleEmail = self.email_institucional.split('@')[1].lower()
        if roleEmail == 'jpiaget.g12.com':
            return 'RE'
        elif roleEmail == 'jpiaget.pro.br':
            return 'RP'
        elif roleEmail == 'jpiaget.com.br':
            return 'RA'
        else:
            return False
        
    def generateRole(self):
        roleEmail = self.email_institucional.split('@')[1].lower()
        if roleEmail == 'jpiaget.g12.com':
            return 'ESTUDANTES'
        elif roleEmail == 'jpiaget.pro.br':
            return 'PROFESSORES'
        elif roleEmail == 'jpiaget.com.br':
            return 'ADMINISTRADORES'
        else:
            return False

    def generateUsername(self):
        username = '@' + self.email_institucional.split('@')[1].lower().replace('.', '-')
        return username    
    
    def generateUserDb(self):
        query = """INSERT INTO usuarios (id, email_institucional, username, password, recovery_question, recovery_answer, role) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        parameters = (self.id, self.email_institucional, self.username, self.hashedPassword, self.recovery_question, self.recovery_answer, self.role)
        return db(query, parameters)
    
    def generateStudentDb(self):
        query = """INSERT INTO usuario_estudante (id, is_active, usuario_id) 
                   VALUES (?, ?, ?)"""
        parameters = (self.idProprio, 1, self.id)
        return db(query, parameters)
    
    def generateScoreDb(self):
        idScore = str(uuid4())
        query = """INSERT INTO score_total (id, total_score, usuario_id_estudante) 
                   VALUES (?, ?, ?)"""
        parameters = (idScore, 0, self.idProprio)
        return db(query, parameters)
    
    def generateAdminDb(self):
        query = """INSERT INTO usuario_admin (id, usuario_id, is_active) 
                   VALUES (?, ?, ?)"""   
        parameters = (self.idProprio, self.id, 1)
        return db(query, parameters)     

    def generateProDb(self, adminId):
        query = """INSERT INTO usuario_professor (id, is_active, usuario_id, usuario_id_admin) 
                   VALUES (?, ?, ?, ?)"""   
        parameters = (self.idProprio, 1, self.id, adminId)
        return db(query, parameters) 

    def generateUserStudentDb(self):
        if not self.generateUserDb()["success"]:
            return False
        if not self.generateStudentDb()["success"]:
            return False
        if not self.generateScoreDb()["success"]:
            return False
        return True

    def generateUserAdminDb(self):
        if not self.generateUserDb()["success"]:
            return False
        if not self.generateAdminDb()["success"]:
            return False
        return True

    def generateUserProDb(self, adminDb):
        if not self.generateUserDb()["success"]:
            return False
        if not self.generateProDb(adminDb)["success"]:
            return False
        return True
