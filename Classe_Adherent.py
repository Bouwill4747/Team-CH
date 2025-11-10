from Classe_Emprunt import Emprunt

class Adherent:

    def __init__(self, nom: str, prenom: str, id_adherent: int):
        self.nom = nom
        self.prenom = prenom
        self.id = id_adherent

    def emprunter_livre(self, bibliotheque, livre):

        # Demander l'ID d'adhérent
        # Afficher les documents dispos avec ISBN et qté dispo
        # Entrer l'ISBN que vous voulez emprunter

        if livre.dispo and bibliotheque.livre_existe(livre.titre):
            emprunt = Emprunt(self, livre)
            livre.qte_dispo -= 1
            bibliotheque.liste_emprunts.append(emprunt)
        else:
            print("Ce livre n'est pas disponible ou n'existe pas.")

    def rendre_livre(self, bibliotheque, livre):

        # Demander ID adhérent
        # Classer les emprunts avec un numméro devant
        # Afficher les emprunts de cet adhérent la (avec leur numéro à leur gauche)
        # Le user tape un numéro pour choisir quel emprunt rendre
        #
        # Et ici j'me demande si on devrait pas demander d'entrer un nom d'adhérent, ensuite afficher les
        # livres qu'il a empruntés, et ensuite demander d'entrer l'ISBN du livre à rendre.

        adherent = input("Veuillez saisir l'ID d'adhérent : ")
        for x in bibliotheque.liste_adherents:
            if x.

        pass

