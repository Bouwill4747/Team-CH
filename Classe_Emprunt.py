class Emprunt:

    def __init__(self, dateEmprunt: str, dateRetour: str, adherent, livre):
        self.dateEmprunt = dateEmprunt
        self.dateRetour = dateRetour
        self.adherant = adherent
        self.livre = livre

    def prolongerDateRetour(self):
        pass