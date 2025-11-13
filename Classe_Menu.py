from Classe_Bibliotheque import Bibliotheque
from Classe_Adherent import Adherent
from Classe_Emprunt import Emprunt
from Classe_Document import *

def sauvegarder_modification():
    pass

def retour_au_menu():
    input("\n👆 Appuyez sur Entrée pour retourner au menu...\n")

def afficher_menu(nom_biblio="Bibliotheque BDEB"):

    print("\n\n")
    print("=" * 60)
    print(f"🌟  BIENVENUE À {nom_biblio.upper()}  🌟")
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
        choix = input("👉 Choisissez une action (1-11 ou Q pour quitter) : ").strip()
        if choix.upper() == 'Q':
            return 'Q'
        elif choix.isdigit() and 1 <= int(choix) <= 11:
            return int(choix)
        print("❌ Choix erroné ! Veuillez entrer un nombre entre 1 et 11 ou Q.")

# --- Main :) ---
if __name__ == "__main__":

    biblio1 = Bibliotheque("Bibliotheque BDEB")

    while True:
        choix = afficher_menu("Bibliotheque BDEB")
        if choix == 'Q':
            print("\nMerci d'avoir utilisé la bibliothèque ! À bientôt 👋")
            break
        elif choix == 1:
            biblio1.ajouter_ad()

        elif choix == 2:
            biblio1.enlever_ad()

        elif choix == 3:
            biblio1.afficher_liste_adherents()
            retour_au_menu()

        elif choix == 4:
            biblio1.ajouter_doc()

        elif choix == 5:
            biblio1.enlever_doc()

        elif choix == 6:
            biblio1.afficher_liste_docs()
            retour_au_menu()

        elif choix == 7:
            Adherent.emprunter_livre(biblio1)
            print(biblio1.liste_emprunts[0])
            retour_au_menu()

        elif choix == 8:
            Adherent.rendre_livre(biblio1)

        elif choix == 9:
            biblio1.afficher_liste_emprunts()
            retour_au_menu()

        elif choix == 10:
            Emprunt.prolonger_date_retour(biblio1)

        elif choix == 11:
            sauvegarder_modification()
