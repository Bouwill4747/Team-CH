from Bibliotheque import Bibliotheque
from Adherent import Adherent
from Emprunt import Emprunt
import Affichage
import Sauvegarde

def retour_au_menu():
    input("\n👆 Appuyez sur Entrée pour retourner au menu...\n")

def afficher_menu(biblio):

    print("\n\n")
    print("=" * 60)
    print(f"🌟  BIENVENUE À {biblio.nom_bibliotheque.upper()}  🌟")
    print("=" * 60)
    print("Choisissez une option :")
    print("-" * 40)

    menu_items = [
        (1, "Ajouter adhérent 👴"),
        (2, "Supprimer adhérent🤵 "),
        (3, "Afficher tous les adhérents 👨‍💼"),
        (4, "Ajouter document 📘"),
        (5, "Supprimer document 🚨"),
        (6, "Afficher tous les documents 📃"),
        (7, "Emprunter un livre 📗"),
        (8, "Retour d'un emprunt 📕"),
        (9, "Afficher tous les emprunts 📃"),
        (10, "Prolonger un emprunt 📈"),
        (11, "Sauvegarder les modifications ✅"),
        ("Q", "Quitter le programme ❌")
    ]

    for key, desc in menu_items:
        print(f"  {key:2} - {desc}")

    print("=" * 60)

    # Boucle de saisie utilisateur
    while True:
        choix_utilisateur = input("👉 Choisissez une action (1-11 ou Q pour quitter) : ").strip()
        match choix_utilisateur.upper():
            case 'Q':
                return 'Q'
            case choix_str if choix_str.isdigit() and 1 <= int(choix_str) <= 11:
                return int(choix_str)
            case _:
                print("❌ Choix erroné ! Veuillez entrer un nombre entre 1 et 11 ou Q.")

# --- Main :) ---
if __name__ == "__main__":

    biblio = Bibliotheque("Bibliotheque BDEB")
    Sauvegarde.importer_documents(biblio)  # Importe automatiquement les documents quand la bibliothèque est créée
    Sauvegarde.importer_adherents(biblio)  # Importe automatiquement les adhérents quand la bibliothèque est créée
    Sauvegarde.importer_emprunts(biblio)  # Importe automatiquement les emprunts quand la bibliothèque est cré

    while True:
        choix = afficher_menu(biblio)

        match choix:
            case 'Q':
                print("\nMerci d'avoir utilisé la bibliothèque ! À bientôt 👋")
                break

            case 1:
                biblio.ajouter_ad()

            case 2:
                biblio.enlever_ad()

            case 3:
                Affichage.afficher_liste_adherents(biblio)
                retour_au_menu()

            case 4:
                biblio.ajouter_doc()

            case 5:
                biblio.enlever_doc()

            case 6:
                Affichage.afficher_liste_docs(biblio)
                retour_au_menu()

            case 7:
                Adherent.emprunter_livre(biblio)
                retour_au_menu()

            case 8:
                Adherent.rendre_livre(biblio)

            case 9:
                Affichage.afficher_liste_emprunts(biblio)
                retour_au_menu()

            case 10:
                Emprunt.menu_prolonger_emprunt(biblio)

            case 11 :
                Sauvegarde.sauvegarder_livres(biblio)
                Sauvegarde.sauvegarder_adherents(biblio)
                Sauvegarde.sauvegarder_emprunts(biblio)
                print("\nSauvegarde complétée.")

            case _:
                print("❌ Option non reconnue !")
