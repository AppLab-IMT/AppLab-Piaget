from datetime import datetime
from uuid import uuid4
from db import db

class SistemaTF:
    """docstring for ClassName."""
    def __init__(self, enunciado, is_correta, explicacao, idTeacher):
        self.id = str(uuid4())
        self.enunciado = enunciado,
        self.is_correta = is_correta,
        self.explicacao = explicacao
        self.usuario_id_professor = idTeacher
    def insert_new_TF(self, db):
        current_date = datetime.now()
        updated_at_date = current_date.isoformat()
        query = """INSERT INTO questoes_verdadeiro_ou_falso(
            id, 
            enunciado, 
            is_correta, 
            explicacao, 
            usuario_professor_id, 
            fase_jogo_id,
            updated_at
            ) VALUES (
            ?, ?, ?, ?, ?, ?, ?
            )"""
        parameters = (self.id, self.enunciado, self.is_correta, self.explicacao, self.usuario_professor_id, 1, updated_at_date)
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
    