from db import db
from utils import separa_tupla_em_lista;
import sqlite3

def db(query, parameters=()):
    db_name = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters).fetchall()
        conn.commit()
        return result

class SistemaRanking:
    """docstring for ClassName."""
    def __init__(self):
        pass
        
    def getFullRanking(self, db):
        query = """SELECT usuarios.email_institucional, usuarios.username, score_total.total_score
                  FROM usuarios
                  INNER JOIN usuario_estudante
                      ON usuario_estudante.usuario_id = usuarios.id
                  RIGHT JOIN score_total
                      ON score_total.usuario_id_estudante = usuario_estudante.id
                  WHERE usuario_estudante.is_active = 1
                  ORDER BY score_total.total_score DESC;"""
        result = db(query)
        full_ranking = [(row[0], row[1], row[2]) for row in result]
        return full_ranking
