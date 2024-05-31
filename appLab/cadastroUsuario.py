from uuid import uuid4


class CadastroUsuario(object):

    def __init__(self, email_institucional, password=None, recovery_answer):
        self.id = uuid4()
        self.email_institucional = email_institucional
        self.username = generateUsername()
        self.password = generatePassword()
        self.recovery_question = generateRecoveryType()
        self.recovery_answer = recovery_answer
        self.role = generateRole()
        
    
    
    def createUser(self, email_institucional, password=None, recovery_answer):
        pass
    
    def generateUsername(self):
       username = '@' + self.email_institucional.split('@')[0].replace('.', '-')
       return username
    
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
        
        
        def generatePassword(self):
            if self.password == None:
                password = '123456'
                return password
            else:
                self.hashing = "!AAUG!"
                self.hashed = self.hashing + self.password[::-1] + self.hashing
                return self.hashed
            