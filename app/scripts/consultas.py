import sqlite3
from db import db
from uuid import uuid4

def search_user_by_email_institucional(email_institucional):
    consulta = "SELECT password, role FROM usuarios WHERE email_institucional = ?;"
    exC = db(consulta, (email_institucional,))
    return exC


def search_user_data_by_email(email_institucional):
    consulta = """
    SELECT 
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



def insert_new_user(data_list):
    query = """
    INSERT INTO usuarios (id, email_institucional, username, password, recovery_question, recovery_answer, role) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    exc = db(query, data_list)
    return exc


def insert_new_admin(user_id):
    id = str(uuid4())
    query = "INSERT INTO usuario_admin (id, is_active, user_id) VALUES (?, 1, ?)"
    exc = db(query, (id, user_id))
    return exc


def insert_new_student(usuario_id_estudante):
    id = str(uuid4())
    query = "INSERT INTO usuario_estudante (id, is_active, usuario_id_estudante) VALUES (?, 1, ?)"
    parameters = (id, usuario_id_estudante)
    
    # Assuming `db` is a function that handles executing the query with the given parameters.
    exc = db(query, parameters)
    return exc



def insert_new_score_total(id_user_student):
    id_score = str(uuid4())
    query = "INSERT INTO score_total (id, total_score, usuario_id_estudante) VALUES (?, 0, ?)"
    exc = db(query, (id_score, id_user_student))
    return exc


def insert_new_teacher(user_id, responsable):
    id = str(uuid4())
    query = "INSERT INTO usuario_professor (id, is_active, user_id, usuario_id_admin) VALUES (?, 1, ?, ?)"
    exc = db(query, (id, user_id, responsable))
    return exc


def select_10_tf():
    query = "SELECT * FROM questoes_verdadeiro_ou_falso ORDER BY updated_at DESC LIMIT 10"
    exc = db(query)
    return exc

def get_score_id(playerId):
    query ="""SELECT score_total.id FROM score_total
    INNER JOIN usuario_estudante 
    ON usuario_estudante.id = score_total.usuario_id_estudante
    WHERE usuario_estudante.usuario_id = '{playerId}'""";
    exc = db(query)
    return exc