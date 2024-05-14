import sqlite3
from db import db

def search_user_by_email_institucional(email_institucional):
    consulta = f"SELECT password, role FROM usuarios WHERE email_institucional = ?;"
    exC = db(consulta, (email_institucional,))
    return exC

def search_user_data_by_email(email_institucional):
    consulta = """SELECT 
    usuarios.id,
    usuarios.email_institucional,
    usuarios.username,
    usuarios.role,
    score_total.total_score,
    score_total.usuario_id_estudante
    FROM usuarios
    INNER JOIN usuario_estudante ON usuario_estudante.usuario_id = usuarios.id
    RIGHT JOIN score_total ON score_total.usuario_id_estudante = usuario_estudante.id
    WHERE email_institucional = ?
    ORDER BY score_total.total_score DESC"""
    exC = db(consulta, (email_institucional,))
    return exC
