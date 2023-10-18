from groupes import Groupes
from data import Data


print("choisissez l'option que vous voulez-utilisez :")
print("1 pour créez des équipes")
print("2 pour une adresse e-mail")

choix = int(input())

if choix == 1 :
    nbre = int(input("des groupes de quel taille voulez-vous ?"))
    les_equipes = Groupes.creation_groupe(nbre)
    for equipe in les_equipes :
        print("groupes:", equipe)
elif choix == 2 :
    print("entrez le nom de l'étudiant dont vous voulez récupérer le mail :")
    nom = input("")
    mail = Data.recuperation_mail(nom)
    print("le mail de :",nom,"est:",mail)
else : 
    print("l'étudiant est soit introuvable, soit il n'as pas de mail")