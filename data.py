import connection

class Data :
    @classmethod
    def creation_liste() :
        database = "binomontron"
        bdd = connection.Connection(database)
        cursor = bdd.cursor()
        query ="select * from etudiants;"
        cursor.execute(query)
        liste_pg = [i[1]for i in cursor]
        cursor.close()
        bdd.close()
        return liste_pg