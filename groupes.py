from data import Data
import random

class Groupes :
    @classmethod
    def random_liste(cls) :
        liste_pg = Data.creation_liste()
        random.shuffle (liste_pg)
        return liste_pg
    
    @classmethod
    def creation_groupe(cls, nbre) :
        liste_ml = cls.random_liste()
        if len(liste_ml) %nbre !=0 :
            print ("attention un groupe ne sera pas complet")
        while len(liste_ml) %nbre != 0 :
            liste_ml.append("none")
        
        les_equipes = []
        for etu in range(0,len(liste_ml), nbre) :
            equipe = tuple(liste_ml[etu:etu+nbre])
            les_equipes.append(equipe)
        return les_equipes