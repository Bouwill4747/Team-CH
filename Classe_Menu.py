from Classe_Bibliotheque import Bibliotheque
from Classe_Adherent import Adherent
from Classe_Emprunt import Emprunt
from Classe_Document import *

def sauvegarderModification():
    pass

def importer_docs():
    documents = []
    try:
        with open("livres.csv", "r") as fichier:

            lignes = fichier.readlines()
            del lignes[0] # Supprime la première ligne (qui est les noms de colonne)

            for ligne in lignes:

                ligne = ligne.strip() # Supprime "\n" à la fin de chaque ligne
                e = ligne.split(",")
                titre = e[0]
                isbn = e[1]
                quantite = int(e[2])
                auteur = e[3]

                nouveau_doc =Livre(titre, isbn, quantite, auteur)
                documents.append(nouveau_doc)

    except FileNotFoundError:
        print("❌ Erreur : Le fichier n'existe pas.")

    return documents

def afficherMenu(nom_biblio="Bibliotheque BDEB"):

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
    while True:
        choix = afficherMenu("Bibliotheque BDEB")
        if choix == 'Q':
            print("\nMerci d'avoir utilisé la bibliothèque ! À bientôt 👋")
            break
        elif choix.upper() == '1':
            Bibliotheque.ajouterAd()

        elif choix.upper() == '2':
            Bibliotheque.enleverAd()

        elif choix.upper() == '3':
            Bibliotheque.afficherListeAdherents()

        elif choix.upper() == '4':
            Bibliotheque.ajouterDoc()

        elif choix.upper() == '5':
            Bibliotheque.enleverDoc()

        elif choix.upper() == '6':
            Bibliotheque.afficherListeDocs()

        elif choix.upper() == '7':
            Adherent.emprunterLivre()

        elif choix.upper() == '8':
            Adherent.rendreLivre()

        elif choix.upper() == '9':
            Bibliotheque.afficherListeEmprunts()

        elif choix.upper() == '10':
            Emprunt.prolongerDateRetour()

        elif choix.upper() == '11':
            Bibliotheque.sauvegarderModification()

        else:
            print(f"\n→ Vous avez choisi l'option {choix}\n")
            input("Appuyez sur Entrée pour revenir au menu...")


documents = importer_docs()
print(documents[2].isbn)
print(documents[2].quantite)
print(documents[2].auteur)