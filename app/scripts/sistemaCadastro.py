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
        self.idProprio= str(uuid4())
        
    def generateHashing(self):
        normal = self.password
        reverseP = normal[:-1]
        hashing = "!AAUG!"
        hashed = hashing + reverseP + hashing
        return hashed
    
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
    
    def generateUserDb(self, db):
        query = """INSERT INTO usuarios (id, email_institucional, username, password, recovery_question, recovery_answer, role) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        parameters = (self.id, self.email_institucional, self.username, self.hashedPassword, self.recovery_question, self.recovery_answer, self.role)
        return db(query, parameters)
    
    def generateStudentDb(self, db):
        query = """INSERT INTO usuario_estudante (id, is_active, usuario_id) VALUES (?, ?, ?)"""
        parameters = (self.idProprio, 1, self.id)
        return db(query, parameters)
    
    def generateScoreDb(self, db):
        idScore = str(uuid4())
        query = """INSERT INTO score_total (id, total_score, usuario_id_estudante) VALUES (?, ?, ?)"""
        parameters = (idScore, 0, self.idProprio)
        return db(query, parameters)
    
    def generateAdminDb(self, db):
        query = """INSERT INTO usuario_admin (id, usuario_id, is_active) VALUES (?, ?, ?)"""   
        parameters = (self.idProprio, self.id, 1)
        return db(query, parameters)     

    def generateProDb(self, db, adminId):
        query = """INSERT INTO usuario_professor (id,is_active,  usuario_id, usuario_id_admin) VALUES (?, 1,?,?)"""   
        parameters = (self.idProprio, 1, self.id, adminId)
        return db(query, parameters) 

    def generateUserStudentDb(self, db):
        if not self.generateUserDb(db)["success"]:
            return False
        if not self.generateStudentDb(db)["success"]:
            return False
        if not self.generateScoreDb(db)["success"]:
            return False
        return True

    def generateUserAdminDb(self, db):
        if not self.generateUserDb(db)["success"]:
            return False
        if not self.generateAdminDb(db)["success"]:
            return False
        return True

    def generateUserProDb(self, db, adminDb):
        if not self.generateUserDb(db)["success"]:
            return False
        if not self.generateAdminDb(db, adminDb)["success"]:
            return False
        return True






