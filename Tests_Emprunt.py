# Sert à tester les méthodes emprunter_livre et rendre_livre
from Classe_Adherent import Adherent
from Classe_Document import Livre
from Classe_Emprunt import Emprunt

adherent1 = Adherent("De Celles", "Eric", 1535)
livre1 = Livre("L'étranger", "ISBN-123", 3, "Albert Camus")

emprunt = Emprunt(adherent1, livre1)
print(emprunt)
