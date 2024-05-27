import sqlite3
import os
class Db:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = sqlite3.connect(self.nome_banco)
            self.cursor = self.conexao.cursor()
            print("Conexão com o banco de dados SQLite estabelecida com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados SQLite: {e}")

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            print("Conexão com o banco de dados SQLite fechada.")

    def executar_query(self, query, parameters=()):
        try:
            self.cursor.execute(query, parameters)
            self.conexao.commit()
            print("Query executada com sucesso.")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao executar a query: {e}")
            return False

# Função db para uso com a classe Db
def db(query, parameters=()):
    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
    db_instance = Db(db_path)
    db_instance.conectar()
    success = db_instance.executar_query(query, parameters)
    db_instance.desconectar()
    return {"success": success}
