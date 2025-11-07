import csv
from Classe_Document import *
class Bibliotheque:
    def __init__(self, nomBibliotheque):
        self.nomBibliotheque = nomBibliotheque

    def __str__(self):
        return self.nomBibliotheque

    @staticmethod
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

        for x in documents:
            print(x)


    @staticmethod
    def afficherListeDocs():
        print("=== Liste de documents ===")
        try:
            with open("Documents.csv", "r") as fichier:
                reader = csv.reader(fichier, delimiter=",")
                next(reader)
                for ligne in reader:
                    print(ligne[0] + " " + ligne[1] + " " + ligne[2])
        except FileNotFoundError:
            print("❌ Erreur : Le fichier n'existe pas.")

    @staticmethod
    def afficherListeEmprunts():
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
    def afficherListeAdherents():
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
    def ajouterAd():
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

    def enleverAd(self):
        pass

    def ajouterDoc(self):
        pass

    def enleverDoc(self):
        pass

    def sauvegarderModification(self):
        pass

nomBibliotheque = Bibliotheque("Ma Bibliothèque")
nomBibliotheque.importer_docs()
