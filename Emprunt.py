from datetime import datetime, timedelta

class Emprunt:

        # J'ai enlevé les dates dans l'input du constructeur parce qu'elles sont maintenant établies automatiquement
    def __init__(self, adherent, livre, date: str = None):
        if date is not None:
            self.date_emprunt = datetime.strptime(date, "%Y-%m-%d").date()
        else:
            self.date_emprunt = datetime.today().date() # la date d'aujourd'hui
        self.date_retour = self.date_emprunt + timedelta(days=14)
        self.adherent = adherent
        self.livre = livre
        livre.qte_dispo -= 1

    def __str__(self):# *À finaliser comme on veut*
        return f"{self.adherent.prenom} {self.adherent.nom} a emprunté {self.livre.titre} ({self.livre.isbn}) le {self.date_emprunt} et doit le retourner pour le {self.date_retour}"

    def prolonger_date_retour(self):
         self.date_retour += timedelta(14)

    @staticmethod
    def menu_prolonger_emprunt(bibliotheque):

        while True:
            # --- Choisir adhérent ---
            try:
                id_adherent = int(input("Veuillez saisir l'ID de l'adhérent : "))
                if id_adherent <= 0:
                    print("❌ L'ID doit être un nombre positif!")
                    continue
            except ValueError:
                print("❌ Veuillez entrer un nombre valide!")
                continue

            adherent_choisi = None
            for ad in bibliotheque.liste_adherents:
                if ad.id == id_adherent:
                    adherent_choisi = ad
                    break

            if adherent_choisi is None:
                print("❌ Aucun adhérent trouvé avec cet ID!")
                continue

            # --- Trouver les emprunts de cet adhérent ---
            emprunts_adherent = [
                emp for emp in bibliotheque.liste_emprunts
                if emp.adherent.id == adherent_choisi.id
            ]

            if not emprunts_adherent:
                print("❌ Cet adhérent n'a aucun emprunt!")
                return

            # --- Afficher les emprunts ---
            print("\n📚 Emprunts de cet adhérent :")
            for i, emp in enumerate(emprunts_adherent, start=1):
                print(f"{i} - {emp.livre.titre} | Retour prévu : {emp.date_retour}")

            # --- Choisir emprunt ---
            while True:
                try:
                    choix = int(input("\nEntrez le numéro de l'emprunt à prolonger : "))
                    if 1 <= choix <= len(emprunts_adherent):
                        emprunt_choisi = emprunts_adherent[choix - 1]
                        break
                    else:
                        print("❌ Numéro invalide!")
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide!")

            # --- Prolongation ---
            emprunt_choisi.date_retour += timedelta(14)

            print(f"\n✅ Prolongation réussie !")
            print(f"Nouvelle date de retour pour « {emprunt_choisi.livre.titre} » : {emprunt_choisi.date_retour}")

            # --- Refaire une prolongation ? ---
            again = input("\nVoulez-vous prolonger un autre emprunt ? (O/N) : ").strip().upper()
            if again != "O":
                break
