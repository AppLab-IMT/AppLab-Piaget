class DbUsuario ():

    def __init__(self):
        pass
    
    def db(self, query, parameters=()):	
        db_path = os.path.join(os.path.dirname(__file__), "..", "data", "database.db")
        db_instance = Db(db_path)
        db_instance.conectar()
        
        success = db_instance.executar_query(query, parameters)
        db_instance.desconectar()
        return {"success": success}
    
    
    def insertUsuario(self):
        user = User()
        userDict = user.toDBModel()
        query = "INSERT INTO usuarios (id, email_institucional, username, password, recovery_question, recovery_answer, role) VALUES (?, ?, ?, ?, ?, ?, ?)"
        parameters = (user.get('id'), email_institucional, username, password, recovery_question, recovery_answer, role)
        
        # Assuming `db` is a function that handles executing the query with the given parameters.
        exc = self.db(query, parameters)
        return exc
        