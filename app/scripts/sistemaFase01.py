from db import db
from utils import separa_tupla_em_lista

class SistemaFase01:
    def __init__(self):
        pass

    def getQuestions(self):
        query = "SELECT * FROM questoes_verdadeiro_ou_falso ORDER BY updated_at DESC LIMIT 10"
        consulta = db(query)
        return consulta
