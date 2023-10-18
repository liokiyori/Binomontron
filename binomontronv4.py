# Le code importe deux modules, `mysql.connector` et `random`.
import mysql.connector as mysql
import random

# Cette fonction se connecte à une base de données MySQL à l'aide des informations d'identification fournies et renvoie l'objet de connexion.
def connect_database(database) : 
    user = "root"
    password = "example"
    host = "localhost"
    port = "3307"
    bdd = mysql.connect(user=user, password=password, host=host, port=port, database=database)
    return bdd

#Cette fonction récupère une liste de noms à partir d'une table de base de données appelée etudiants.
def creation_liste() :
    database = "binomontron"
    bdd = connect_database(database)
    cursor = bdd.cursor()
    query ="select * from etudiants;"
    cursor.execute(query)
    liste_pg = [i[1]for i in cursor]
    cursor.close()
    bdd.close()
    return liste_pg

#Cette fonction crée une liste aléatoire en mélangeant une liste préexistante.
def random_liste() :
    liste_pg = creation_liste()
    random.shuffle (liste_pg)
    return liste_pg

# Cette fonction crée des groupes d'une taille spécifiée à partir d'une liste générée aléatoirement et
# ajoute des éléments "aucun" à la liste si nécessaire pour s'assurer que tous les groupes sont complets
def creation_groupe(nbre) :
    liste_ml = random_liste()
    if len(liste_ml) %nbre !=0 :
        print ("attention un groupe ne sera pas complet")
    while len(liste_ml) %nbre != 0 :
        liste_ml.append("none")
    
    les_equipes = []
    for etu in range(0,len(liste_ml), nbre) :
        equipe = tuple(liste_ml[etu:etu+nbre])
        les_equipes.append(equipe)
    return les_equipes

def recuperation_mail(nom) :
    database = "binomontron"
    bdd = connect_database(database)
    cursor = bdd.cursor()
    query ="select * from etudiants where nom = %s;"
    cursor.execute(query, (nom,))
    mail = [i[3]for i in cursor]
    cursor.close()
    bdd.close()    
    return mail


print("choisissez l'option que vous voulez-utilisez :")
print("1 pour créez des équipes")
print("2 pour une adresse e-mail")
choix = int(input())
if choix == 1 :
    nbre = int(input("des groupes de quel taille voulez-vous ?"))
    les_equipes = creation_groupe(nbre)
    for equipe in les_equipes :
        print("groupes:", equipe)
elif choix == 2 :
    print("entrez le nom de l'étudiant dont vous voulez récupérer le mail :")
    nom = input("")
    mail = recuperation_mail(nom)
    print("le mail de :",nom,"est:",mail)
else : 
    print("l'étudiant est soit introuvable, soit il n'as pas de mail")