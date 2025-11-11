from datetime import date, timedelta
import random

class Emprunt:

        # J'ai enlevé les dates dans l'input du constructeur parce qu'elles sont maintenant établies automatiquement
    def __init__(self, adherent, bibliotheque, livre):
        self.date_emprunt = date.today()
        self.date_retour = self.date_emprunt + timedelta(14) # Date d'emprunt + 14 jours
        self.adherent = adherent
        self.livre = livre
        while True:
            id_emprunt = random.randint(1, 100)
            for x in bibliotheque.liste_emprunts:
                if id_emprunt == x.id_emprunt:
                    break
            else:
                self.id_emprunt = id_emprunt
                break

    def __str__(self):# *À finaliser comme on veut*
        return f"{self.adherent.prenom} {self.adherent.nom} a emprunté {self.livre.titre} ({self.livre.isbn}) le {self.date_emprunt}. ID d'emprunt : {self.id_emprunt}"

    def prolonger_date_retour(self, jours_extra: int):
        self.date_retour += timedelta(jours_extra)



