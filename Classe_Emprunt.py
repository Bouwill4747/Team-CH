from datetime import date, timedelta
from Classe_Adherent import *
from Classe_Document import *

class Emprunt:

        # J'ai enlevé les dates dans l'input du constructeur parce qu'elles sont maintenant établies automatiquement
    def __init__(self, adherent: Adherent, livre: Livre):
        self.date_emprunt = date.today()
        self.date_retour = self.date_emprunt + timedelta(14) # Date d'emprunt + 14 jours
        self.adherent = adherent
        self.livre = livre

    def __str__(self):# *À finaliser*
        return f"{self.adherent.prenom} {self.adherent.nom} a emprunté {self.livre.titre} ({self.livre.isbn}) le {self.date_emprunt}."

    def prolonger_date_retour(self, jours_extra: int):
        self.date_emprunt += timedelta(jours_extra)


# # ------------ TESTS-------------
# adherent1 = Adherent("De Celles", "Eric", 1535)
# livre1 = Livre("L'étranger", "ISBN-123", 3, "Albert Camus")
# emprunt = Emprunt(adherent1, livre1)
# print(emprunt)