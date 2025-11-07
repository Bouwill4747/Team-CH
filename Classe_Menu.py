def afficherMenu(nom_biblio="Bibliotheque BDEB"):

    # Titre principal
    print("************************************************************")
    print(f"*   Bienvenue à votre bibliothèque : {nom_biblio.center(25)}*")
    print("************************************************************")
    print("*                Faites un choix :                         *")
    print("************************************************************")

    # Liste des options
    options = [
        "1   Ajouter adhérent",
        "2   Supprimer adhérent",
        "3   Afficher tous les adhérents",
        "4   Ajouter document",
        "5   Supprimer document",
        "6   Afficher tous les documents",
        "7   Ajouter emprunt",
        "8   Retour d’un emprunt",
        "9   Afficher tous les emprunts",
        "10  Prolonger un emprunt",
        "11  Sauvegarder les modifications",
        "Q   Quitter le programme"
    ]

    # Affichage des options
    for ligne in options:
        print(f"*   {ligne.ljust(52)}*")

    print("************************************************************")

    # Boucle de saisie utilisateur
    while True:
        choix = input("👉 Choisissez une action (1-11 ou Q pour quitter) : ").strip()
        if choix.upper() == 'Q':
            return 'Q'
        if choix.upper() == '1':
            pass
        if choix.upper() == '2':
            pass
        if choix.upper() == '3':
            pass
        if choix.upper() == '4':
            pass
        if choix.upper() == '5':
            pass
        if choix.upper() == '6':
            pass
        if choix.upper() == '7':
            pass
        if choix.upper() == '8':
            pass
        if choix.upper() == '9':
            pass
        if choix.upper() == '10':
            pass
        if choix.upper() == '11':
            pass
        if choix.isdigit() and 1 <= int(choix) <= 11:
            return int(choix)
        print("❌ Choix erroné ! Veuillez entrer un nombre entre 1 et 11 ou Q.")

# --- Exemple d'utilisation ---
if __name__ == "__main__":
    while True:
        choix = afficherMenu("Bibliotheque BDEB")
        if choix == 'Q':
            print("\nMerci d'avoir utilisé la bibliothèque ! À bientôt 👋")
            break
        else:
            print(f"\n→ Vous avez choisi l'option {choix}\n")
            input("Appuyez sur Entrée pour revenir au menu...")
