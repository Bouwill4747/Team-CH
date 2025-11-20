import re # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
from Document import *
from Adherent import Adherent
from Emprunt import Emprunt
import Affichage

class Bibliotheque:
    def __init__(self, nom_bibliotheque):
        self.nom_bibliotheque = nom_bibliotheque
        self.liste_emprunts = []
        self.liste_documents = []
        self.liste_adherents = []
        self.importer_documents() # Importe automatiquement les documents quand la bibliothèque est créée
        self.importer_adherents() # Importe automatiquement les adhérents quand la bibliothèque est créée
        self.importer_emprunts() # Importe automatiquement les emprunts quand la bibliothèque est créée

    def __str__(self):
        return self.nom_bibliotheque

# Importe et crée une liste de documents avec attributs : titre, isbn, quantite, auteur
    def importer_documents(self):
        try:
            with open("livres.csv", "r", encoding="utf-8") as fichier:
                lignes = fichier.readlines()[1:]  # Supprime la première ligne (en-tête)
                for ligne in lignes:
                    e = ligne.strip().split(",")
                    titre, isbn, quantite, auteur = e[0], e[1], int(e[2]), e[3]
                    self.liste_documents.append(Livre(titre, isbn, quantite, auteur))
        except FileNotFoundError:
            print("Erreur : Le fichier livres.csv n'existe pas.")


# Importe et crée une liste d'adhérents avec les attributs : nom, prenom, id_adherent
    def importer_adherents(self):
        try:
            with open("adherents.csv", "r", encoding="utf-8") as fichier:
                lignes = fichier.readlines()[1:] # Supprime la première ligne (en-tête)
                for ligne in lignes:
                    nom, prenom = ligne.strip().split(",")[:2]
                    self.liste_adherents.append(Adherent(nom, prenom, self))
        except FileNotFoundError:
            print("Erreur : Le fichier adherents.csv n'existe pas.")


# Importe et crée une liste d'emprunts avec les attributs : (à voir)
    def importer_emprunts(self):
        try:
            with open("emprunts.csv", "r", encoding="utf-8") as fichier:
                lignes = fichier.readlines()[1:]
                for ligne in lignes:
                    e = ligne.strip().split(",")
                    id_adherent, isbn = int(e[0]), e[2]

                    try:
                        adherent = next(a for a in self.liste_adherents if a.id == id_adherent)
                    except StopIteration:
                        print(f"❌ Aucun adhérent avec l'ID {id_adherent} trouvé. Emprunt ignoré.")
                        continue

                    try:
                        livre = next(l for l in self.liste_documents if l.isbn == isbn)
                    except StopIteration:
                        print(f"❌ Aucun document avec l'ISBN {isbn} trouvé. Emprunt ignoré.")
                        continue

                    self.liste_emprunts.append(Emprunt(adherent, self, livre))
        except FileNotFoundError:
            print("Erreur : Le fichier emprunts.csv n'existe pas.")

# Ajouter un adhérent
    def ajouter_ad(self):
        while True: # boucle interne pour permettre d'ajouter un autre adhérent à la fin de la méthode

            # Saisie de l'utilisateur
            while True:
                nom = input("Saisissez le nom de l'adhérent : ").strip()
                if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\-]+$", nom): # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
                    print("❌ Le nom ne peut contenir que des lettres et un tiret. Réessayez.")
                else:
                    break
            while True:
                prenom = input("Saisissez le prénom de l'adhérent : ").strip()
                if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\-]+$", prenom): # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
                    print("❌ Le prénom ne peut contenir que des lettres et un tiret. \n Réessayez...")
                else:
                    break

            # Recherche si le nom et prénom se retrouvent déjà dans la liste d'adhérents
            try:
                doublon = next(a for a in self.liste_adherents
                               if a.nom.strip().lower() == nom.lower() and a.prenom.strip().lower() == prenom.lower())
                print(f"❌ L'adhérent {nom} {prenom} existe déjà. Ajout annulé.")
            except StopIteration:
                nouvel_adherent = Adherent(nom, prenom, self)
                self.liste_adherents.append(nouvel_adherent)
                print(f"✅ Adhérent #{nouvel_adherent.id} : {nom} {prenom} ajouté avec succès.")

            # On demande à l’utilisateur s’il veut ajouter un 2e adhérent ou revenir au menu
            while True:
                while True:
                    choix = input("Voulez-vous ajouter un autre adhérent ? (O/N) : ").strip().upper()
                    if choix in ("O", "N"):
                        break
                    print("❌ Réponse invalide. O ou N.")
                if choix == "N":
                    return

# Supprimer un adhérent
    def enlever_ad(self):
        while True: # boucle interne pour permettre de supprimer un autre adhérent à la fin de la méthode
            Affichage.afficher_liste_adherents(self) # Affiche la liste d'adhérents actuels

            # Saisie de l'utilisateur
            try:
                identifiant = int(input("Saisissez l'ID de l'adhérent à supprimer : "))
            except ValueError:
                print("❌ Entrez un numéro valide.")
                continue

            try: # Recherche l'adhérent dans la liste
                adherent = next(a for a in self.liste_adherents if a.id == identifiant)
            except StopIteration:
                print(f"❌ Aucun adhérent avec l'ID {identifiant}.")
                continue

            confirmation = input(f"Confirmez-vous la suppression de {adherent.nom} {adherent.prenom} ? (O/N) : ").strip().upper()
            if confirmation == "O":
                # Vérifie si l'adhérent a des emprunts.
                for emprunt in self.liste_emprunts[:]:  # Créer une copie de la liste pour éviter que des éléments de la liste soient sautés
                    if emprunt.adherent.id == identifiant: # Parcourt la liste copiée
                        self.liste_emprunts.remove(emprunt)  # Supprime les emprunts de l'adhérent dans la liste originale
                    self.liste_adherents.remove(adherent)
                    print(f"Adhérent #{adherent.id} supprimé avec succès.")
                else:
                    print("❌ Suppression annulée.")

            # On demande à l’utilisateur s’il veut supprimer un 2e adhérent ou revenir au menu
            while True:
                while True:
                    choix = input("Voulez-vous supprimer un autre adhérent ? (O/N) : ").strip().upper()
                    if choix in ("O", "N"):
                        break
                    print("❌ Réponse invalide. O ou N.")
                if choix == "N":
                    return


    # Sort de la boucle interne pour revenir au menu principal

# Ajoute un document
    def ajouter_doc(self):
        while True: # boucle interne pour permettre d'ajouter un autre document à la fin de la méthode
            # Saisie de l'utilisateur
            while True: # Boucle qui valide que le champ n'est pas vide
                titre = input("Saisissez le titre du document : ").strip()
                if titre:
                    break
                print("❌ Le titre ne peut pas être vide.")

            while True: # Boucle qui valide que le champ n'est pas vide
                auteur = input("Saisissez l'auteur du document : ").strip()
                if auteur:
                    break
                print("❌ Le champ ne peut pas être vide.")

            while True: # Boucle qui valide que l'ISBN ne contient que des chiffres
                isbn = input("Saisissez l'ISBN du document : ").strip()
                try:
                    valeur = int(isbn)  # essaie de convertir en entier
                    if valeur <= 0:
                        raise ValueError
                    break # Si l'isbn est valide, on sort de la boucle.
                except ValueError:
                    print("❌ ISBN invalide! Veuillez saisir uniquement des chiffres positifs.")
                    continue

            while True: # Boucle qui valide que la quantité est un entier
                try:
                    quantite = int(input("Saisissez la quantité : ").strip())
                    if quantite > 0:
                        break
                    print("❌ La quantité doit être un nombre positif.")
                except ValueError:
                    print("❌ Entrez un nombre entier.")

            # Recherche si un document avec le même titre existe déjà dans la liste de documents
            try:
                doc_existant = next(d for d in self.liste_documents if
                                    d.titre.strip().lower() == titre.lower() and str(d.isbn) == str(isbn))
                # Document trouvé → augmenter quantité
                choix = input(f"⚠️ Document existe. Augmenter quantité ? (O/N) : ").strip().upper()
                if choix == "O":
                    doc_existant.quantite += quantite
                    print(f"✅ Quantité mise à jour : {doc_existant.quantite} exemplaires.")
                else:
                    print("❌ Ajout annulé.")
            except StopIteration:
                nouveau_document = Livre(titre, isbn, quantite, auteur)
                self.liste_documents.append(nouveau_document)
                print(f"✅ {quantite} exemplaires de «{titre}» ajoutés avec succès.")

            # On demande à l’utilisateur s’il veut ajouter un 2e document ou revenir au menu
            while True:
                while True:
                    choix = input("Voulez-vous ajouter un autre adhérent ? (O/N) : ").strip().upper()
                    if choix in ("O", "N"):
                        break
                    print("❌ Réponse invalide. O ou N.")
                if choix == "N":
                    return


# Supprimer un document
    def enlever_doc(self):
        while True:
            Affichage.afficher_liste_docs(self)  # Affiche la liste actuelle des documents
            # Saisie du ISBN par l'utilisateur
            choix_isbn = input("Saisissez l'ISBN du document à supprimer : ").strip()

            # Recherche du document dans la liste
            try:
                document = next(doc for doc in self.liste_documents if doc.isbn == choix_isbn)
            except StopIteration:
                print(f"❌ Aucun document avec le numéro ISBN '{choix_isbn}' trouvé! Réessayez.")
                continue
                # Ici on a trouvé le document, donc on peut le supprimer
            confirmation = input(f"Confirmez-vous la suppression de «{document.titre}» ? (O/N) : ").strip().upper()
            if confirmation == "O":
                # Vérifie s'il y a des emprunts pour ce livre
                for emprunt in self.liste_emprunts[:]: # Créer une copie de la liste pour éviter que des éléments de la liste soient sautés
                    if emprunt.livre.isbn == choix_isbn: # Parcourt la liste copiée
                        self.liste_emprunts.remove(emprunt) # Supprime les emprunts de ce livre dans la liste originale
                self.liste_documents.remove(document)
                print(f"Titre : «{document.titre}» retiré avec succès.")
            else:
                print("❌ Suppression annulée.")

            while True:  # On demande à l’utilisateur s’il veut supprimer un 2e document ou revenir au menu
                while True:
                    choix = input("Voulez-vous supprimer un autre adhérent ? (O/N) : ").strip().upper()
                    if choix in ("O", "N"):
                        break
                    print("❌ Réponse invalide. O ou N.")
                if choix == "N":
                    return