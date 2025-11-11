import csv
from Classe_Document import *
from Classe_Adherent import Adherent

class Bibliotheque:

    def __init__(self, nomBibliotheque):
        self.nomBibliotheque = nomBibliotheque
        self.liste_emprunts = []
        # Au lieu que, comme avant, liste_documents soit une variable isolée qu'on doive "return" pour la rendre
        # accessible, maintenant c'est un attribut de la bibliothèque qui peut être accédé de partout (tant que
        # la bibliothèque est fournie en tant qu'input, ou dans le "main" où elle sera créée).
        self.liste_documents = []
        self.liste_adherents = []
        self.importer_docs() # Importe automatiquement les documents quand la bibliothèque est créée
        self.importer_adherents() # Importe automatiquement les adhérents quand la bibliothèque est créée

    def __str__(self):
        return self.nomBibliotheque

    # def livre_existe(self, titre: str):
    #     for x in self.liste_documents:
    #         if x.titre == titre: # Reste à rendre ça case insensitive
    #             return True
    #     return False

    def importer_docs(self):
        try:
            with open("livres.csv", "r", encoding="utf-8") as fichier: # Le encoding rend ça capable d'interpréter les accents (é,è,à, etc.)

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
                    self.liste_documents.append(nouveau_doc)

        except FileNotFoundError:
            print("❌ Erreur : Le fichier n'existe pas.")

    def importer_adherents(self):
        try:
            with open("Adherents.csv", "r", encoding="utf-8") as fichier:
                lignes = fichier.readlines()
                del lignes[0] # Supprime la première ligne (qui est les noms de colonne)

                for ligne in lignes:

                    ligne = ligne.strip() # Supprime "\n" à la fin de chaque ligne
                    e = ligne.split(",")
                    no_adherent = int(e[0])
                    nom = e[1]
                    prenom = e[2]
                    nouvel_adherent = Adherent(nom, prenom, no_adherent)
                    self.liste_adherents.append(nouvel_adherent)

        except FileNotFoundError:
            print("❌ Erreur : Le fichier n'existe pas.")

    def afficher_liste_docs(self):

        print("\n************************************************************")
        print("*             === Liste documents ===                      *") # :)
        print("************************************************************")

        for doc in self.liste_documents:
            dash_line = '-' * (len(doc.titre) + 4)
            print(f"\n |{dash_line}|\n"
                  f" |  {doc.titre}  |\n"
                  f" |{dash_line}|\n"
                  f"Titre : {doc.auteur} | Quantité : {str(doc.quantite)} | ISBN : {doc.isbn}\n")

    @staticmethod
    def afficher_liste_emprunts():
        print("=== Liste d'Emprunts ===")
        try:
            with open("Emprunts.csv", "r") as fichier:
                reader = csv.reader(fichier, delimiter=",")
                next(reader)
                for ligne in reader:
                    print(ligne[0] + " " + ligne[1] + " " + ligne[2])
        except FileNotFoundError:
            print("❌ Erreur : Le fichier n'existe pas.")

    @staticmethod
    def afficher_liste_adherents():
        print("=== Liste d'adhérents ===")
        try:
            with open("Adherents.csv", "r") as fichier:
                reader = csv.reader(fichier, delimiter=",")
                next(reader)
                for ligne in reader:
                    print(ligne[0] + " " + ligne[1] + " " + ligne[2])
        except FileNotFoundError:
            print("❌ Erreur : Le fichier n'existe pas.")

    @staticmethod
    def ajouter_ad():
        while True:
            print("=== Ajouter un adhérent ===")

            while True:
                adherent = input("Ajouter un nouveau adhérent? (Oui/Non) : ").lower()

                if adherent.lower() == "oui":
                    no_adherent = input("Saisissez l'identifiant de l'adhérent : ")
                    nom_adherent = input("Saisissez le nom de l'adhérent : ")
                    prenom_adherent = input("Saisissez le prénom de l'adhérent : ")

                    with open("Adherents.csv", "a", newline="") as fichier:
                        writer = csv.writer(fichier)
                        writer.writerow([no_adherent, nom_adherent, prenom_adherent])
                    print(f"✅ Adhérent #{no_adherent} : {prenom_adherent} {nom_adherent} ajouté avec succès.")
                    break

                elif adherent == "non":
                    break
                else:
                    print("❌ Réponse non valide, veuillez répondre par 'Oui' ou 'Non'")

            while True:
                retour = input("Revenir au menu principal? (Oui/Non) : ").lower()

                if retour == "oui":
                    return
                elif retour == "non":
                    break
                else:
                    print("❌ Réponse non valide, veuillez répondre par 'Oui' ou 'Non'")

    def enlever_ad(self):

        pass

    def ajouter_doc(self):

        pass

    def enlever_doc(self):

        pass


nomBibliotheque = Bibliotheque("Ma Bibliothèque")
