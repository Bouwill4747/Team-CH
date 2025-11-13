from Classe_Emprunt import Emprunt

class Adherent:

    def __init__(self, nom: str, prenom: str, id_adherent: int):
        self.nom = nom
        self.prenom = prenom
        self.id = id_adherent

    @staticmethod
    def emprunter_livre(bibliotheque):

        while True:
            while True:
                try:
                    id_adherent = int(input("Veuillez saisir l'ID de l'adhérent : "))
                    if id_adherent <= 0:
                        print("❌ L'ID doit être un nombre positif!")
                        continue
                    break
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide pour l'ID!")

            choix_adherent = None
            for x in bibliotheque.liste_adherents:
                if x.id == id_adherent:
                    choix_adherent = x
                    break

            if choix_adherent is not None:
                break
            else:
                print("❌ Aucun adhérent trouvé avec cet ID!")
                print("Veuillez réessayer...\n")

        # Afficher les documents dispos avec ISBN et qté dispo
        print("-" * 60)
        print("📚 Documents disponibles :")
        print("-" * 120)
        for x in bibliotheque.liste_documents:
            if x.dispo and x.qte_dispo > 0:
                print(x)

        # Entrer l'ISBN que vous voulez emprunter
        while True:
            print("-" * 120)
            choix_isbn = input("Veuillez saisir l'ISBN du livre à emprunter : ").strip()

            choix_livre = None
            for x in bibliotheque.liste_documents:
                if x.isbn == choix_isbn:
                    choix_livre = x
                    break

            if choix_livre is not None:
                print("-" * 60)
                break
            else:
                print("❌ ISBN non trouvé ou livre non disponible!")
                print("Veuillez réessayer...\n")

        emprunt = Emprunt(choix_adherent, bibliotheque, choix_livre)
        choix_livre.qte_dispo -= 1
        bibliotheque.liste_emprunts.append(emprunt)

    @staticmethod
    def rendre_livre(bibliotheque):

        # Demander ID adhérent
        while True:
            while True:
                try:
                    id_adherent = int(input("Veuillez saisir l'ID de l'adhérent : "))
                    if id_adherent <= 0:
                        print("❌ L'ID doit être un nombre positif!")
                        continue
                    break
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide pour l'ID!")

            adherent_choisi = None
            for x in bibliotheque.liste_adherents:
                if x.id == id_adherent:
                    adherent_choisi = x
                    break

            if adherent_choisi is not None:
                break
            else:
                print("❌ Aucun adhérent trouvé avec cet ID!")
                print("Veuillez réessayer...\n")

        # Créer une liste des emprunts de cet adhérent seulement
        liste_emprunts_adherent = []
        for emprunt in bibliotheque.liste_emprunts:
            if emprunt.adherent.id == adherent_choisi.id:
                liste_emprunts_adherent.append(emprunt)

        # Classer les emprunts avec un numéro devant
        dictionnaire_emprunts = {}
        numero = 1
        for emprunt in liste_emprunts_adherent:
            dictionnaire_emprunts[numero] = emprunt
            numero += 1

        # Afficher les emprunts de cet adhérent la (avec leur numéro à leur gauche)
        print("\nVoici la liste des emprunts :\n")
        for numero, emprunt in dictionnaire_emprunts.items():
            print(f"{numero} - {emprunt.livre.titre} | Emprunté le : {emprunt.date_emprunt}")

        # Le user tape un numéro pour choisir quel emprunt rendre
        choix = int(input("\nEntrez le numéro de l'emprunt que vous voulez rendre : "))
        while choix not in dictionnaire_emprunts:
            choix = int(input("Numéro invalide. Essayez encore : "))
        a_rendre = dictionnaire_emprunts[choix]

        # L'emprunt est supprimé de la liste d'emprunt de la bibliothèque
        for emprunt in bibliotheque.liste_emprunts:
            if emprunt is a_rendre:
                emprunt.livre.qte_dispo += 1
                bibliotheque.liste_emprunts.remove(emprunt)
                print("Emprunt complété avec succès!")
                break