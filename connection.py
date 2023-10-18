import mysql.connector as mysql

class Connection :
    
    @classmethod
    def connexion(cls,user,password,host,port,database) : 
        bdd = mysql.connect(user=user, password=password, host=host, port=port, database=database)
        return bdd
    
    @classmethod
    def deconnexion(cls, bdd, cursor) :
        cursor.fetchall()
        cursor.close()
        bdd.close()
        cursor = None