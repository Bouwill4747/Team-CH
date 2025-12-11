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

# Ajouter un adhérent
    def ajouter_ad(self):
        while True: # boucle interne pour permettre d'ajouter un autre adhérent à la fin de la méthode

            # Saisie de l'utilisateur
            while True:
                nom = input("Saisissez le nom de l'adhérent : ").strip()
                if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\- ]+$", nom): # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
                    print("❌ Le nom ne peut contenir que des lettres et des tirets!")
                else:
                    break
            while True:
                prenom = input("Saisissez le prénom de l'adhérent : ").strip()
                if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\- ]+$", prenom): # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
                    print("❌ Le prénom ne peut contenir que des lettres et des tirets!")
                else:
                    break

            # Recherche si le nom et prénom se retrouvent déjà dans la liste d'adhérents
            try:
                doublon = next(a for a in self.liste_adherents
                               if a.nom.strip().lower() == nom.lower() and a.prenom.strip().lower() == prenom.lower())
                print(f"❌ L'adhérent {nom} {prenom} existe déjà! Ajout annulé.")
                print("-" * 60)
            except StopIteration:
                nouvel_adherent = Adherent(nom, prenom, self)
                self.liste_adherents.append(nouvel_adherent)
                print(f"✅ Adhérent #{nouvel_adherent.id} : {nom} {prenom} ajouté avec succès.")
                print("-" * 60)

            # On demande à l’utilisateur s’il veut ajouter un 2e adhérent ou revenir au menu
            while True:
                choix = input("Voulez-vous ajouter un autre adhérent ? (O/N) : ").strip().upper()
                if choix in ("O", "N"):
                      break
                print("❌ Réponse invalide! Veuillez inscrire O ou N.")
            if choix == "N":
                return

# Supprimer un adhérent
    def enlever_ad(self):
        while True: #  boucle interne pour permettre de supprimer un autre adhérent à la fin de la méthode
            while True: # boucle de saisie de l'utilisateur
                try:
                    identifiant = int(input("Saisissez l'ID de l'adhérent à supprimer : "))
                except ValueError:
                    print("❌ Aucun adhérent trouvé avec cet ID!")
                    continue

                # Recherche l'adhérent dans la liste
                adherent = next((a for a in self.liste_adherents if a.id == identifiant),None)
                if not adherent:
                    print("❌ Aucun adhérent trouvé avec cet ID!")
                    continue

                break

            while True: # Boucle qui permet de confirmer la suppression
                confirmation = input(
                    f"Confirmez-vous la suppression de {adherent.nom} {adherent.prenom} ? (O/N) : "
                ).strip().upper()

                if confirmation == "O":
                    # Vérifie si l'adhérent a des emprunts.
                    for emprunt in self.liste_emprunts[:]: # Créer une copie de la liste pour éviter que des éléments de la liste soient sautés
                        if emprunt.adherent.id == identifiant: # Parcourt la liste copiée
                            self.liste_emprunts.remove(emprunt) # Supprime les emprunts de l'adhérent dans la liste originale

                    self.liste_adherents.remove(adherent)
                    print(f"✅ Adhérent #{adherent.id} supprimé avec succès.")
                    print("-" * 60)
                    break  # on sort du while de confirmation

                elif confirmation == "N":
                    print("❌ Suppression annulée.")
                    break  # on sort du while de confirmation

                else:
                    print("❌ Réponse invalide! Veuillez inscrire O ou N.")
                    continue

            while True:
                choix = input("Voulez-vous supprimer un autre adhérent ? (O/N) : ").strip().upper()
                if choix in ("O", "N"):
                    break
                print("❌ Réponse invalide! Veuillez inscrire O ou N.")

            if choix == "N":
                return

# Ajoute un document
    def ajouter_doc(self):
        while True: # boucle interne pour permettre d'ajouter un autre document à la fin de la méthode
            # Saisie de l'utilisateur
            while True: # Boucle qui valide que le champ n'est pas vide
                titre = input("Saisissez le titre du document : ").strip()
                if titre:
                    break
                print("❌ Le titre ne peut pas être vide!")

            while True: # Boucle qui valide que le champ n'est pas vide
                auteur = input("Saisissez l'auteur du document : ").strip()
                if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\- ]+$", auteur): # Pour accepter l'input d'accents et de tirets dans les noms d'adhérents
                    print("❌ Le nom ne peut contenir que des lettres et des tirets!")
                else:
                    break

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

            # Recherche si un document avec le même titre ou isbn existe déjà dans la liste de documents
            try:
                print("-" * 60)
                doc_existant = next(d for d in self.liste_documents if
                                    d.titre.strip().lower() == titre.lower() or str(d.isbn) == str(isbn))
                # Document trouvé → augmenter quantité
                choix = input(f"⚠️ Document existe. Augmenter quantité ? (O/N) : ").strip().upper()
                if choix == "O":
                    doc_existant.quantite += quantite
                    print(f"✅ Quantité mise à jour : {doc_existant.quantite} exemplaires.")
                    print("-" * 60)
                else:
                    print("❌ Ajout annulé.")
            except StopIteration:
                nouveau_document = Livre(titre, isbn, quantite, auteur)
                self.liste_documents.append(nouveau_document)
                print(f"✅ {quantite} exemplaires de «{titre}» ajoutés avec succès.")
                print("-" * 60)

            # On demande à l’utilisateur s’il veut ajouter un 2e document ou revenir au menu
            while True:
                choix = input("Voulez-vous ajouter un autre document ? (O/N) : ").strip().upper()
                if choix in ("O", "N"):
                      break
                print("❌ Réponse invalide! Veuillez inscrire O ou N.")
            if choix == "N":
                return


# Supprimer un document
    def enlever_doc(self):
        while True:
            # Saisie du ISBN par l'utilisateur
            choix_isbn = input("Saisissez l'ISBN du document à supprimer : ").strip()

            # Recherche du document dans la liste
            document = next((doc for doc in self.liste_documents if doc.isbn == choix_isbn), None)
            if not document:
                print(f"❌ Aucun document avec le numéro ISBN '{choix_isbn}' trouvé!")
                continue

            # Boucle pour confirmer la suppression
            while True:
                confirmation = input(f"Confirmez-vous la suppression de «{document.titre}» ? (O/N) : ").strip().upper()
                if confirmation == "O":
                # Vérifie s'il y a des emprunts pour ce livre
                    for emprunt in self.liste_emprunts[:]: # Créer une copie de la liste pour éviter que des éléments de la liste soient sautés
                        if emprunt.livre.isbn == choix_isbn: # Parcourt la liste copiée
                            self.liste_emprunts.remove(emprunt) # Supprime les emprunts de ce livre dans la liste originale
                # Suppression du document
                    self.liste_documents.remove(document)
                    print(f"✅ Titre : «{document.titre}» retiré avec succès.")
                    print("-" * 60)
                    break

                elif confirmation == "N":
                    print("❌ Suppression annulée.")
                    break

                else:
                    print("❌ Réponse invalide! Veuillez inscrire O ou N.")

            # On demande à l’utilisateur s’il veut supprimer un 2e document ou revenir au menu
            while True:
                choix = input("Voulez-vous supprimer un autre document ? (O/N) : ").strip().upper()
                if choix in ("O", "N"):
                      break
                print("❌ Réponse invalide! Veuillez inscrire O ou N.")
            if choix == "N":
                return