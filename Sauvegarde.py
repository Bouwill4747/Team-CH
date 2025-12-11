import csv
from Document import Livre
from Adherent import Adherent
from Emprunt import Emprunt

# Importe et crée une liste de documents avec attributs : titre, isbn, quantite, auteur
def importer_documents(biblio):
    try:
        with open("livres.csv", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()[1:]  # Supprime la première ligne (en-tête)
            for ligne in lignes:
                e = ligne.strip().split(",")
                titre, isbn, quantite, auteur = e[0], e[2], int(e[4]), e[1]
                biblio.liste_documents.append(Livre(titre, isbn, quantite, auteur))
    except FileNotFoundError:
        print("Erreur : Le fichier livres.csv n'existe pas.")

# Importe et crée une liste d'adhérents avec les attributs : nom, prenom, id_adherent
def importer_adherents(biblio):
    try:
        with open("adherents.csv", "r", encoding="utf-8") as fichier:
            next(fichier)  # Saute la ligne d'en-tête "prenom,nom,id"
            for ligne in fichier:
                prenom, nom, id = ligne.strip().split(",")
                biblio.liste_adherents.append(Adherent(nom, prenom, biblio, int(id)))
    except FileNotFoundError:
        print("Erreur : Le fichier adherents_imports.csv n'existe pas.")

# Importe et crée une liste d'emprunts avec les attributs : (à voir)
def importer_emprunts(biblio):
    try:
        with open("emprunts.csv", "r", encoding="utf-8") as fichier:
            lignes = fichier.readlines()[1:]
            for ligne in lignes:
                e = ligne.strip().split(",")
                id_adherent, isbn, date = int(e[1]), e[3], e[4]

                try:
                    adherent = next(a for a in biblio.liste_adherents if a.id == id_adherent)
                except StopIteration:
                    print(f"❌ Aucun adhérent avec l'ID {id_adherent} trouvé. Emprunt ignoré.")
                    continue

                try:
                    livre = next(l for l in biblio.liste_documents if l.isbn == isbn)
                except StopIteration:
                    print(f"❌ Aucun document avec l'ISBN {isbn} trouvé. Emprunt ignoré.")
                    continue

                biblio.liste_emprunts.append(Emprunt(adherent, livre, date))

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