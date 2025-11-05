# À FAIRE : protéger certaines variables contre les modifications directes? (i.e. utiliser setters)

# La classe Document comprend également tous ses enfants
# (pour avoir juste une classe à importer au lieu de 6)

from abc import ABC, abstractmethod


class Document(ABC): # Classe abstraite

    def __init__(self, titre: str, isbn: str, quantite: int):
        if quantite < 0:
            # Le texte entre les "" ici peut être utilisé par un bloc try-except (ce qui n'est pas encore le cas).
            raise ValueError("❌ ERREUR: La quantité initiale ne peut pas être négative.")  # Le programme est interrompu.
        if quantite == 0:
            print("⚠️ ATTENTION: Le document a été créé avec une quantité de 0.") # C'est possible que ce message-là soit déplacé.
        self.titre = titre
        self.isbn = isbn
        self.quantite = quantite

    @property # C'est un attribut dynamique qui se calcule à chaque fois qu'il est accédé.
    @abstractmethod
    def type_document(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError

    def aug_quantite(self, qte_aug: int):
        if qte_aug > 0:
            self.quantite += qte_aug
            print("✅ Opération réussie") # C'est possible que tous ces messages-là soient déplacés dans la ou les méthodes qui vont utiliser aug_quantite et red_quantite
        else:
            print("❌ ERREUR: La quantité à ajouter doit être positive. Veuillez réessayer.")

    def red_quantite(self, qte_red: int):
        if qte_red <= 0:
            print("❌ ERREUR: La quantité à retirer doit être positive. Veuillez réessayer.")
        elif qte_red > self.quantite:
            print("❌ ERREUR: Quantité insuffisante en inventaire.")
        else:
            self.quantite -= qte_red
            print("✅ Opération réussie")


class Journal(Document):

    def __init__(self, titre: str, isbn: str, quantite: int, date_publication: str):
        super().__init__(titre, isbn, quantite)
        self.date_publication = date_publication

    @property
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
        self.qte_dispo = quantite # Prend pour acquis qu'un livre ne peut pas être emprunté en même temps d'être créé.

    @property
    def type_document(self):
        return "Livre"

    @property
    def dispo(self):
        return self.qte_dispo > 0

    def __str__(self):
        return (f"({self.type_document}) {self.titre}, ISBN: {self.isbn}, auteur: {self.auteur}, "
                f"Quantité disponible: {self.qte_dispo}/{self.quantite}")

    def aug_quantite(self, qte_aug: int):
        if qte_aug > 0:
            self.quantite += qte_aug
            self.qte_dispo += qte_aug
            print("✅ Opération réussie")
        else:
            print("❌ ERREUR: La quantité à ajouter doit être positive. Veuillez réessayer.")

    def red_quantite(self, qte_red: int):
        if qte_red <= 0:
            print("❌ ERREUR: La quantité à retirer doit être positive. Veuillez réessayer.")
        elif qte_red > self.quantite:
            print("❌ ERREUR: Quantité insuffisante en inventaire.")
        elif qte_red > self.qte_dispo:
            print("❌ ERREUR: Quantité insuffisante de livres disponibles. Les livres doivent être rendus avant d'être retirés de la bibliothèque")
        else:
            self.quantite -= qte_red
            self.qte_dispo -= qte_red
            print("✅ Opération réussie")



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



###########     TESTS     ################

if __name__ == "__main__":
    # Création de quelques objets
    print("=== TEST DES CLASSES DE DOCUMENTS ===\n")

    # Test du Journal
    journal1 = Journal("Le Devoir", "ISSN-001", 10, "2025-10-15")
    print(journal1)

    # Test du Livre avec quantité valide
    livre1 = Livre("L'étranger", "ISBN-123", 3, "Albert Camus")
    print(livre1)

    # Test du Livre avec quantité 0
    livre2 = Livre("1984", "ISBN-456", 0, "George Orwell")
    print(livre2)

    # Test de la disponibilité
    print(f"Le livre '{livre1.titre}' est-il disponible ? {livre1.dispo}")
    print(f"Le livre '{livre2.titre}' est-il disponible ? {livre2.dispo}")
    print()

    # Test des méthodes d’ajout et de réduction de quantité
    print("Augmentation de la quantité de 2 exemplaires du livre1...")
    livre1.aug_quantite(2)
    print(livre1)

    print("Réduction de la quantité de 3 exemplaires du livre1...")
    livre1.red_quantite(3)
    print(livre1)

    print("Tentative de retirer une quantité invalide (-1)...")
    livre1.red_quantite(-1)
    print()

    # Test de la BD
    bd1 = BD("Astérix et Obélix", "ISBN-321", 5, "René Goscinny", "Albert Uderzo")
    print(bd1)

    # Test du Dictionnaire
    dico1 = Dictionnaire("Larousse", "ISBN-654", 2, "Éditions Larousse")
    print(dico1)

    print("\n=== FIN DES TESTS ===")

