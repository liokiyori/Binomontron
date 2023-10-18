from connection import Connection

class Data :
    @classmethod
    def creation_liste(cls) :
        bdd = Connection.connexion("root","example","localhost",3307,"binomontron")
        cursor = bdd.cursor()
        query ="select * from etudiants;"
        cursor.execute(query)
        liste_pg = [i[1]for i in cursor]
        Connection.deconnexion(bdd, cursor)
        return liste_pg
    @classmethod
    def recuperation_mail(cls, nom) :
        bdd = Connection.connexion("root","example","localhost",3306,"binomontron")
        cursor = bdd.cursor()
        query ="select * from etudiants where nom = %s;"
        cursor.execute(query, (nom,))
        mail = [i[3]for i in cursor]
        Connection.deconnexion(bdd, cursor)
        return mail