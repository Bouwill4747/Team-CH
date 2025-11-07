from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def afficherMenu(nom_biblio="Bibliothèque municipale"):

    console.clear()
    console.rule(f"[bold cyan]📚 Bienvenue à {nom_biblio} 📚", style="bright_yellow")

    # Création du tableau du menu
    table = Table(show_header=False, header_style="bold magenta", style="bright_white on black")
    table.add_column("Option", justify="center", style="bold green")
    table.add_column("Description", style="white")

    table.add_row("1", "Ajouter adhérent")
    table.add_row("2", "Supprimer adhérent")
    table.add_row("3", "Afficher tous les adhérents")
    table.add_row("4", "Ajouter document")
    table.add_row("5", "Supprimer document")
    table.add_row("6", "Afficher tous les documents")
    table.add_row("7", "Ajouter emprunt")
    table.add_row("8", "Retour d’un emprunt")
    table.add_row("9", "Afficher tous les emprunts")
    table.add_row("10", "Prolonger un emprunt")
    table.add_row("11", "Sauvegarder les modifications")
    table.add_row("[red]Q[/red]", "Quitter le programme")

    console.print(Panel.fit(table, title="[bold yellow]Menu principal", border_style="bright_blue"))

    while True:
        choix = Prompt.ask("[bold green]👉 Choisissez une action (1-11 ou Q pour quitter)[/bold green]").strip()
        if choix.upper() == "Q":
            return "Q"
        if choix.upper() == '1':
            pass
        if choix.upper() == '2':
            pass
        if choix.upper() == '3':
            pass
        if choix.upper() == '4':
            pass
        if choix.upper() == '5':
            pass
        if choix.upper() == '6':
            pass
        if choix.upper() == '7':
            pass
        if choix.upper() == '8':
            pass
        if choix.upper() == '9':
            pass
        if choix.upper() == '10':
            pass
        if choix.upper() == '11':
            pass
        if choix.isdigit() and 1 <= int(choix) <= 11:
            return int(choix)
        console.print("[bold red]❌ Choix erroné ![/bold red] Veuillez entrer un nombre entre 1 et 11 ou Q.")

# --- Exemple d'utilisation ---
if __name__ == "__main__":
    while True:
        choix = afficherMenu("Médiathèque de Paris")
        if choix == "Q":
            console.print("\n[bold cyan]Merci d'avoir utilisé la bibliothèque ! À bientôt 👋[/bold cyan]")
            break
        else:
            console.print(f"[yellow]→ Vous avez choisi l'option {choix}[/yellow]\n")
            console.input("Appuyez sur [bold magenta]Entrée[/bold magenta] pour revenir au menu...")
