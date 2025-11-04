import csv

class Bibliotheque:
    def __init__(self, nomBiblio):
        self.nomBibliotheque = nomBiblio

    def __str__(self):
        return self.nomBibliotheque

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
        print("=== Ajouter un adhérent ===")
        no_adherent = input(f"Saisissez l'identifiant de l'adhérent : ")
        nom_adherent = input(f"Saisissez le nom de l'adhérent : ")
        prenom_adherent = input(f"Saisissez le prénom de l'adhérent : ")

        with open("Adherents.csv", "a", newline="") as fichier: # on utilise append ici pour ne pas écraser le contenu du fichier
            writer = csv.writer(fichier)
            writer.writerow([no_adherent,nom_adherent,prenom_adherent])
        print(f"✅ Adhérent #{no_adherent} : {prenom_adherent} {nom_adherent} ajouté avec succès.")


    def enleverAd(self):
        pass

    def ajouterDoc(self):
        pass

    def enleverDoc(self):
        pass

if __name__ == "__main__":
    nomBiblio = Bibliotheque("Ma Bibliothèque")
    print(nomBiblio)
    nomBiblio.afficherListeAdherents()
    nomBiblio.ajouterAd()