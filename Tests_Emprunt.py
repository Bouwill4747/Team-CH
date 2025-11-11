# Sert à tester les méthodes emprunter_livre et rendre_livre
from Classe_Adherent import Adherent
from Classe_Document import Livre
from Classe_Emprunt import Emprunt
from Classe_Bibliotheque import Bibliotheque

biblio = Bibliotheque("Bibliothèque BdeB")
Adherent.emprunter_livre(biblio)
print(biblio.liste_emprunts[0])