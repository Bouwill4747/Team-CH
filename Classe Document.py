# La classe Document comprend également tous ses enfants
# (pour avoir juste une classe à importer au lieu de 6)

from abc import ABC, abstractmethod

class Document(ABC): # Classe abstraite
    def __init__(self, titre: str, isbn: str, quantite: int):
        self.titre = titre
        self.isbn = isbn
        self.quantite = quantite

class Journal(Document):
    def __init__(self, titre: str, isbn: str, quantite: int, date_publication: str):
        super().__init__(titre, isbn, quantite)
        self.date_publication = date_publication

    def __str__(self):
        return f"(Journal) {self.titre}, ISBN: {self.isbn}, qté: {self.quantite}, Publication: {self.date_publication}"

class Volume(Document): # Classe abstraite
    def __init__(self, titre: str, isbn: str, quantite: int, auteur: str):
        super().__init__(titre, isbn, quantite)
        self.auteur = auteur

class Livre(Volume):
    def __init__(self, titre: str, isbn: str, quantite: int, auteur: str):
        super().__init__(titre, isbn, quantite, auteur)

        # On prend pour acquis qu'un livre nouvellement créé n'a pas encore été emprunté.
        self.quantite_dispo = quantite

        if self.quantite_dispo > 0:
            self.dispo = True
        else:
            self.dispo = False
            print("⚠️ ATTENTION: Le document a été créé avec une quantité de 0.")

    def __str__(self):
        return f"(Livre) {self.titre}, ISBN: {self.isbn}, qté: {self.quantite}, auteur: {self.auteur}"

    # C'est dans le diagramme du TP, mais je sais pas si c'est nécessaire...
    def empruntable(self):
        return self.dispo




