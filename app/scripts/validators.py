from tkinter import messagebox
from uuid import uuid4
from utils import to_caixa_baixa
from hash_manager import hasheando
from consultas import insert_new_score_total, insert_new_teacher, insert_new_user, insert_new_admin, insert_new_student
def validate_input_email(email, password, question, answer, responsable=""):
    admin_keys = ["@jpiaget.com.br", "com", "ADMINISTRADORES", "B", "#F86442", "ORANGE"]
    students_keys = ["@jpiaget.g12.br", "g12", "ESTUDANTES", "A", "#FEEE41", "YELLOW"]
    teacher_keys = ["@jpiaget.pro.br", "pro", "PROFESSORES", "C", "#4942EF", "BLUE"]
    
    lower_email = to_caixa_baixa(email)
    if lower_email.endswith(admin_keys[0]):
        id = str(uuid4())
        email_institucional = lower_email
        username = get_username(lower_email)
        password_hash =get_password(password)
        
        data_list = [id, email_institucional, username, password_hash, question, answer, admin_keys[2]]
        insert_new_user(data_list)
        insert_new_admin(id)
        return messagebox.showinfo("Sucesso", "Usuario criado com sucesso")
        
    elif lower_email.endswith(students_keys[0]):
        id = str(uuid4())
        email_institucional = lower_email
        username = get_username(lower_email)
        password_hash = get_password(password)
        id_user_student = str(uuid4())
        
        data_list = [id, email_institucional, username, password_hash, question, answer, students_keys[2]]
        insert_new_user(data_list)
        insert_new_student(id)
        insert_new_score_total(id_user_student)
        return messagebox.showinfo("Sucesso", "Usuario criado com sucesso")
    
    elif lower_email.endswith(teacher_keys[0]):
        id = str(uuid4())
        email_institucional = lower_email
        username = get_username(lower_email)
        password_hash = get_password(password)
        
        
        data_list = [id, email_institucional, username, password_hash, question, answer, teacher_keys[2]]
        if responsable:
            insert_new_user(data_list)
            insert_new_teacher(id, responsable)
            return messagebox.showinfo("Sucesso", "Usuario criado com sucesso")        
        else:
            return messagebox.showerror("Erro", "Preencha o responsavel, nao e autorizado a criar um novo professor")

    
def get_password(password):
    if len(password) < 12 and len(password) > 4 and not password.count('!'):
        return hasheando(password)
    else:
        return 'ERROR PASSWORD'


def get_username(email_institucional):
    fullname = email_institucional.split('@')[0]
    username = fullname.replace('.', '-')
    return username
     