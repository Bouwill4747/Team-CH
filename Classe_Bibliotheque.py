import csv
import re # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
from Classe_Document import *
from Classe_Adherent import Adherent
from Classe_Emprunt import Emprunt

class Bibliotheque:

    def __init__(self, nom_bibliotheque):
        self.nom_bibliotheque = nom_bibliotheque
        self.liste_emprunts = []
        self.liste_documents = []
        self.liste_adherents = []
        self.importer_docs() # Importe automatiquement les documents quand la bibliothèque est créée
        self.importer_adherents() # Importe automatiquement les adhérents quand la bibliothèque est créée
        self.importer_emprunts() # Importe automatiquement les emprunts quand la bibliothèque est créée

    def __str__(self):
        return self.nom_bibliotheque

# Importe et crée une liste de documents avec attributs : titre, isbn, quantite, auteur
    def importer_docs(self):
        try:
            with open("livres.csv", "r", encoding="utf-8") as fichier:

                lignes = fichier.readlines()
                del lignes[0] # Supprime la première ligne (qui est les noms de colonne)

                for ligne in lignes:

                    ligne = ligne.strip() # Supprime "\n" à la fin de chaque ligne
                    e = ligne.split(",")
                    titre = e[0]
                    isbn = e[1]
                    quantite = int(e[2])
                    auteur = e[3]
                    nouveau_doc = Livre(titre, isbn, quantite, auteur)
                    self.liste_documents.append(nouveau_doc)

        except FileNotFoundError:
            print("Erreur : Le fichier n'existe pas.")

# Importe et crée une liste d'adhérents avec les attributs : nom, prenom, id_adherent
    def importer_adherents(self):
        try:
            with open("adherents.csv", "r", encoding="utf-8") as fichier:
                lignes = fichier.readlines()
                del lignes[0] # Supprime la première ligne (qui est les noms de colonne)
                for ligne in lignes:
                    ligne = ligne.strip() # Supprime "\n" à la fin de chaque ligne
                    e = ligne.split(",")
                    id = int(e[0])
                    nom = e[1]
                    prenom = e[2]
                    nouvel_adherent = Adherent(nom, prenom, id)
                    self.liste_adherents.append(nouvel_adherent)

        except FileNotFoundError:
            print("Erreur : Le fichier n'existe pas.")

# Importe et crée une liste d'emprunts avec les attributs : (à voir)
    def importer_emprunts(self):
        try:
            with open("emprunts.csv", "r", encoding="utf-8") as fichier:
                lignes = fichier.readlines()
                del lignes[0]  # Supprime la première ligne (qui est les noms de colonne)
                for ligne in lignes:

                    ligne = ligne.strip()  # Supprime "\n" à la fin de chaque ligne
                    e = ligne.split(",")
                    id = int(e[0])
                    isbn = e[2]
                    for x in self.liste_adherents:
                        if x.id == id:
                            adherent = x
                    for x in self.liste_documents:
                        if x.isbn == isbn:
                            livre = x
                    nouvel_emprunt = Emprunt(adherent, self, livre)
                    self.liste_emprunts.append(nouvel_emprunt)

        except FileNotFoundError:
            print("Erreur : Le fichier n'existe pas.")


    def afficher_liste_docs(self):
        print("============================================================")
        print("                  Liste des documents                       ")
        print("============================================================")

        for doc in self.liste_documents:
            dash_line = '-' * (len(doc.titre) + 4)
            print(f"\n |{dash_line}|\n"
                  f" |  {doc.titre}  |\n"
                  f" |{dash_line}|\n"
                  f"Titre : «{doc.titre}» | Auteur : {doc.auteur} | Quantité : {str(doc.quantite)} | ISBN : {doc.isbn}\n")


# Affiche la liste complète des adhérents
    def afficher_liste_adherents(self):
        print("============================================================")
        print("                  Liste des adhérents                       ")
        print("============================================================")

        for adherent in self.liste_adherents:
            print(f"Nom : {adherent.nom} | Prénom : {str(adherent.prenom)} | ID de l'adhérent : {adherent.id}\n")


    def afficher_liste_emprunts(self):
        print("============================================================")
        print("                  Liste d'emprunts                          ")
        print("============================================================")

        for emprunt in self.liste_emprunts:
            print(f"{emprunt.adherent.prenom} {emprunt.adherent.nom} a emprunté «{emprunt.livre.titre}» ({emprunt.livre.isbn}) le {emprunt.date_emprunt}. ID d'emprunt : {emprunt.id_emprunt}\n")

    def ajouter_ad(self):
        while True: # boucle interne pour permettre d'ajouter un autre adhérent à la fin de la méthode

            # Saisie de l'utilisateur
            while True:
                nom = input("Saisissez le nom de l'adhérent : ").strip()
                if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\-]+$", nom): # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
                    print("❌ Le nom ne peut contenir que des lettres et éventuellement un tiret. Réessayez.")
                else:
                    break
            while True:
                prenom = input("Saisissez le prénom de l'adhérent : ").strip()
                if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\-]+$", prenom): # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
                    print("❌ Le prénom ne peut contenir que des lettres et éventuellement un tiret. \n Réessayez...")
                else:
                    break

            # Recherche si le nom et prénom se retrouvent déjà dans la liste d'adhérents
            doublon = False
            for adherent in self.liste_adherents:
                    if adherent.nom.strip().lower() == nom.lower() and adherent.prenom.strip().lower() == prenom.lower():
                        doublon = True
                        break

            if doublon :
                print(f"❌ L'adhérent {nom}, {prenom} existe déjà. Ajout annulé.")

            else:
                # Classer les adhérents avec un numéro devant
                dictionnaire_adherents = {}
                id = 1
                for adherent in self.liste_adherents:
                    dictionnaire_adherents[id] = adherent
                    id += 1
                nouvel_adherent = Adherent(nom,prenom,id)
                self.liste_adherents.append(nouvel_adherent)
                print(f"Adhérent #{id} : {nom}, {prenom} ajouté avec succès.")

            # On demande à l’utilisateur s’il veut ajouter un 2e adhérent ou revenir au menu
            while True:
                choix = input("Voulez-vous ajouter un autre adhérent ? (O/N) : ")
                if choix.strip().upper() not in ("O", "N"):
                    print("❌ Sélection invalide.")
                    continue # redemande "Voulez-vous ajouter un autre adhérent ? (O/N) : "
                if choix.strip().upper() == "O":
                    break # Laisse la boucle while continuer = permet un nouvel ajout
                if choix.strip().upper() == "N":
                    return # Sort de la boucle interne pour revenir au menu principal


    def enlever_ad(self):
        while True: # boucle interne pour permettre de supprimer un autre adhérent à la fin de la méthode
            self.afficher_liste_adherents() # Affiche la liste d'adhérents actuels

            # Saisie de l'utilisateur
            try:
                choix_id = input("Saisissez l'ID de l'adhérent à supprimer : ")
                identifiant = int(choix_id)
            except ValueError:
                print("❌ Saisie invalide. Entrez un numéro.")
                continue

            # Recherche l'adhérent dans la liste
            for adherent in self.liste_adherents:
                if adherent.id == identifiant:
                    confirmation = input(  # Confirmation avant la suppression
                    f"Confirmez-vous la suppression de Adhérent #{adherent.id} : {adherent.nom}, {adherent.prenom}» ? (O/N) : ").strip().upper()
                    if confirmation == "O":
                        for emprunt in self.liste_emprunts: # Vérifie si l'adhérent a des emprunts
                            if emprunt.adherent.id == identifiant:
                                self.liste_emprunts.remove(emprunt) # Supprime les emprunts de l'adhérent
                    self.liste_adherents.remove(adherent)
                    print(f"Adhérent #{adherent.id} : {adherent.nom} {adherent.prenom} retiré avec succès.")
                    break
            else:
                print(f"❌ Aucun adhérent trouvé avec l'ID {identifiant}. Réessayez.")

            # On demande à l’utilisateur s’il veut supprimer un 2e adhérent ou revenir au menu
            while True:
                choix = input("Voulez-vous supprimer un autre adhérent ? (O/N) : ")
                if choix.strip().upper() not in ("O", "N"):
                    print("❌ Sélection invalide.")
                    continue # redemande "Voulez-vous supprimer un autre adhérent ? (O/N) : "
                if choix.strip().upper() == "O":
                    break # Laisse la boucle while continuer = permet une nouvelle suppression
                if choix.strip().upper() == "N":
                    return # Sort de la boucle interne pour revenir au menu principal


    def ajouter_doc(self): ############################################################################################# Ajouter type de document? est-ce qu'on permet aussi d'ajouter LES BD, VOLUMES ETC
        while True: # boucle interne pour permettre d'ajouter un autre document à la fin de la méthode
            # Saisie de l'utilisateur
            titre = input("Saisissez le titre du document : ").strip()
            auteur = input("Saisissez l'auteur du document : ").strip()
            isbn = input("Saisissez l'ISBN du document : ").strip()

            # Boucle qui valide que la quantité est un entier
            while True:
                quantite = input("Saisissez la quantité : ").strip()
                try:
                    quantite = int(quantite)
                    if quantite <= 0:
                        print("❌ La quantité doit être un nombre positif.")
                    else:
                        break  # Sort de la boucle quand la quantité est valide
                except ValueError:
                    print("❌ Quantité invalide. Veuillez saisir un nombre entier.")

            # Recherche si un document avec le même titre existe déjà dans la liste de documents
            doublon = False
            doc_existant = None
            for doc in self.liste_documents:
                if doc.titre.strip().lower() == titre.lower() or doc.isbn == isbn:
                    doublon = True
                    doc_existant = doc
                    break

            if doublon :
                choix = input(f"⚠️ Ce document existe déjà dans la bibliothèque. Voulez-vous augmenter sa quantité? (oui/non")
                if choix.strip().lower() == "oui": # Augmenter la quantité du document existant ****** À revoir *****
                   doc_existant.quantite += quantite
                   print(f"Quantité mise à jour : {doc_existant.quantite}x «{doc_existant.titre}»")
                else:
                    break  # Laisse la boucle while continuer = permet l'ajout d'un nouveau doc
            else: # Si aucun doublon, on crée le nouveau document + on l'ajoute à la liste de docs
                nouveau_document = Livre(titre,isbn,quantite,auteur)
                self.liste_documents.append(nouveau_document)
                print(f"{quantite}x «{titre}» de {auteur} ajouté avec succès.")

            # On demande à l’utilisateur s’il veut ajouter un 2e document ou revenir au menu
            while True:
                choix = input("Voulez-vous ajouter un autre document ? (O/N) : ")
                if choix.strip().upper() not in ("O", "N"):
                    print("❌ Sélection invalide.")
                    continue # redemande "Voulez-vous ajouter un autre document ? (O/N) : "
                if choix.strip().upper() == "O":
                    break # Laisse la boucle while continuer = permet un nouvel ajout
                if choix.strip().upper() == "N":
                    return # Sort de la boucle interne pour revenir au menu principal

######################################################################################################################### est-ce qu'on ajoute "si vous ne connaissez pas son ISBN, saisissez le titre du document"?
    def enlever_doc(self):
        while True:
            self.afficher_liste_docs()  # Affiche la liste actuelle des documents

            # Saisie du ISBN par l'utilisateur
            choix_document = input("Saisissez l'ISBN du document à supprimer : ").strip()

            # Recherche du document dans la liste
            trouve = False
            for document in self.liste_documents:
                if document.isbn == choix_document:
                    confirmation = input( # Confirmation avant la suppression
                        f"Confirmez-vous la suppression de «{document.titre}» ? (O/N) : ").strip().upper()
                    if confirmation == "O":
                        self.liste_documents.remove(document)
                        print(
                            f"Titre : «{document.titre}» | Auteur : {document.auteur} | ISBN : {document.isbn} retiré avec succès.")
                        trouve = True
                    else:
                        print("❌ Suppression annulée.")

                    trouve = True
                    break
            if not trouve:
                print(f"❌ Aucun document avec le numéro ISBN '{choix_document}' trouvé. Réessayez.")

            # On demande à l’utilisateur s’il veut supprimer un 2e document ou revenir au menu
            while True:
                choix = input("Voulez-vous supprimer un autre document ? (O/N) : ")
                if choix.strip().upper() not in ("O", "N"):
                    print("❌ Sélection invalide.")
                    continue # redemande "Voulez-vous supprimer un autre document ? (O/N) : "
                if choix.strip().upper() == "O":
                    break # Laisse la boucle while continuer = permet une nouvelle suppression
                if choix.strip().upper() == "N":
                    return # Sort de la boucle interne pour revenir au menu principal
            choix = input("Voulez-vous supprimer un autre document ? (O/N) : ")
            if choix.strip().upper() == "O":
                continue # Laisse la boucle while continuer = permet une nouvelle suppression
            else:
                break # Sort de la boucle interne pour revenir au menu principal


    def sauvegarder_livres(self, chemin_fichier):
        with open(chemin_fichier, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Titre", "Auteur", "ISBN", "Quantité disponible", "Quantité totale"])

            for livre in self.liste_documents:
                writer.writerow([
                    livre.titre,
                    livre.auteur,
                    livre.isbn,
                    livre.qte_dispo,
                    livre.quantite
                ])
