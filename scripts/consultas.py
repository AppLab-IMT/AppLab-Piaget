# Código 3

from db import db

def consulta_jogador(email_institucional):
    consulta = """SELECT usuarios.id, usuarios.email_institucional, usuarios.username, score_total.total_score
                    FROM usuarios
                    INNER JOIN usuarios_estudante
                        ON usuarios_estudante.usuarios_id = usuarios.id
                    RIGHT JOIN score_total
                        ON score_total.usuarios_id_estudante = usuarios_estudante.id
                    WHERE  usuarios.email_institucional = {email_institucional} 
                    ORDER BY score_total.total_score DESC;"""
    consulta_efetuada = db(consulta, (email_institucional))
    if consulta_efetuada:
        return consulta_efetuada
    else:
        return False
        

def consulta_profile_e_senha(email_institucional, input_password):
    consulta = """SELECT usuarios.email_institucional, usuarios.password, usuarios.role 
                   FROM usuarios 
                   where email_institucional = {email_institucional};"""
    consulta_efetuada = db(consulta(email_institucional))
    if consulta_efetuada:
        return consulta_efetuada
    else:
        return False
