# Sert à tester les méthodes emprunter_livre et rendre_livre
from Classe_Adherent import Adherent
from Classe_Document import Livre
from Classe_Emprunt import Emprunt
from Classe_Bibliotheque import Bibliotheque

# adherent1 = Adherent("De Celles", "Eric", 1535)
# livre1 = Livre("L'étranger", "ISBN-123", 3, "Albert Camus")
#
# emprunt = Emprunt(adherent1, livre1)
# print(emprunt)



biblio1 = Bibliotheque("Ma Bibliothèque")
biblio1.importer_docs()

print("************************************************************")
print("*             === Liste d'Emprunts ===                     *")
print("************************************************************")

for doc in biblio1.liste_documents:
    dash_line = '-' * (len(doc.titre) + 4)
    print(f"\n |{dash_line}|\n"
          f" |  {doc.titre}  |\n"
          f" |{dash_line}|\n"
          f"Titre : {doc.auteur} | Quantité : {str(doc.quantite)} | ISBN : {doc.isbn}\n")


#               |The Picture of Dorian Gray|
