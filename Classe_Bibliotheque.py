from Classe_Document import *
from Classe_Adherent import Adherent

class Bibliotheque:

    def __init__(self, nomBibliotheque):
        self.nomBibliotheque = nomBibliotheque
        # Au lieu que, comme avant, liste_documents soit une variable isolée qu'on doive "return" pour la rendre
        # accessible, maintenant c'est un attribut de la bibliothèque qui peut être accédé de partout (tant que
        # la bibliothèque est fournie en tant qu'input, ou dans le "main" où elle sera créée).
        self.liste_documents = []
        self.liste_adherents = []
        self.liste_emprunts = [] # À voir si on en aura réellement besoin
        self.importer_docs() # Importe automatiquement les documents quand la bibliothèque est créée
        self.importer_adherents() # Importe automatiquement les adhérents quand la bibliothèque est créée
        self.importer_emprunts() # Importe automatiquement les emprunts quand la bibliothèque est créée

    def __str__(self):
        return self.nomBibliotheque

    # def livre_existe(self, titre: str):
    #     for x in self.liste_documents:
    #         if x.titre == titre: # Reste à rendre ça case insensitive
    #             return True
    #     return False


# Importe et crée une liste de documents avec attributs : titre, isbn, quantite, auteur
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
                    nouveau_doc = Livre(titre, isbn, quantite, auteur)
                    self.liste_documents.append(nouveau_doc)

        except FileNotFoundError:
            print("❌ Erreur : Le fichier n'existe pas.")


# Importe et crée une liste d'adhérents avec les attributs : nom, prenom, no_adherent
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


# Importe et crée une liste d'emprunts avec les attributs : (à voir)
    # def importer_emprunts(self): # ID_Adherent,Nom,Titre_Livre,ISBN : (à voir quand la classe emprunts sera faite)
    #     try:
    #         with open("Emprunts1.csv", "r", encoding="utf-8") as fichier:
    #             lignes = fichier.readlines()
    #             del lignes[0] # Supprime la première ligne (qui est les noms de colonne)
    #
    #        for ligne in lignes:
    #                ligne = ligne.strip()  # Supprime "\n" à la fin de chaque ligne
    #               e = ligne.split(",")
    #                no_adherent = int(e[0])
    #                nom = e[1]
    #                prenom = e[2]
    #                nouvel_adherent = Adherent(nom, prenom, no_adherent)
    #                self.liste_adherents.append(nouvel_adherent)


# Affiche la liste complète des documents
    def afficher_liste_docs(self):
        print("============================================================")
        print("                  Liste des documents                       ")
        print("============================================================")

        for doc in self.liste_documents:
            dash_line = '-' * (len(doc.titre) + 4)
            print(f"\n |{dash_line}|\n"
                  f" |  {doc.titre}  |\n"
                  f" |{dash_line}|\n"
                  f"Titre : {doc.titre} | Auteur : {doc.auteur} | Quantité : {str(doc.quantite)} | ISBN : {doc.isbn}\n")


# Affiche la liste complète des adhérents
    def afficher_liste_adherents(self):
        print("============================================================")
        print("                  Liste des adhérents                       ")
        print("============================================================")

        for adherent in self.liste_adherents:
            print(f"Nom : {adherent.nom} | Prénom : {str(adherent.prenom)} | # d'adhérent : {adherent.no_adherent}\n")


    def afficher_liste_emprunts(self):

        print("============================================================")
        print("                  Liste d'emprunts                          ")
        print("============================================================")

        # for emprunt in self.liste_emprunts:  # À faire quand la classe emprunts sera complétée
        #     dash_line = '-' * (len(emprunt.titre) + 4)
        #     print(f"\n |{dash_line}|\n"
        #           f" |  {doc.titre}  |\n"
        #           f" |{dash_line}|\n"
        #           f"Titre : {doc.auteur} | Quantité : {str(doc.quantite)} | ISBN : {doc.isbn}\n")


    def ajouter_ad(self):
        while True: # boucle interne pour permettre d'ajouter un autre adhérent à la fin de la méthode

        # Saisie de l'utilisateur
            nom = input("Saisissez le nom de l'adhérent : ").strip()
            prenom = input("Saisissez le prénom de l'adhérent : ").strip()

        # Recherche si le nom et prénom se retrouvent déjà dans la liste d'adhérents
            doublon = False
            for adherent in self.liste_adherents:
                    if adherent.nom.strip().lower() == nom.lower() and adherent.prenom.strip().lower() == prenom.lower():
                        doublon = True
                        break

            if doublon :
                print(f"L'adhérent {nom}, {prenom} existe déjà. Ajout annulé.")

            else:
                # faire un compteur +1 chq adhérent.
                if self.liste_adherents:
                    max_numero = max(adherent.no_adherent for adherent in self.liste_adherents)
                else:
                    max_numero = 0
                no_adherent = max_numero + 1
                nouvel_adherent = Adherent(nom,prenom,no_adherent)
                self.liste_adherents.append(nouvel_adherent)
                print(f"Adhérent #{no_adherent} : {nom}, {prenom} ajouté avec succès.")

            # On demande à l’utilisateur s’il veut ajouter un 2e adhérent ou revenir au menu
            choix = input("Voulez-vous ajouter un autre adhérent ? (O = oui / N = non : retour au menu) : ")
            if choix.strip().upper() == "O":
                continue # Laisse la boucle while continuer = permet une nouvelle suppression
            else:
                break # Sort de la boucle interne pour revenir au menu principal


    def enlever_ad(self):
        while True: # boucle interne pour permettre de supprimer un autre adhérent à la fin de la méthode
            self.afficher_liste_adherents() # Affiche la liste d'adhérents actuels

            # Saisie de l'utilisateur
            try:
                choix_id = input("Saisissez l'identifiant de l'adhérent à supprimer : ")
                identifiant = int(choix_id)
            except ValueError:
                print("Saisie invalide. Entrez un numéro d'adhérent valide.")
                continue

            # Recherche l'adhérent dans la liste
            trouve = None
            for adherent in self.liste_adherents:
                if adherent.no_adherent == identifiant:
                    trouve = adherent
            if trouve:
                self.liste_adherents.remove(trouve)
                print(f"✅ Adhérent #{trouve.no_adherent} : {trouve.nom_adherent} {trouve.prenom_adherent} retiré avec succès.")
            else:
                print(f"Aucun adhérent trouvé avec l'identifiant {identifiant}. Réessayez.")

            # On demande à l’utilisateur s’il veut supprimer un 2e adhérent ou revenir au menu
            choix = input("Voulez-vous supprimer un autre adhérent ? (O = oui / N = non : retour au menu) : ")
            if choix.strip().upper() == "O":
                continue # Laisse la boucle while continuer = permet une nouvelle suppression
            else:
                break # Sort de la boucle interne pour revenir au menu principal


    def ajouter_doc(self):
        while True: # boucle interne pour permettre d'ajouter un autre document à la fin de la méthode
            # Saisie de l'utilisateur
            titre = input("Saisissez le titre du document : ").strip() # strip retire les espaces superflus
            auteur = input("Saisissez l'auteur du document : ").strip()
            isbn = input("Saisissez l'ISBN du document : ").strip()
            quantite = input("Saisissez la quantité : ").strip()

            # Vérifier que la quantité est un entier
            try:
                quantite = int(quantite)
                if quantite <= 0:
                    print("❌ La quantité doit être un nombre positif.")
                    continue
            except ValueError:
                print("❌ Quantité invalide. Veuillez saisir un nombre entier.")
                continue

            # Recherche si un document avec le même titre existe déjà dans la liste de documents
            doublon = False
            doc_existant = None
            for doc in self.liste_documents:
                if doc.titre.strip().lower() == titre.lower() or doc.isbn == isbn:
                    doublon = True
                    doc_existant = doc
                    break

            if doublon :
                choix = input(f"Ce document existe déjà dans la bibliothèque. Voulez-vous augmenter sa quantité? (oui/non")
                if choix.strip().lower() == "oui": # Augmenter la quantité du document existant ****** À revoir *****
                   doc_existant.quantite += quantite
                   print(f"✅ Quantité mise à jour : {doc_existant.quantite}x {doc_existant.titre}")
                else:
                    continue  # Laisse la boucle while continuer = permet l'ajout d'un nouveau doc
            else: # Si aucun doublon, on crée le nouveau document + on l'ajoute à la liste de docs
                nouveau_document = Livre(titre,isbn,quantite,auteur)
                self.liste_documents.append(nouveau_document)
                print(f"{quantite}x «{titre}» de {auteur} ajouté avec succès.")

            # On demande à l’utilisateur s’il veut ajouter un 2e adhérent ou revenir au menu
            choix2 = input("Voulez-vous ajouter un autre adhérent ? (oui/non) : ")
            if choix2.strip().lower() == "oui":
                if choix2.strip().lower() != "oui":
                    break

######## Ajouter si vous ne connaissez pas son ISBN, saisissez le titre du document ? ##########
    def enlever_doc(self):
        while True:
            self.afficher_liste_docs()  # Affiche la liste actuelle des documents

            # Saisie du ISBN par l'utilisateur
            try:
                choix_document = input("Saisissez l'ISBN du document à supprimer : ")
                isbn = int(choix_document)
            except ValueError:
                print("Saisie invalide. Entrez un numéro ISBN valide.")
                continue

            # Recherche du document dans la liste
            trouve = None
            for document in self.liste_documents:
                if document.isbn == isbn:
                    trouve = isbn
                if trouve:
                    self.liste_documents.remove(document)
                    print(f"✅ Titre : {document.titre} | Quantité : {str(document.auteur)} | ISBN : {document.isbn} retiré avec succès.")
                else:
                    print(f"Aucun adhérent avec le numéro {isbn} trouvé. Réessayez.")

            # On demande à l’utilisateur s’il veut supprimer un 2e document ou revenir au menu
            choix = input("Voulez-vous supprimer un autre document ? (O = oui / N = non : retour au menu) : ")
            if choix.strip().upper() == "O":
                continue # Laisse la boucle while continuer = permet une nouvelle suppression
            else:
                break # Sort de la boucle interne pour revenir au menu principal