from Classe_Adherent import Adherent
from Classe_Document import Livre
from Classe_Emprunt import Emprunt
from Classe_Bibliotheque import Bibliotheque

biblio = Bibliotheque("Bibliothèque BdeB")
# biblio.liste_adherents[0].emprunter_livre(biblio)
for x in biblio.liste_emprunts:
    print(x)