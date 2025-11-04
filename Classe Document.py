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

    @property # C'est un attribut dynamique qui se calcule à chaque fois qu'il est accédé.
    def type_document(self):
        return "Journal"

    def __str__(self):
        return f"({self.type_document}) {self.titre}, ISBN: {self.isbn}, qté: {self.quantite}, Publication: {self.date_publication}"


class Volume(Document, ABC): # Classe abstraite

    def __init__(self, titre: str, isbn: str, quantite: int, auteur: str):
        super().__init__(titre, isbn, quantite)
        self.auteur = auteur


class Livre(Volume):

    def __init__(self, titre: str, isbn: str, quantite: int, auteur: str):
        super().__init__(titre, isbn, quantite, auteur)

        if quantite > 0:
            self.qte_dispo = quantite
        elif quantite == 0:
            self.qte_dispo = quantite
            print("⚠️ ATTENTION: Le document a été créé avec une quantité de 0.")
        else:
            print("❌ ERREUR: La quantité ne peut pas être négative. Veuillez réessayer.")

    @property
    def type_document(self):
        return "Livre"

    @property
    def dispo(self):
        return self.qte_dispo > 0

    def __str__(self):
        return (f"({self.type_document}) {self.titre}, ISBN: {self.isbn}, auteur: {self.auteur},"
                f"Quantité disponible: {self.qte_dispo}/{self.quantite}")

    def aug_quantite(self, qte_aug: int):
        if qte_aug > 0:
            self.quantite += qte_aug
            self.qte_dispo += qte_aug
        else:
            print("❌ ERREUR: La quantité à ajouter doit être positive. Veuillez réessayer.")

    def red_quantite(self, qte_red: int):
        if qte_red <= 0:
            print("❌ ERREUR: La quantité à retirer doit être positive. Veuillez réessayer.")
        elif qte_red <= self.qte_dispo:
            self.quantite -= qte_red
            self.qte_dispo -= qte_red
        else:
            print("❌ ERREUR: Quantité insuffisante de livres disponibles. Les livres doivent être rendus avant d'être retirés de la bibliothèque")


class BD(Volume):

    def __init__(self, titre: str, isbn: str, quantite: int, auteur: str, dessinateur: str):
        super().__init__(titre, isbn, quantite, auteur)
        self.dessinateur = dessinateur

    @property
    def type_document(self):
        return "BD"

    def __str__(self):
        return f"({self.type_document}) {self.titre}, ISBN: {self.isbn}, qté: {self.quantite}, auteur: {self.auteur}, dessinateur: {self.dessinateur}"


class Dictionnaire(Volume):

    def __init__(self, titre: str, isbn: str, quantite: int, auteur: str):
        super().__init__(titre, isbn, quantite, auteur)

    @property
    def type_document(self):
        return "Dictionnaire"

    def __str__(self):
        return f"({self.type_document}) {self.titre}, ISBN: {self.isbn}, qté: {self.quantite}, auteur: {self.auteur}"
