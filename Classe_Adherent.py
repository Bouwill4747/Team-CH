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

# Dans la liste emprunt, Adhérant, Livre et Date


    def rendre_livre(self, bibliotheque, livre):

        # Demander ID adhérent
        # Classer les emprunts avec un numméro devant
        # Afficher les emprunts de cet adhérent la (avec leur numéro à leur gauche)
        # Le user tape un numéro pour choisir quel emprunt rendre
        #
        # Et ici j'me demande si on devrait pas demander d'entrer un nom d'adhérent, ensuite afficher les
        # livres qu'il a empruntés, et ensuite demander d'entrer l'ISBN du livre à rendre.

        # adherent = input("Veuillez saisir l'ID d'adhérent : ")
        # for x in bibliotheque.liste_adherents:
        #     if x.

        pass