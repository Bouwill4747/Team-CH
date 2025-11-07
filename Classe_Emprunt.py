class Emprunt:

    def __init__(self, dateEmprunt: str, dateRetour: str, adherant, livre):
        self.dateEmprunt = dateEmprunt
        self.dateRetour = dateRetour
        self.adherant = adherant
        self.livre = livre

    def prolongerDateRetour(self):
        pass