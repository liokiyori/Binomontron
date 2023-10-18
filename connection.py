import mysql.connector as mysql

class Connection :
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    
    @classmethod
    def connect_database(cls, database) : 
        bdd = mysql.connect(user=cls.user, password=cls.password, host=cls.host, port=cls.port, database=database)
        return bdd
