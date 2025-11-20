import csv

def sauvegarder_livres(biblio, chemin_fichier):
    with open(chemin_fichier, "w", newline="", encoding="utf-8") as f:
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


def sauvegarder_adherents(biblio, chemin_fichier):
    with open(chemin_fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Prénom", "Nom", "ID"])

        for adherent in biblio.liste_adherents:
            writer.writerow([
                adherent.prenom,
                adherent.nom,
                adherent.id
            ])


def sauvegarder_emprunts(biblio, chemin_fichier):
    with open(chemin_fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Adhérent", "ID d'adhérent", "Titre du livre", "ISBN", "Date d'emprunt", "Date de retour"])

        for emprunt in biblio.liste_emprunts:
            writer.writerow([
                emprunt.adherent.prenom + " " + emprunt.adherent.nom,
                emprunt.livre.titre,
                emprunt.livre.isbn,
                emprunt.date_emprunt,
                emprunt.date_retour
            ])