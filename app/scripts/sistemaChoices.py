from datetime import datetime
from uuid import uuid4
from db import db

class SistemaChoices:
    """docstring for ClassName."""
    def __init__(self, enunciado, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e, correta, explicacao, usuario_professor_id):
        self.id = str(uuid4())
        self.enunciado = enunciado,
        self.alternativa_a = alternativa_a,
        self.alternativa_b, = alternativa_b,
        self.alternativa_c = alternativa_c,
        self.alternativa_d = alternativa_d,
        self.alternativa_e= alternativa_e,
        self.correta = correta,
        self.explicacao = explicacao,
        self.usuario_professor_id = usuario_professor_id
        
    
    def insert_new_choice(self, db, usuario_professor_id):
        current_date = datetime.now()
        updated_at_date = current_date.isoformat()
        query = """INSERT INTO questoes_choice(
            id, 
            enunciado, 
            alternativa_a, 
            alternativa_b, 
            alternativa_c, 
            alternativa_d, 
            alternativa_e, 
            correta, 
            explicacao, 
            usuario_professor_id, 
            fase_jogo_id,
            updated_at
            ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )"""
        parameters = (self.id, self.enunciado[0], self.alternativa_a[0], self.alternativa_b[0], self.alternativa_c[0], self.alternativa_d[0], self.alternativa_e[0], self.correta[0], self.explicacao[0], usuario_professor_id, 2, updated_at_date)
        return db(query, parameters)


    def update_choice(self):
        current_date = datetime.now()
        updated_at_date = current_date.isoformat()
        query = """UPDATE questoes_verdadeiro_ou_falso(
            id, 
            enunciado, 
            alternativa_a, 
            alternativa_b, 
            alternativa_c, 
            alternativa_d, 
            alternativa_e, 
            correta, 
            explicacao, 
            usuario_professor_id, 
            fase_jogo_id,
            updated_at
            ) VALUES (
            ?, ?, ?, ?, ?, ?, ?,? ,?, ?, ?, ?
            )"""
        parameters = (self.id, self.enunciado, self.alternativa_a, self.alternativa_b, self.alternativa_c, self.alternativa_d, self.alternativa_e, self.correta, self.explicacao, self.usuario_professor_id, 2, updated_at_date)
        return db(query, parameters)
    