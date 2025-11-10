from Classe_Bibliotheque import Bibliotheque
from Classe_Adherent import Adherent
from Classe_Emprunt import Emprunt
from Classe_Document import *

def sauvegarder_modification():
    pass

def afficher_menu(nom_biblio="Bibliotheque BDEB"):

    # Titre principal
    print("************************************************************")
    print(f"*   Bienvenue à votre bibliothèque : {nom_biblio.center(25)}*")
    print("************************************************************")
    print("*                Faites un choix :                         *")
    print("************************************************************")

    # Liste des options
    options = [
        "1   Ajouter adhérent",
        "2   Supprimer adhérent",
        "3   Afficher tous les adhérents",
        "4   Ajouter document",
        "5   Supprimer document",
        "6   Afficher tous les documents",
        "7   Ajouter emprunt",
        "8   Retour d’un emprunt",
        "9   Afficher tous les emprunts",
        "10  Prolonger un emprunt",
        "11  Sauvegarder les modifications",
        "Q   Quitter le programme"
    ]

    # Affichage des options
    for ligne in options:
        print(f"*   {ligne.ljust(52)}*")

    print("************************************************************")

    # Boucle de saisie utilisateur
    while True:
        choix = input("👉 Choisissez une action (1-11 ou Q pour quitter) : ").strip()
        if choix.upper() == 'Q':
            return 'Q'
        elif choix.isdigit() and 1 <= int(choix) <= 11:
            return int(choix)
        print("❌ Choix erroné ! Veuillez entrer un nombre entre 1 et 11 ou Q.")

# --- Main :) ---
if __name__ == "__main__":

    biblio1 = Bibliotheque("Bibliotheque BDEB")
    biblio1.importer_docs()

    while True:
        choix = afficher_menu("Bibliotheque BDEB")
        if choix == 'Q':
            print("\nMerci d'avoir utilisé la bibliothèque ! À bientôt 👋")
            break
        elif choix == 1:
            Bibliotheque.ajouter_ad()

        elif choix == 2:
            Bibliotheque.enlever_ad()

        elif choix == 3:
            Bibliotheque.afficher_liste_adherents()

        elif choix == 4:
            Bibliotheque.ajouter_doc()

        elif choix == 5:
            Bibliotheque.enlever_doc()

        elif choix == 6:
            biblio1.afficher_liste_docs()

        elif choix == 7:
            Adherent.emprunter_livre()

        elif choix == 8:
            Adherent.rendre_livre()

        elif choix == 9:
            Bibliotheque.afficher_liste_emprunts()

        elif choix == 10:
            pass

        elif choix == 11:
            sauvegarder_modification()




# documents = Bibliotheque.importer_docs()
# print(documents[2].isbn)
# print(documents[2].quantite)
# print(documents[2].auteur)