from Adherent import Adherent
from Document import Livre
from Emprunt import Emprunt
from Bibliotheque import Bibliotheque

biblio = Bibliotheque("Bibliothèque BdeB")
# biblio.liste_adherents[0].emprunter_livre(biblio)
Adherent.rendre_livre(biblio)