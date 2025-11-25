import re # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
from Document import *
from Adherent import Adherent
import Affichage

class Bibliotheque:

    def __init__(self, nom_bibliotheque):
        self.nom_bibliotheque = nom_bibliotheque
        self.liste_emprunts = []
        self.liste_documents = []
        self.liste_adherents = []

    def __str__(self):
        return self.nom_bibliotheque

    def ajouter_ad(self):
        while True: # boucle interne pour permettre d'ajouter un autre adhérent à la fin de la méthode

            # Saisie de l'utilisateur
            while True:
                #      PERMETTRE LES ESPACES? J'peux pas mettre "De Celles" :(
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
                nouvel_adherent = Adherent(nom,prenom, self)
                self.liste_adherents.append(nouvel_adherent)
                print(f"Adhérent #{nouvel_adherent.id} : {nom}, {prenom} ajouté avec succès.")

            # On demande à l’utilisateur s’il veut ajouter un 2e adhérent ou revenir au menu
            while True:
                choix = input("Voulez-vous ajouter un autre adhérent ? (O/N) : ").strip().upper()
                if choix not in ("O", "N"):
                    print("❌ Sélection invalide! Répondez O ou N.")
                    continue # redemande "Voulez-vous ajouter un autre adhérent ? (O/N) : "
                if choix == "O":
                    break # Laisse la boucle while continuer = permet un nouvel ajout
                if choix == "N":
                    return # Sort de la boucle interne pour revenir au menu principal


    def enlever_ad(self):
        while True: # boucle interne pour permettre de supprimer un autre adhérent à la fin de la méthode
            Affichage.afficher_liste_adherents(self) # Affiche la liste d'adhérents actuels

            # Saisie de l'utilisateur
            try:
                choix_id = input("Saisissez l'ID de l'adhérent à supprimer : ")
                identifiant = int(choix_id)
            except ValueError:
                print("❌ Saisie invalide! Entrez un numéro.")
                continue

            # Recherche l'adhérent dans la liste
            for adherent in self.liste_adherents:
                if adherent.id == identifiant:

                    while True:
                        confirmation = input(  # Confirmation avant la suppression
                        f"Confirmez-vous la suppression de Adhérent #{adherent.id} : {adherent.nom}, {adherent.prenom}» ? (O/N) : ").strip().upper()

                        if confirmation == "O":
                            for emprunt in self.liste_emprunts: # Vérifie si l'adhérent a des emprunts
                                if emprunt.adherent.id == identifiant:
                                    self.liste_emprunts.remove(emprunt) # Supprime les emprunts de l'adhérent
                            self.liste_adherents.remove(adherent)
                            print(f"Adhérent #{adherent.id} : {adherent.nom} {adherent.prenom} retiré avec succès.")
                            break

                        elif confirmation == "N":
                            print("❌ Suppression annulée.")
                            break

                        else:
                            print("❌ Sélection invalide! Répondez O ou N.")
                            continue
                    break

                elif adherent not in self.liste_adherents:
                    print(f"❌ Aucun adhérent trouvé avec l'ID {identifiant}. Réessayez.")

            # On demande à l’utilisateur s’il veut supprimer un 2e adhérent ou revenir au menu
            while True:
                choix = input("Voulez-vous supprimer un autre adhérent ? (O/N) : ").strip().upper()
                if choix not in ("O", "N"):
                    print("❌ Sélection invalide! Répondez O ou N.")
                    continue # redemande "Voulez-vous supprimer un autre adhérent ? (O/N) : "
                if choix == "O":
                    break # Laisse la boucle while continuer = permet une nouvelle suppression
                if choix == "N":
                    return # Sort de la boucle interne pour revenir au menu principal


    def ajouter_doc(self): ############################################################################################# Ajouter type de document? est-ce qu'on permet aussi d'ajouter LES BD, VOLUMES ETC
        while True: # boucle interne pour permettre d'ajouter un autre document à la fin de la méthode
            # Saisie de l'utilisateur

            while True: # Boucle qui valide que le champ n'est pas vide
                titre = input("Saisissez le titre du document : ").strip()
                if not titre:
                    print("❌ Le titre ne peut pas être vide.")
                    continue
                break

            while True: # Boucle qui valide que le champ n'est pas vide
                auteur = input("Saisissez l'auteur du document : ").strip()
                if not auteur:
                    print("❌ Le champ ne peut pas être vide.")
                    continue
                break

            while True: # Boucle qui valide que l'ISBN ne contient que des chiffres
                isbn = input("Saisissez l'ISBN du document : ").strip()
                try:
                    valeur = int(isbn)  # essaie de convertir en entier
                    if valeur <= 0:
                        print("❌ ISBN invalide! L'ISBN doit être un nombre positif.")
                        continue
                    break # Si l'isbn est valide, on sort de la boucle.
                except ValueError:
                    print("❌ ISBN invalide! Veuillez saisir uniquement des chiffres.")
                    continue

            while True: # Boucle qui valide que la quantité est un entier
                quantite = input("Saisissez la quantité : ").strip()
                try:
                    quantite = int(quantite)
                    if quantite <= 0:
                        print("❌ La quantité doit être un nombre positif.")
                    else:
                        break  # Sort de la boucle quand la quantité est valide
                except ValueError:
                    print("❌ Quantité invalide! Veuillez saisir un nombre entier.")

            # Recherche si un document avec le même titre existe déjà dans la liste de documents
            doublon = False
            doc_existant = None
            for doc in self.liste_documents:
                if doc.titre.strip().lower() == titre.lower() and str(doc.isbn) == str(isbn):
                    doublon = True
                    doc_existant = doc
                    break

            if doublon :
                while True:
                    choix = input(f"⚠️ Ce document existe déjà dans la bibliothèque. Voulez-vous augmenter sa quantité? (O/N)").strip().upper()
                    if choix not in ("O", "N"):
                        print("❌ Sélection invalide! Répondez O ou N.")
                        continue  # redemande "Voulez-vous augmenter sa quantité? (O/N) "
                    if choix == "O":
                       doc_existant.quantite += quantite
                       print(f"Quantité mise à jour avec succès! Quantité disponible pour «{doc_existant.titre}» : {doc_existant.quantite}")
                       break
                    elif choix == "N":
                        print("❌ Ajout de document annulé.")
                        break
            else: # Si aucun doublon, on crée le nouveau document + on l'ajoute à la liste de docs
                nouveau_document = Livre(titre,isbn,quantite,auteur)
                self.liste_documents.append(nouveau_document)
                print(f"{quantite} exemplaires du document «{titre}» écrit par {auteur} ajoutés avec succès.")

            # On demande à l’utilisateur s’il veut ajouter un 2e document ou revenir au menu
            while True:
                choix = input("Voulez-vous ajouter un autre document ? (O/N) : ").strip().upper()
                if choix not in ("O", "N"):
                    print("❌ Sélection invalide! Répondez O ou N.")
                    continue # redemande "Voulez-vous ajouter un autre document ? (O/N) : "
                elif choix == "O":
                    break # Laisse la boucle while continuer = permet un nouvel ajout
                elif choix == "N":
                    return # Sort de la boucle interne pour revenir au menu principal

    def enlever_doc(self):
        while True:
            Affichage.afficher_liste_docs(self)  # Affiche la liste actuelle des documents

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
                    else:
                        print("❌ Suppression annulée.")

                    trouve = True
                    break
            if not trouve:
                print(f"❌ Aucun document avec le numéro ISBN '{choix_document}' trouvé! Réessayez.")

            # On demande à l’utilisateur s’il veut supprimer un 2e document ou revenir au menu
            while True:
                choix = input("Voulez-vous supprimer un autre document ? (O/N) : ").strip().upper()
                if choix not in ("O", "N"):
                    print("❌ Sélection invalide! Répondez O ou N.")
                    continue # redemande "Voulez-vous supprimer un autre document ? (O/N) : "
                if choix == "O":
                    break # Laisse la boucle while continuer = permet une nouvelle suppression
                if choix == "N":
                    return # Sort de la boucle interne pour revenir au menu principal
            else:
                break # Sort de la boucle interne pour revenir au menu principal

