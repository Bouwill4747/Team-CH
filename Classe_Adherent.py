from Classe_Emprunt import Emprunt

class Adherent:

    def __init__(self, nom: str, prenom: str, id_adherent: int):
        self.nom = nom
        self.prenom = prenom
        self.id = id_adherent

    # On a une décision à prendre concernant les interactions reliées à ces 2 méthodes-là... Mes propositions seraient
    # plus compliquées mais pretty cool.

    def emprunter_livre(self, bibliotheque, livre):

        # J'me demande si on devrait pas plutôt afficher la liste de documents
        # disponibles et demander à l'utilisateur d'entrer l'ISBN pour l'emprunter...

        if livre.dispo and bibliotheque.livre_existe(livre.titre):
            emprunt = Emprunt(self, livre)
            livre.qte_dispo -= 1
            bibliotheque.liste_emprunts.append(emprunt)
        else:
            print("Ce livre n'est pas disponible ou n'existe pas.")

    def rendre_livre(self, livre):

        # Et ici j'me demande si on devrait pas demander d'entrer un nom d'adhérent, ensuite afficher les
        # livres qu'il a empruntés, et ensuite demander d'entrer l'ISBN du livre à rendre.

        pass

