# Projet Bibliothèque
## Description
Module python développé en programmation orientée objet (POO) permettant la gestion complète d’une bibliothèque à l’aide d’un menu interactif en ligne de commande. L’utilisateur peut gérer les adhérents, les documents, les emprunts et la sauvegarde des données de manière dynamique.
Les données de la bibliothèque sont manipulées à l’aide de fichiers CSV, permettant leur lecture et leur écriture pour assurer la persistance des informations.

- Concepts utilisés : l’encapsulation, l’héritage, le polymorphisme et les classes abstraites.

- Modules utilisés : datetime, abc.

---
## Diagramme UML
![Diagramme UML.png](Images/Diagramme%20UML.png)

### Bibliotheque 
Classe centrale :
- elle agrège plusieurs Adherents (relation 1..*),
- elle gère la liste des Documents (relation 1..*),
- elle maintient la liste des Emprunts.

### Adherent 
- Classe concrète qui peut être associée à 0 à n emprunts (0..n). Chaque emprunt est lié à un seul adhérent.

### Emprunt
- Classe concrète reliant un Adherent à un Livre et contenant les informations temporelles (date_emprunt, date_retour).

### Document
- Classe abstraite (ABC) définissant les attributs communs (titre, isbn, quantite) ainsi que les méthodes abstraites liées au type de document et à la gestion des quantités.

### Volume
- Classe abstraite intermédiaire héritant de Document, ajoutant l’attribut auteur.

### Journal
- Hérite directement de Document et ajoute l’attribut date_publication.

### Les classes concrètes suivantes héritent de Volume : 
- Livre,
- BD,
- Dictionnaire.

---
## Fonctionnalités principales
- Gestion des adhérents (ajout, suppression, affichage)
- Gestion des documents (ajout, suppression, affichage)
- Système d'emprunts et de retours
- Prolongation des emprunts
- Sauvegarde et chargement des données (CSV)

Les dates d’emprunt et de retour sont générées automatiquement, réduisant ainsi les erreurs de saisie.

---
## Exemples d'utilisation
## Menu
Affichage du menu principal au démarrage de l'application.

![Menu.png](Images/Menu.png)


## Ajouter adhérent
Après l'ajout d'un nouvel adhérent valide, un message de confirmation s'affiche et l'adhérent reçoit un ID unique généré automatiquement. L'adhérent est également ajouté à la liste des adhérents.
 
![1AjouterAdherent.png](Images/1AjouterAdherent.png)



## Supprimer adhérent
Lors de la suppression d'un adhérent existant, l'adhérent et ses emprunts associés sont supprimés, puis un message de confirmation s'affiche.

![2SupprimerAdherent.png](Images/2SupprimerAdherent.png)


## Afficher tous les adhérents
Affichage de la liste complète de tous les adhérents avec leur nom, prénom et ID.

![3AfficherAdherents.png](Images/3AfficherAdherents.png)


## Ajouter document 
Après l'ajout d'un document valide, un message de confirmation s'affiche et le document est ajouté à la liste des documents.

![4AjouterDocument.png](Images/4AjouterDocument.png)


## Supprimer document
Lors de la suppression d'un document existant, l'adhérent et ses emprunts associés sont supprimés, puis un message de confirmation s'affiche.

![5SupprimerDocument.png](Images/5SupprimerDocument.png)


## Afficher tous les documents
Affichage de la liste de tous les documents avec titre, auteur, ISBN, quantité disponible/totale.

![6AfficherDocs.png](Images/6AfficherDocs.png)


## Emprunter un livre
Pour emprunter un livre, l'utilisateur doit saisir son ID d'adhérent.
Ensuite, la liste des livres disponibles s'affichera. Si la saisie de l'ISBN est relié à un livre disponible, un message de confirmation apparaitra et la quantité disponible pour ce livre sera mise-à-jour automatiquement.

![7EmprunterDoc.png](Images/7EmprunterDoc.png)


## Retour d'un emprunt
Pour retourner un emprunt, l'utilisateur doit saisir son ID d'adhérent.
Ensuite, la liste de ses emprunts s'affichera. Si la saisie du numéro de l'emprunt est valide, un message de confirmation s'affichera, puis la quantité disponible pour ce livre et la liste d'emprunt de cet adhérent seront mis-à-jour automatiquement.

![8RetourDemprunt.png](Images/8RetourDemprunt.png)


## Afficher tous les emprunts
Affichage de la liste de tous les emprunts en cours avec : nom de l'adhérent, titre du livre, ISBN, date d'emprunt et date de retour prévue.

![9AfficherEmprunts.png](Images/9AfficherEmprunts.png)


## Prolonger un emprunt
Pour prolonger un emprunt, l'utilisateur doit saisir son ID d'adhérent.
Ensuite, la liste de ses emprunts s'affichera. Si la saisie du numéro de l'emprunt est valide, un message de confirmation avec la nouvelle date de retour (ancienne date + 14 jours) s'affichera.

![10ProlongerEmprunt.png](Images/10ProlongerEmprunt.png)


## Sauvegarder les modifications
Une fois cette option sélectionnée, les fichiers CSV sont mis à jour et un message de confirmation s'affiche.

![Sauvegarde.png](Images/Sauvegarde.png)


## Quitter le programme 
Permet de quitter le programme.

![Quitter.png](Images/Quitter.png)


## Prise en charge des erreurs de saisies
Les saisies erronées sont prises en compte par le programme pour l’ensemble des saisies utilisateur. Des messages d’erreur clairs sont affichés et des boucles permettent à l’utilisateur de corriger son entrée sans interrompre l’exécution du programme. 
En voici quelques exemples :

![ErreursSaisies1.png](Images/ErreursSaisies1.png)

![ErreursSaisies4.png](Images/ErreursSaisies4.png)

![ErreursSaisies2.png](Images/ErreursSaisies2.png)

![ErreursSaisies3.png](Images/ErreursSaisies3.png)

---
## Auteurs
Projet réalisé par Eric De Celles, Valérie Ouellet et William Bourbonnière dans dans le cadre du cours 420-2PR-BB Programmation orientée objet.
Collège Bois-de-Boulogne
14/12/2025