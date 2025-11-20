from Classe_Emprunt import Emprunt
from datetime import date

class Adherent:

    def __init__(self, nom: str, prenom: str, bibliotheque):
        self.nom = nom
        self.prenom = prenom
        # Récupérer tous les id déjà utilisés
        used_ids = {e.id for e in bibliotheque.liste_adherents}
        # Trouver le plus petit entier positif qui n'est pas dans used_ids
        new_id = 1
        while new_id in used_ids:
            new_id += 1
        # L’assigner
        self.id = new_id

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
            if x.dispo:
                print(x)

        # Entrer l'ISBN que vous voulez emprunter
        while True:
            print("-" * 120)
            choix_isbn = input("Veuillez saisir l'ISBN du livre à emprunter : ").strip()

            choix_livre = None
            for x in bibliotheque.liste_documents:
                if x.isbn == choix_isbn and x.dispo:
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
        print("✅ Livre emprunté avec succès :\n")
        print(f"{choix_adherent.prenom} {choix_adherent.nom} a emprunté {choix_livre.titre} ({choix_livre.isbn}) le {emprunt.date_emprunt}.\n"
              f"Quantité maintenant disponible : {choix_livre.qte_dispo}")

    @staticmethod
    def rendre_livre(bibliotheque):

        # Demander ID adhérent
        while True:

            try:
                id_adherent = int(input("Veuillez saisir l'ID de l'adhérent : "))
                if id_adherent <= 0:
                    print("❌ L'ID doit être un nombre positif!")
                    continue

            except ValueError:
                print("❌ Veuillez entrer un nombre valide pour l'ID!")
                continue

            adherent_choisi = None
            for adherent in bibliotheque.liste_adherents:
                if hasattr(adherent, 'id') and adherent.id == id_adherent: # hasattr = fonction Python qui vérifie si un objet possède un certain attribut
                    adherent_choisi = adherent
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

        if not liste_emprunts_adherent:
            print("❌ Cet adhérent n'a aucun emprunt en cours!")
            return

        # Classer les emprunts avec un numéro devant
        dictionnaire_emprunts = {}
        numero = 1
        for emprunt in liste_emprunts_adherent:
            dictionnaire_emprunts[numero] = emprunt
            numero += 1

        if not dictionnaire_emprunts:
            print("❌ Aucun emprunt valide trouvé pour cet adhérent!")
            return

        # Afficher les emprunts de cet adhérent la (avec leur numéro à leur gauche)
        print("\nVoici la liste des emprunts :\n")
        for numero, emprunt in dictionnaire_emprunts.items():
            print(f"{numero} - {emprunt.livre.titre} | Emprunté le : {emprunt.date_emprunt}")

        # Le user tape un numéro pour choisir quel emprunt rendre
        while True:
            try:
                choix_input = input("\nEntrez le numéro de l'emprunt que vous voulez rendre : ").strip()
                if not choix_input:
                    print("❌ Le numéro ne peut pas être vide!")
                    continue

                choix = int(choix_input)

                if choix in dictionnaire_emprunts:
                    a_rendre = dictionnaire_emprunts[choix]
                    break
                else:
                    print(
                        f"❌ Numéro invalide. Veuillez choisir un numéro entre {min(dictionnaire_emprunts.keys())} et {max(dictionnaire_emprunts.keys())}")   #dictionnaire_emprunts.keys() : retourne les clés du dictionnaire → [1, 2, 3]
                                                                                                                                                    # min() : donne la plus petite clé → 1
                                                                                                                                                    # max() : donne la plus grande clé → 3

            except ValueError:
                print("❌ Veuillez entrer un nombre valide!")
            except KeyboardInterrupt:
                print("\n❌ Opération annulée par l'utilisateur!")
                return

            # L'emprunt est supprimé de la liste d'emprunt de la bibliothèque
        try:
            for emprunt in bibliotheque.liste_emprunts[:]: # Copie de la liste pour éviter les problèmes lors de la suppression
                if emprunt is a_rendre:
                    # Vérifier et augmenter la quantité disponible
                    if hasattr(emprunt.livre, 'qte_dispo'): # hasattr = Vérifie si l'objet livre possède bien un attribut appelé qte_dispo
                        emprunt.livre.qte_dispo += 1
                    else:
                        print("⚠️  Impossible d'augmenter la quantité disponible - attribut manquant")                                          #Checker ca

                    bibliotheque.liste_emprunts.remove(emprunt)
                    print("✅ Retour complété avec succès!")
                    print(
                        f"{adherent_choisi.prenom} {adherent_choisi.nom} a retourné {emprunt.livre.titre} ({emprunt.livre.isbn}) le {date.today()}.\n"
                        f"Quantité maintenant disponible : {emprunt.livre.qte_dispo}")
                    break
            else:
                print("❌ Erreur: Emprunt non trouvé dans la liste des emprunts!")

        except Exception as e:
            print(f"❌ Erreur lors du retour du livre: {e}")

    # ajouter confirmer identité :
    #   "L'adhérent choisi est Ferland Pinpin. Voulez-vous continuer ou choisir un autre adhérent?"