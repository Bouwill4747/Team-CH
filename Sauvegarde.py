import csv
from Document import Livre
from Adherent import Adherent
from Emprunt import Emprunt

# Importe et crée une liste de documents avec attributs : titre, isbn, quantite, auteur
def importer_documents(biblio):
    try:
        # Le fichier sera fermé automatiquement une fois que la boucle with terminera
        with open("livres.csv", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            del lignes[0]  # Supprime la première ligne (qui est les noms de colonne)
            for ligne in lignes:
                ligne = ligne.strip()  # Supprime "\n" à la fin de chaque ligne
                e = ligne.split(",")
                titre = e[0]
                auteur = e[1]
                isbn = e[2]
                quantite = int(e[4])  # Quantité totale (dernière colonne)
                # Note: e[3] contient quantité disponible si besoin

                nouveau_doc = Livre(titre, isbn, quantite, auteur)
                biblio.liste_documents.append(nouveau_doc)

    except FileNotFoundError:
        print("Erreur : le fichier n'existe pas.")

# Importe et crée une liste d'adhérents avec les attributs : nom, prenom, id_adherent
def importer_adherents(biblio):
    try:
        with open("adherents_import.csv", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            del lignes[0]  # Supprime la première ligne (qui est les noms de colonne)
            for ligne in lignes:
                ligne = ligne.strip()  # Supprime "\n" à la fin de chaque ligne
                e = ligne.split(",")
                prenom = e[0]
                nom = e[1]

                nouvel_adherent = Adherent(nom, prenom, biblio)
                biblio.liste_adherents.append(nouvel_adherent)

    except FileNotFoundError:
        print("Erreur : Le fichier n'existe pas.")

# Importe et crée une liste d'emprunts avec les attributs : (à voir)
def importer_emprunts(biblio):
    try:
        with open("emprunts_import.csv", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()
            del lignes[0]  # Supprime la première ligne (qui est les noms de colonne)
            for ligne in lignes:
                ligne = ligne.strip()  # Supprime "\n" à la fin de chaque ligne
                e = ligne.split(",")
                id_adherent = int(e[0])  # ID d'adhérent
                isbn = e[1]  # ISBN

                # Trouver l'adhérent correspondant
                adherent = None
                for x in biblio.liste_adherents:
                    if x.id == id_adherent:
                        adherent = x
                        break

                # Trouver le livre correspondant
                livre = None
                for x in biblio.liste_documents:
                    if x.isbn == isbn:
                        livre = x
                        break

                # Créer l'emprunt seulement si l'adhérent et le livre existent
                if adherent and livre:
                    nouvel_emprunt = Emprunt(adherent, livre)
                    biblio.liste_emprunts.append(nouvel_emprunt)

    except FileNotFoundError:
        print("Erreur : Le fichier n'existe pas.")


def sauvegarder_livres(biblio):
    with open("livres.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Titre", "Auteur", "ISBN", "Quantité disponible", "Quantité totale"])

        for livre in biblio.liste_documents:
            writer.writerow([
                livre.titre,
                livre.auteur,
                livre.isbn,
                livre.qte_dispo,
                livre.quantite
            ])


def sauvegarder_adherents(biblio):
    with open("adherents.csv", "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Prénom", "Nom", "ID"])

        for adherent in biblio.liste_adherents:
            writer.writerow([
                adherent.prenom,
                adherent.nom,
                adherent.id
            ])


def sauvegarder_emprunts(biblio):
    with open("emprunts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Adhérent", "ID d'adhérent", "Titre du livre", "ISBN", "Date d'emprunt", "Date de retour"])

        for emprunt in biblio.liste_emprunts:
            writer.writerow([
                emprunt.adherent.prenom + " " + emprunt.adherent.nom,
                emprunt.adherent.id,
                emprunt.livre.titre,
                emprunt.livre.isbn,
                emprunt.date_emprunt,
                emprunt.date_retour
            ])