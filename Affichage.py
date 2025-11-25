# Affiche la liste complète des documents, adhérents et emprunts
def afficher_liste_docs(biblio):
    print("="*60)
    print("                  Liste des documents")
    print("="*60)

    for doc in biblio.liste_documents:
        dash_line = '-' * (len(doc.titre) + 4)
        print(f"\n |{dash_line}|\n"
              f" |  {doc.titre}  |\n"
              f" |{dash_line}|\n"
              f"Titre : «{doc.titre}» | Auteur : {doc.auteur} | Quantité disponible : {str(doc.qte_dispo)}/{str(doc.quantite)} | ISBN : {doc.isbn}\n")


def afficher_liste_adherents(biblio):
    print("="*60)
    print("                  Liste des adhérents")
    print("="*60)

    for adherent in biblio.liste_adherents:
        print(f"Nom : {adherent.nom} | Prénom : {str(adherent.prenom)} | ID : {adherent.id}\n")


def afficher_liste_emprunts(biblio):
    print("="*60)
    print("                  Liste d'emprunts")
    print("="*60)

    for emprunt in biblio.liste_emprunts:
        print(
            f"{emprunt.adherent.prenom} {emprunt.adherent.nom} a emprunté «{emprunt.livre.titre}» ({emprunt.livre.isbn}) le {emprunt.date_emprunt} et dois le retourner pour le {emprunt.date_retour}.\n")